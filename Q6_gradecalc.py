# Question 5: Grade Calculator


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

print("Enter marks for 5 subjects (out of 100):")
print("--------------------------------------")


math = int(input("Enter marks for Math: "))
science = int(input("Enter marks for Science: "))
english = int(input("Enter marks for English: "))
history = int(input("Enter marks for History: "))
art = int(input("Enter marks for Art: "))

# Total
total = math + science + english + history + art
print("\nTotal Marks:", total, "/ 500")

# Percentage
percentage = (total / 500) * 100
print("Percentage:", round(percentage, 2), "%")

# Grade
print("Grade:", grade_calculator(percentage))

# Pass/Fail (all subjects must be >= 40)
failed = False

if math < 40:
    print("Failed in Math")
    failed = True

if science < 40:
    print("Failed in Science")
    failed = True

if english < 40:
    print("Failed in English")
    failed = True

if history < 40:
    print("Failed in History")
    failed = True

if art < 40:
    print("Failed in Art")
    failed = True

if failed == False:
    print("Result: Pass")
else:
    print("Result: Fail")