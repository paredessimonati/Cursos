from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# General knowledge base
KB = And(
    # each character is either a knight or a knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight,AKnave)),
    # each character is either a knight or a knave, but not both
    Or(BKnight, BKnave),
    Not(And(BKnight,BKnave)),
    # each character is either a knight or a knave, but not both
    Or(CKnight, CKnave),
    Not(And(CKnight,CKnave)),
    
    
)


# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    KB,
    # Knight implying he's a knight and a knave
    Implication(AKnight, And(AKnight, AKnave)),
    # Knave implying he's not a knight and a knave
    Implication(AKnave, Not(And(AKnight, AKnave))),
    
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    KB,
    # Knight implying A and B are knaves
    Implication(AKnight, And(AKnave, BKnave)),
    # Knave implying A and B not are knaves
    Implication(AKnave, Not(And(AKnave, BKnave))),

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    KB,
    # Implying for all scenarios
    Implication(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    Implication(AKnave, Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),
    Implication(BKnight, Or(And(BKnight, AKnave), And(BKnave, AKnight))),
    Implication(BKnave, Not(Or(And(BKnight, AKnave), And(BKnave, AKnight)))),
    
    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    KB,
    # implying necessary
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    
    # B says A said he (A) was a knave, or not a knave
    Implication(BKnight, Implication(AKnight, AKnave)),
    Implication(BKnave, Implication(AKnave, Not(AKnave))),
    
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight)),
    
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
