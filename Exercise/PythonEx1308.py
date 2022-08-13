import random


def main():
    #starTriangle(3)
    #print(intsIn("10 and 3 are like alot of 200"))
    #fizzBuzz()
    #print(addNumbers([5,6,10], [5,8,19], [10, 12, 3, 18]))
    #monkeyAuthor()
    mastermind()


def starTriangle(n):
    res = "*"
    for _ in range(n):
        print(res)
        res = f"*{res}*" 


def intsIn(i):
    l = i.split(" ")
    res = int()

    for _ in l:
        if _.isnumeric():
            res = res + int(_)

    if res > 0:
        return res
    else:
        return "NO int above 0"


def fizzBuzz():
    try:
        x = int(input("Eine Nummer?"))
        for _ in range(1, x):

            if _ % 4 == 0 and _%6 != 0:
                print("Fizz!")
            elif _%6 == 0 and _%4 !=0:
                print("Buzz")
            elif _% 6 == 0 and _% 4 ==0:
                print("Fizz Buzz !!")
            else:
                print(_)
    except ValueError:
        return print("Eine >>>> NUMMER <<<<!"),fizzBuzz()


def addNumbers(a,b,c):
    for i in a:
        for j in b:
            if (i + j) in c:
                return True
            else:
                return False

def monkeyAuthor():
    sentence1 = (input("Input sentence: ")).split(" ")
    sentence2 = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphadict = {}
    for count, value in enumerate(alphabet):
        alphadict[count] = value

    for i in sentence1:
        word = str()
        for j in i:
            letter = alphadict[random.randrange(1,26)]
            word = word + letter
 
        sentence2.append(word)
    if sentence1 == (" ".join(sentence2)):
        print("ITS THE SAME")

    else:
        print(" ".join(sentence2))


def mastermind():
    num = random.randrange(999, 9999)
    counter = 10
    while counter > 0:
        output = []
        counter-=1
        try:
            numIn = int(input("Four digit number!"))
        except ValueError:
            print("A >>>>>>>>NUMBER<<<<<<<<<")
            continue
        if len(str(numIn)) != 4:
            print("Four digits.....four")
            continue

        else:
            numInL = list(str(numIn))
            numL = list(str(num))

            for x in numInL:
                if x in numL:
                    if numL.index(x) == numInL.index(x):
                        output.append("R")
                    else:
                        output.append("Y")

                else:
                    output.append("B")
        if numIn == num:
            print(f"you done did it, and it took {10-counter} tries!")
            break
        else:
            print(f'Result: {"".join(output)} yout have {counter} left')
            


if __name__ == "__main__":
    main()