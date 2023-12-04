def count_of_local_minimums(numbers):
    db = 0
    for i in range(1,len(numbers)-1):
        if numbers[i] < numbers[i-1] and numbers[i] < numbers[i+1]:
            db += 1
    return db

import  sys
def main():
    for line in sys.stdin:
        numbers_str = line.split()
        numbers = []
        for x in numbers_str:
            numbers.append(int(x))
            print(count_of_local_minimums(numbers))


if __name__ == "__main__":
    main()