import random
file = open("Number_Text.txt", "w")
file.write((str(random.randint(0, 999999999999999)) + "\n") + (str(random.randint(0, 999999999999999)) + "\n") + (str(random.randint(0, 999999999999999)) + "\n"))
file.close()
file = open("Number_Text.txt", "r")
number = (((file.read()).lstrip("0").replace(",", "")).replace(" ", ""))
file.close()
bel_20 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
bel_100 = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
opt = ""


def Num_to_text(x):
    n = 1
    answer = ""
    if int(len(str(x))) > 7:
        while n * 7 < len(str(x)):
            n += 1
        n = n - 1
        while n > 0:
            answer = answer + Num_to_text(int(str(x)[(-7 * (n + 1)): (-7 * n)])) + " crore "
            n = n - 1
        answer = answer + Num_to_text(int(str(x)[(-7):]))
        return answer
    if int(len(str(x))) == 6 or int(len(str(x))) == 7:
        if int(len(str(x//100000))) == 1 or int(str(x//100000)[0]) < 2:
            answer = (answer + (bel_20[x // 100000]) + " lakhs") if (x % 100000) == 0 and (bel_20[x // 100000]) != "one" else (answer + (bel_20[x // 100000]) + " lakh ")
        else:
            answer = answer + (bel_100[int(str(x // 100000)[0])] + " " + bel_20[int(str(x // 100000)[1])]) if int(str(x // 100000)[1]) != 0 else answer + bel_100[int(str(x // 100000)[0])]
            answer = (answer + " lakhs") if (x % 100000) == 0 else (answer + " lakh ")
        x = x % 100000
        answer = answer + "and " if int(len((str(x % 100000)).lstrip("0"))) < 2 and (x % 100000) != 0 else answer
        answer = answer
    if int(len(str(x))) == 4 or int(len(str(x))) == 5:
        if int(len(str(x//1000))) == 1 or int(str(x//1000)[0]) < 2:
            answer = (answer + (bel_20[x//1000]) + " thousand ") if int(len((str(x % 1000)).lstrip("0"))) > 2 or (x % 1000) == 0 else (answer + (bel_20[x//1000]) + " thousand and ")
        else:
            answer = (answer + bel_100[int(str(x//1000)[0])] + " " + bel_20[int(str(x//1000)[1])]) if int(str(x//1000)[1]) != 0 else answer + (bel_100[int(str(x//1000)[0])])
            answer = (answer + " thousand ") if int(len((str(x % 1000)).lstrip("0"))) > 2 or (x % 1000) == 0 else (answer + " thousand and ")
        x = x % 1000
    if int(len(str(x))) == 3:
        answer = answer + (bel_20[int(str(x)[0])] + " hundred") if int(str(x)[1] + str(x)[2]) == 0 else answer + (bel_20[int(str(x)[0])] + " hundred and ")
        x = x % 100
    if (int(len(str(x))) == 1 and x != 0) or (int(str(x)[0]) < 2 and x != 0):
        answer = answer + bel_20[x]
    elif x != 0:
        answer = answer + (bel_100[int(str(x)[0])] + " " + bel_20[int(str(x)[1])]) if int(str(x)[1]) != 0 else answer + (bel_100[int(str(x)[0])])
    return answer.strip()


def convert():
    global opt
    global file
    global number
    file = open("Number_Text.txt", "w")
    file.write("")
    file.close()
    for i in range(0, (len(numbers))):
        number = int(numbers[i])
        print(number)
        if int(len(str(number))) > 14:
            opt = input(
                "The number is very large and the naming may arise controversies, do you want to continue(y/n)\n")
        if opt == "" or opt == "y":
            print(Num_to_text(number))
            file = open("Number_Text.txt", "a")
            file.write(numbers[i] + " is " + Num_to_text(number) + "\n" + "\n")
            file.close()


numbers = number.splitlines()
if len(numbers) > 1:
    y = 0
    for x in numbers:
        if not x.isdigit():
            print("One of the input numbers are not numeric, please rewrite with only numbers")
            y = 1
            break
    if y== 0:
        convert()
elif number == "":
    print(0)
    print("zero")
elif not number.isdigit():
    print(number)
    print("The input number is not numeric, please rewrite with only numbers")
else:
    convert()
