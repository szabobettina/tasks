def pythagorean (a,b):
    return (a*a+b*b)**0.5


def main():
    while True:
        line = input()
        if line == "0":
            return
        sz = line.split(" ")
        print(pythagorean(float(sz[0]),float(sz[1])))

if __name__ == "__main__":
    main()