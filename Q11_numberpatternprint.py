# Question 11: Number Pattern Printer

print("Choose a Pattern:")
print("1. Increasing Numbers")
print("2. Repeating Numbers")
print("3. Reverse Decreasing")
print("4. Pyramid Pattern")
print("5. Reverse Pyramid")
print("6. Continuous Numbers")
print("7. Repeating Rows")


choice = int(input("Enter pattern number (1-7(bonus-3)): "))
height = int(input("Enter height: "))

print()

# Pattern 1
if choice == 1:
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Pattern 2
elif choice == 2:
    for i in range(1, height + 1):
        for j in range(i):
            print(i, end=" ")
        print()
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# Pattern 3
elif choice == 3:
    for i in range(height, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# Pattern 4
elif choice == 4:
   for i in range(1, height + 1):
    # Spaces
    for j in range(height - i):
        print(" ", end="")
    # Numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

elif choice == 5:
    for i in range(height, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
        #pattern 1 2 3 4 5
               # 1 2 3 4
               # 1 2 3
               # 1 2
               # 1
elif choice == 6:
    num = 1
    for i in range(1, height + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

elif choice == 7:
    for i in range(1, height + 1):
        for j in range(height):
            print(i, end=" ")
        print()
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

else:
    print("Invalid pattern choice.")