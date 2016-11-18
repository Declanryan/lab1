# count poker hands

# 1. open the poker data file for reading
file_str = input("Enter a file name: ")

while True: # loop until you break
    try:
        poker_file = open(file_str, 'r')
        break # success! so move on to rest of program
    except IOError:
        print("Error opening file:", file_str)
        file_str = input("Enter a file name: ")

total_count_int = 0 # 2. create and initialize variable to hold the totalcount
pair_count_int = 0 # create and initialize variable to hold pair count

# 3. Loop through each l ine of the file
for line_str in poker_file:
    total_count_int = total_count_int + 1 # (a). add one total for each hand
    fields = line_str.split(',') # (b) .split on a comma
    hand_rank_str = fields[-1] # and ge t the last field
    try:
        hand_rank_int = int(hand_rank_str)
    except ValueError:
        continue # bad line : quietly skip this line of the file
    if hand_rank_int == 1: #( c ) if handRank is 1 ( it is a pair )
        pair_count_int = pair_count_int + 1 # add one to pair count
        
print("Total hands in file: ", total_count_int) # 4. print the values
print("Count of pair hands: ", pair_count_int)
print("Probability of a pair: {:>9.4%}".format(pair_count_int/total_count_int))