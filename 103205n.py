def n_sum(n):
    sum = 0
    for i in range(n):
        sum += i + 1
    return sum

def main():
    k = int(input())
    for i in range(k):
        n = int(input())
        print(n_sum(n))

if __name__ == "__main__":
    main()