# this program changes decimal numbers into binary and back
#initalize the functions

#this function is to turn a decimal number into a binary string
def converter_dec_bin (n1):
    n1 = int(dec_num // 2)
    r1 = int(dec_num % 2)
    n2 = int(n1 // 2)
    r2 = int(n1 % 2)
    n3 = int(n2 // 2)
    r3 = int(n2 % 2)
    n4 = int(n3 // 2)
    r4 = int(n3 % 2)
    n5 = int(n4 // 2)
    r5 = int(n4 % 2)
    n6 = int(n5 // 2)
    r6 = int(n5 % 2)
    n7 = int(n6 // 2)
    r7 = int(n6 % 2)
    n8 = int(n7 // 2)
    r8 = int(n7 % 2)
    return("{0}{1}{2}{3}{4}{5}{6}{7}.".format(r8, r7, r6, r5, r4, r3, r2, r1))

#this function is to turn a binary string into a decimal number
def converter_bin_dec(bin):
    sum=0
    if bin[7]=='1':
        sum = sum +((2**0)*1)
    if bin[6]=='1':
        sum = sum +((2**1)*1)
    if bin[5]=='1':
        sum = sum +((2**2)*1)
    if bin[4]=='1':
        sum = sum +((2**3)*1)
    if bin[3]=='1':
        sum = sum +((2**4)*1)
    if bin[2]=='1':
        sum = sum +((2**5)*1)
    if bin[1]=='1':
        sum = sum +((2**6)*1)
    if bin[0]=='1':
        sum = sum +((2**7)*1)
    return (sum)








#take input from the user, for the decimal value
print ("Denary to Binary Converter")
print ("")
dec_num = int (input ("Please enter a number between 0 and 255 to change it into a binary : "))

#make sure input is within the 8 bit range
while dec_num <0 or dec_num >255:
        print ("ERROR. Only a number between 0 and 255. Try Again.")
        dec_num = int (input ("Please enter a number between 0 and 255 to change it into a binary : "))

#call and print the function to convert the decimal to binary
bin = converter_dec_bin(dec_num)

print("The binary number you requeted:",bin)
#call the function to convert the binary number to decimal
dec = converter_bin_dec(bin)
print("The decimal number IS: ",dec)
