import sys

from crossword import *


class CrosswordCreator:
    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy() for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont

        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size, self.crossword.height * cell_size),
            "black",
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                rect = [
                    (j * cell_size + cell_border, i * cell_size + cell_border),
                    (
                        (j + 1) * cell_size - cell_border,
                        (i + 1) * cell_size - cell_border,
                    ),
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (
                                rect[0][0] + ((interior_size - w) / 2),
                                rect[0][1] + ((interior_size - h) / 2) - 10,
                            ),
                            letters[i][j],
                            fill="black",
                            font=font,
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        # Loop through each variable in the domain
        for var, domain in self.domains.items():
            # Create a set of values to remove from the domain
            remove = {word for word in domain if len(word) != var.length}

            # And remove them
            domain.difference_update(remove)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """

        revised = False

        # Determine the overlap between x and y
        overlap = self.crossword.overlaps[x, y]

        # Create a set for values to be removed from the domain
        word_remove = set()

        # Loop through x and y to check for overlaps
        for word_x in self.domains[x]:
            check_overlaps = False
            for word_y in self.domains[y]:
                if word_x[overlap[0]] == word_y[overlap[1]]:
                    check_overlaps = True
                    break

            # If no overlaps, add word to set
            if not check_overlaps:
                word_remove.add(word_x)
                revised = True

        # Remove word
        self.domains[x] -= word_remove
        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """

        # If `arcs` is None, begin with initial list of all arcs in the problem.
        if arcs is None:
            arcs = [
                (x, y)
                for x in self.crossword.variables
                for y in self.crossword.neighbors(x)
            ]

        while arcs:
            # Get the first arc in the list and remove it
            x, y = arcs.pop(0)

            # Send x, y to be revised
            if self.revise(x, y):
                # If domain is empty, theres no solution
                if len(self.domains[x]) == 0:
                    return False

                # Add arcs from X to neighbors - Y
                for z in self.crossword.neighbors(x) - {y}:
                    arcs.append((z, x))

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """

        # If the set of assignment is equal to set of domains, return true.
        return set(assignment) == set(self.domains)

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """

        # Check for matching length
        for var in assignment:
            if var.length != len(assignment[var]):
                return False

        # Check for uniqueness
        if len(set(assignment.values())) != len(set(assignment.keys())):
            return False

        # Check neighbors for conflicts
        for var, word in assignment.items():
            for neighbor in self.crossword.neighbors(var):
                # Check overlap between the current var and neighbor
                overlap = self.crossword.overlaps[var, neighbor]
                if neighbor in assignment:
                    if assignment[neighbor][overlap[1]] != word[overlap[0]]:
                        return False

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """

        # Setting up some variables
        values = {}
        variables = self.domains[var]
        neighbors = self.crossword.neighbors(var)

        # Looping through var domain
        for variable in variables:
            if variable in assignment:
                continue
            else:
                count = 0
                # Looping through neighbors
                for neighbor in neighbors:
                    if variable in self.domains[neighbor]:
                        count = count + 1
                # Adding the count to the variable
                values[variable] = count

        # Return sorted variables by key
        return sorted(values, key=lambda key: values[key])

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        var = [v for v in self.crossword.variables if v not in assignment]
        if len(var) == 1:
            return var[0]

        # Sort variables by  remaining values
        var = sorted(var, key=lambda var: len(self.domains[var]))

        # Check for a variable with the minimum number of values
        if len(self.domains[var[0]]) < len(self.domains[var[1]]):
            return var[0]

        # Sort variables by degree
        var = sorted(
            var, key=lambda var: len(self.crossword.neighbors(var)), reverse=True
        )

        return var[0]

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """

        # Check first if assigment is complete
        if self.assignment_complete(assignment):
            return assignment

        # Get unassigned variable
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            assignment[var] = value

            # Checking consistency
            if self.consistent(assignment):
                result = self.backtrack(assignment)
                if result:
                    return result

            # If not consistent, delete variable.
            del assignment[var]

        return None


def main():
    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
