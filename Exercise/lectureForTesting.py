
def main():
    print(isPrime(int(input("number"))))


def isPrime(i):
    for _ in range(2,i):
        if i%_ == 0 and i!=_:
            return False

    return True



if __name__ == "__main__":
    main()