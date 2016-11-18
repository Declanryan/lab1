"""problem 2-how many gallons of water fall on an acre of land given the number of
inches of rain that fell"""
# 1 acre = 43560 square feet
# 1 cubic foot = 7.48051975 gallons
#volume = depth * area

#ask user for input
my_inches = float(input("please enter the number of inches"))
#put input into formula for volume and convert to gallons
my_volume = (my_inches/12) *43560
my_volume_gallons = my_volume * 7.48051975
#output the answer
print("the total volume of water in gallons is {:.2f}".format(my_volume_gallons))