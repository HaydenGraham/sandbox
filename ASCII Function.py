LOWER = "33"
UPPER = "127"
letter_to_number = str(input("Enter a character: "))
print("The ASCII code for {} is {}".format(letter_to_number, ord(letter_to_number)))

number_to_letter = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while number_to_letter > UPPER or number_to_letter < LOWER:
    print("error")
    number_to_letter = int(input("Enter a valid number BETWEEN {} AND 127: ".format(LOWER, UPPER)))
else:
    print("The ASCII letter for {} is {}".format(number_to_letter, chr(number_to_letter)))
    for i in range(LOWER, UPPER):
        print("{:5}    {}".format(i, chr(i)))