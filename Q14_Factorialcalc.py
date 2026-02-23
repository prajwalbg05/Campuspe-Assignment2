# Question 14: Factorial Calculator (Using while loop)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")

elif num == 0:
    print("0! = 1")

else:
    factorial = 1
    i = num
    expression = ""

    while i >= 1:
        factorial = factorial * i

        if i == 1:
            expression = expression + str(i)
        else:
            expression = expression + str(i) + " × "

        i = i - 1

    print(str(num) + "! =", expression, "=", factorial)