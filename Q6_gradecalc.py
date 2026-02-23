# Question 5: Grade Calculator
from numpy import array


def grade_calculator(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"
sub = ["Math", "Science", "English", "History", "Art"]
array = []
print("Enter marks for 5 subjects (out of 100):")
print("--------------------------------------")
for i in range(5):
    print("Subject ", i, ":", sub[i])
for i in range(5):
    array.append(int(input("Enter marks for subject " + sub[i] + ": ")))
    print("Marks for subject ",sub[i],":",array[i])


total_marks = sum(array)
print("\nTotal Marks:", total_marks)

percentage = (total_marks / 500) * 100
print("Percentage:", percentage)

print("Grade:", grade_calculator(total_marks))

for i in range(5):
    if array[i] >= 40:
        continue
    else:
        print("You have failed in subject " + sub[i])
        break
else:
    print("Congratulations! You have passed all subjects.")

#