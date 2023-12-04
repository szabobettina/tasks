def delete_odd_digits(str):
    s = ""
    for i in range(len(str)):
        if  not str[i].isdigit():
            s+=str[i]
        else:
            if int(str[i]) % 2 == 0:
                s+=str[i]
    return s

#from src import prog_test

def main():
    n = input()
    for i in range(int(n)):
        original = input()
        print(delete_odd_digits(original))

if __name__ == "__main__":
    main()