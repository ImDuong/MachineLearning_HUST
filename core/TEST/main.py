

from processEmail import processEmail

file = open('data/spamSample2.txt', mode='r')

# read all lines at once
all_of_it = file.read()
processEmail(all_of_it)

