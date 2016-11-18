"""A day has 86400secs(24*60*60). given a number in the range 1 to 86400
 output the current time as hours,minutes and seconds with a 24 hour clock."""

#input the number of secs
no_entered = int(input("please enter the number of secs"))
# convert the secs into hours,min
no_of_hours = int( no_entered / 60/60)
no_of_min = int((no_entered-(no_of_hours *60*60))/60)
no_of_secs = int(no_entered-((no_of_hours *60*60)+(no_of_min*60)))

#output the answer
print(no_of_hours,"hours",no_of_min,"min",no_of_secs,"seconds")