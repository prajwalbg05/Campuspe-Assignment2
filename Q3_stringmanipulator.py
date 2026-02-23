# Question 3: String Manipulator

# Taking input from user
str = input("Enter a sentence: ")
# Original sentence
print("\nOriginal:", str)
# Total characters (with spaces)
print("Characters (with spaces):", len(str))
# Total characters (without spaces)
no_space = str.replace(" ", "")
print("Characters (without spaces):", len(no_space))
# Total words
words = str.split()
print("Total words:", len(words))
# Uppercase
print("UPPERCASE:", str.upper())
# Lowercase
print("lowercase:", str.lower())
# Title Case
print("Title Case:", str.title())

# First word
if len(words) > 0:
    print("First word:", words[0])
else:
    print("First word: No words entered")

# Last word
if len(words) > 0:
    print("Last word:", words[-1])
else:
    print("Last word: No words entered")

# Reversed sentence
print("Reversed:", str[::-1])

