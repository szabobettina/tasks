def double_even_digits(str):
    s = ""
    for i in range(len(str)):
        if str[i].isdigit() and int(str[i]) % 2 == 0:
            s += str[i]
            s += str[i]
        else:
            s += str[i]
    return s

#from src import prog_test

def main():
    while True:
        original = input()
        if original == "END":
            break
        print(double_even_digits(original))

if __name__ == "__main__":
    main()