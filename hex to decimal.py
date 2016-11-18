# this program changes decimal numbers into hexadecimal and back
#initalize the functions

#this function is to turn a decimal number into a hexadecimalstring
def converter_too (n):
    '''

    :param n:
    :return:
    '''
    n1 = int(n // 16)
    r1 = int(n % 16)
    if (r1 < 10):
        return(r1),
    if (r1 == 10):
        print("A"),
    if (r1 == 11):
        print("B"),
    if (r1 == 12):
        print("C"),
    if (r1 == 13):
        print("D"),
    if (r1 == 14):
        print("E"),
    if (r1 == 15):
        print("F"),

    n2 = int(n1 // 16)
    r2 = int(n1 % 16)
    n3 = int(n2 // 16)
    r3 = int(n2 % 16)
    n4 = int(n3 // 16)
    r4 = int(n3 % 16)
    n5 = int(n4 // 16)
    r5 = int(n4 % 16)
    n6 = int(n5 // 16)
    r6 = int(n5 % 16)
    n7 = int(n6 // 16)
    r7 = int(n6 % 16)
    n8 = int(n7 // 16)
    r8 = int(n7 % 16)
    return("{0}{1}{2}{3}{4}{5}{6}{7}.".format(r8, r7, r6, r5, r4, r3, r2, r1))

#this function is to turn a hexadecimal string into a decimal number
def converter_back(bin):
    sum=0
    sum = sum + ((base_output ** 0) * int(bin[7]))
    sum = sum + ((base_output ** 1) * int(bin[6]))
    sum = sum + ((base_output ** 2) * int(bin[5]))
    sum = sum + ((base_output ** 3) * int(bin[4]))
    sum = sum + ((base_output ** 4) * int(bin[3]))
    sum = sum + ((base_output ** 5) * int(bin[2]))
    sum = sum + ((base_output ** 6) * int(bin[1]))
    sum = sum + ((base_output ** 7) * int(bin[0]))
    return (sum)








#take input from the user, for the decimal value
print (" Converter")
print ("")
convert_too = int(input("please enter a base to convert to"))
base_output = int(input("please enter a basethe to output to"))
number = int (input ("Please enter a number to change: "))

#make sure input is within the 8 bit range
while number <0 or number >4294967295:
        print ("ERROR. Only a number between 0 and 4294967295. Try Again.")
        number = int (input ("Please enter a number between 0 and 4294967295 to change it into a binary : "))

#call and print the function to convert the decimal to binary
#bin = converter_too(number)

#print("The  number you requested:",bin)
#call the function to convert the binary number to decimal
dec = converter_back(bin)
print("The number IS: ",dec)
