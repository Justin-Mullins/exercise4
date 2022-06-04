'''

Exercise 4

For this exercise, you need to write a function ( hex_output ) that takes a hex num-
ber and returns the decimal equivalent. That is, if the user enters 50 , you’ll assume
that it’s a hex number (equal to 0x50 ) and will print the value 80 to the screen. And
no, you shouldn’t convert the number all at once using the int function, although it’s
permissible to use int one digit at a time.

'''
# Function convers hex to decimal
def hex_output(number):
    hex_string = str(number).lower()[::-1]
    hex = 0
    exponent = 0
    for x in hex_string:
        if x.isnumeric():
            hex += int(x) * 16**exponent
        else:
            if (x == 'a'):
                hex += 10 * 16**exponent
            elif (x == 'b'):
                hex += 11 * 16**exponent
            elif (x == 'c'):
                hex += 12 * 16**exponent
            elif (x == 'd'):
                hex += 13 * 16**exponent
            elif (x == 'e'):
                hex += 14 * 16**exponent
            elif (x == 'f'):
                hex += 15 * 16**exponent
        exponent += 1
    return hex

print(hex_output(50))
print(hex_output('a23e'))
print(hex_output('4c'))