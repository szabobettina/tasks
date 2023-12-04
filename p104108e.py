def is_twisting(numbers):
    for i in range(len(numbers)-1):
        if numbers[i]*numbers[i+1]>=0:
            return False
    return True

#from src import prog_test

def main():
    while True:
        line = input()
        if line == "":
            return
        numbers_str = line.split()
        numbers=[]
        for x in numbers_str:
            numbers.append(int(x))
        print(is_twisting(is_twisting(numbers)))


if __name__ == "__main__":
    main()