# Taking inputs
age = int(input("Enter your age: "))
day = input("Enter the day of the week: ").lower()
ticket_count = int(input("Enter the number of tickets: "))

def ticketprice(age, day):

    # Weekday pricing
    if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
        
        if age < 3:
            return 0
        elif age >= 3 and age <= 12:
            return 150
        elif age >= 13 and age <= 59:
            return 300
        else:
            return 200

    # Weekend pricing (20% discount applied directly)
    elif day == "saturday" or day == "sunday":
        
        if age < 3:
            return 0
        elif age >= 3 and age <= 12:
            return 120      # 150 - 20%
        elif age >= 13 and age <= 59:
            return 240      # 300 - 20%
        else:
            return 160      # 200 - 20%

    else:
        return 0   # Invalid day


# Calculating total
price_per_ticket = ticketprice(age, day)
ticketamount = price_per_ticket * ticket_count

print("Ticket price for one ticket: ₹", price_per_ticket)
print("Total Ticket Price for", ticket_count, "tickets: ₹", ticketamount)

if day == "saturday" or day == "sunday":
    print("It's a weekend! You get a 20% discount.")
else:
    print("It's a weekday. No discount.")