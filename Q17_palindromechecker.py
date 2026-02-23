# Question 17: Palindrome Checker

value = input("Enter word or number: ")

original = value
reversed_value = value[::-1]   # Reverse using slicing

print("Original:", original)
print("Reversed:", reversed_value)

if original.lower() == reversed_value.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")