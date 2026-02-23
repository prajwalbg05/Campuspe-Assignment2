#Prime checker
#part1
num = int(input("Enter a number: "))
if num < 2:
    print(num, "is not a prime number.")
else:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
#part2
#print all prime numbers between range
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")
