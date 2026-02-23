# Question 11: Number Pattern Printer

print("Choose a Pattern:")
print("1. Increasing Numbers")
print("2. Repeating Numbers")
print("3. Reverse Decreasing")
print("4. Pyramid Pattern")

choice = int(input("Enter pattern number (1-4): "))
height = int(input("Enter height: "))

print()

# Pattern 1
if choice == 1:
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Pattern 2
elif choice == 2:
    for i in range(1, height + 1):
        for j in range(i):
            print(i, end=" ")
        print()

# Pattern 3
elif choice == 3:
    for i in range(height, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# Pattern 4
elif choice == 4:
    for i in range(1, height + 1):
        # Increasing part
        for j in range(1, i + 1):
            print(j, end="")
        # Decreasing part
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

else:
    print("Invalid pattern choice.")