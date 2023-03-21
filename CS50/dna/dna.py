import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Syntax: python dna.py database sequence")

    # Read database file into a variable
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        database = []
        for row in reader:
            database.append(row)

    # Read txt to variable
    with open(sys.argv[2], "r") as file:
        sequence = file.read()

    # using longest_match
    result = []
    for i in range(1, len(database[0])):
        x = longest_match(sequence, database[0][i])
        result.append(x)

    for i in range(1, len(database)):
        # found about all on stackoverflow, spent quite a while trying to understand how it works and this seems to work fine
        # im checking if the result from longest_match are equal to the ints in the database (2nd row and below)
        if all(int(result[j]) == int(database[i][j+1]) for j in range(len(result))):
            print(database[i][0])
            return 0
    else:
        print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
