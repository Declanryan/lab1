
try:
    abc_file =open("predtest.txt",'r')
except IOError as e:
    print(e)
    quit()

def count_lines(file):
    '''
    count the lines in file inputed
    :param file:
    :return: the tolal lines in the file
    '''
    count = 0
    for line in file:
        count += 1
    return count

def print_lines(file):
    '''
    counts each line and prints the line and count at the same time
    :param file:
    :return:
    '''
    count = 0
    for line in file:
        print(count)
        print(type(line))
        print(line)
        count += 1


count = abc_file.co('Bachelors')



def count_word(search_str,file_entered):
    count=0
    for line in file_entered:
        count += line.count(search_str)
    return count
