# Question 4: Age Calculator

# Taking birth year input
birthyear = int(input("Enter your birth year: "))

# current year
current_year = 2026

# Calculating age
age = current_year - birthyear

# Checking valid age
if age >= 0:
    print("\nYour Age Details:")
    print("Current Age:", age, "years")

    # Age in months
    months = age * 12
    print("Age in Months:", months)

    # Age in days (approx)
    days = age * 365
    print("Age in Days:", days)

    # Age in hours
    hours = days * 24
    print("Age in Hours:", hours)

    # Age in minutes
    minutes = hours * 60
    print("Age in Minutes:", minutes)

    # Years until 100
    years_left = 100 - age

    if years_left > 0:
        print("Years until 100:", years_left)
    else:
        print("You are already 100 or above!")

else:
    print("Invalid birth year entered.")