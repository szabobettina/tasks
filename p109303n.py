from typing import NamedTuple

Airport = NamedTuple("Airport", [("name", str), ("city", str), ("runways", int), ("time", int)])

def line_to_airport(line:str) -> Airport:
    line = line.split(";")
    return Airport(line[0], line[1], int(line[2]), int(line[3]))


def airport_to_line(airport:Airport) -> str:
    return f"{airport.name} ({airport.city}): {airport.time}"


def group_by_runways(airports:list[Airport]) -> dict[int, list[Airport]]:
    res = dict()
    for x in airports:
        if x.runways not in res:
            res[x.runways] = [x]
        else:
            res[x.runways].append(x)

    return res


def main():
    airports = []
    n = int(input())
    for i in range(n):
        line = input()
        airports.append(line_to_airport(line))

    r_d = group_by_runways(airports)

    for k in r_d:
        print(k)
        for i in r_d[k]:
            print(airport_to_line(i))


if __name__ == "__main__":
    main()