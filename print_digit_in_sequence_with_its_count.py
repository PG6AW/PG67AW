#Code to print each digit of the given number in sequence with digit's count and each digit within the next separate line : (Also prints the first Zero(s))


a = input("Please input any number here to get each digit in sequence with its count: ")
for i in a:
    b = []
    print(f"{int(i)}: ",end = (""))
    if int(i) > 0 :
        for j in range(int(i)):
            b.append(i)
    elif int(i) == 0 :
        print()
    output = "".join(b)
    if int(i) > 0 :
        print(int(output))

        #And the output is always int ! Good luck.
