import sys
from src.accommodation import modul


def main():
    n = 0

    try:
        n = int(sys.argv[1])
    except IndexError:
        print("Hiányzó parancssori argumentum")
    except ValueError:
        print("Nem megfelelő parancssori argumentum")

    accommodations = []
    for i in range(n):
        line = input()
        tokens = line.split(";")
        if len(tokens) == 3:
            accm = modul.Accommodation(tokens[0], int(tokens[2]), tokens[1])
            accommodations.append(accm)
        elif len(tokens) == 4:
            hotel = modul.Hotel(tokens[0], int(tokens[2]), tokens[1], int(tokens[3]))
            accommodations.append(hotel)
        else:
            print("Nem megfelelő bemenet!")

    accommodations.sort()

    for szallas in accommodations:
        print(szallas)

if __name__ == "__main__":
    main()