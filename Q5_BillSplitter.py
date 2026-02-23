TotalBill_amount = float(input("Total bill amount: "))
number_of_people = int(input("Number of people sharing the bill: "))
Tax_percentage= float(input("Tax percentage: "))
Tip_percentage = float(input("Tip percentage: "))

tax_amt=TotalBill_amount*(Tax_percentage/100)
tip_amt=TotalBill_amount*(Tip_percentage/100)
total=TotalBill_amount+tax_amt+tip_amt

print("\n====BILL BREAKDOWN====")
print("Subtotal:",TotalBill_amount)
print("Tax (", Tax_percentage, "%):", TotalBill_amount*(Tax_percentage/100))
print("Tip (", Tip_percentage, "%):", TotalBill_amount*(Tip_percentage/100))
print("Total Amount:",total)
print("Amount per person:",total/number_of_people)
print("========================")
