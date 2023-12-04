import math

def lnko(a,b):
    while b:
        a,b = b, a%b
    return a
def main():
    line = input()
    t = line.split(" ")
    elso_szam = int(t[0])
    masodik_szam = int(t[1])
    if lnko(elso_szam, masodik_szam) == 1:
        print("IGEN")
    else:
        print("NEM")

if __name__ == "__main__":
    main()