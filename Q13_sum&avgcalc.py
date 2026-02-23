# Question 13: Sum and Average Calculator (Alternative Logic)

count = int(input("How many numbers? "))

total = 0

for i in range(1, count + 1):
    num = float(input("Enter number : "))
    
    total = total + num

    # Initialize max and min during first iteration
    if i == 1:
        maximum = num
        minimum = num
    else:
        if num > maximum:
            maximum = num
        
        if num < minimum:
            minimum = num

# Calculate average
average = total / count

print("\nResults:")
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)