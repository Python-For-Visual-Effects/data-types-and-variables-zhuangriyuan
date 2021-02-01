"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64 + 32)

# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
num1 = 64
num2 = 32
sum = num1 + num2
print(sum)

# 3.- Make a program that prints a sentence that includes at least 3 variables.
word1 = "program"
word2 = "sentence"
word3 = "variables"
print("Make a " + word1 + " that prints a " + word2 + " that includes at least 3 " + word3)

# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."
sentence = "This is my first Python program."
print(len(sentence))

# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"
value1 = 1920 * 0.1
value2 = 1080 * 0.1
print("The 10% overscan of 1920 is " + str(int(value1)) + ", and the 1080 is " + str(int(value2)))
