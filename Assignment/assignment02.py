num1 = str(input("Enter the number01:-"))
# num1 = int(num1)
num2 = str(input("Enter the number02:-"))
# num2 = int(num2)
opr = input("Enter the opr:-")
if opr == "+":
    print(int(num1) + int(num2))
elif opr == "-":
    print(num1 - num2)
elif opr == "*":
    print(num1*num2)
else:
    print("invalid operation")