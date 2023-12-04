import sys
from typing import NamedTuple

LegoSet = NamedTuple("LegoSet", [("number", int),("name", str),("theme", str),("pieces", int)])

def line_to_lego_set(line):
    tokens = line.split(";")
    return LegoSet(int(tokens[0]),tokens[1],tokens[2], int(tokens[3]))

def lego_set_to_line(lego_set):
    line = lego_set.name
    line += " ("
    line += str(lego_set.number)
    line += "): "
    line += str(lego_set.pieces)
    line += " - "
    line += lego_set.theme
    return line

def sort_lego_sets(lego_sets):
    return sorted(lego_sets, key = lambda x : (-x[3],x[2],x[1],x[0]))

def main():
    lego_sets = []

    for line in sys.stdin:
        lego_sets.append(line_to_lego_set(line))

    lego_sets = sort_lego_sets(lego_sets)

    for i in range(len(lego_sets)):
        print(lego_set_to_line(lego_sets[i]))

#from src import prog_test_v2

if __name__ == "__main__":
    #prog_test_v2.test()
    main()
