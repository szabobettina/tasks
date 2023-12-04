import math


def main():
    n = int(input())
    if n > 0:
        maxi = - math.inf
        for i in range(n):
            k = int(input())
            if k > maxi:
                maxi = k
        print(maxi)
    else:
        print("Helytelen paraméter!")

if __name__ == "__main__":
    main()