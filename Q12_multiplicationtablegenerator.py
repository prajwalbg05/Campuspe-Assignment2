n=int(input("Enter a number to generate multiplication table:: "))
print("\nMultiplication Table for", n)
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
print()