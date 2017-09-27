import random as r

# File I/O
f = open('occupations.csv','r')
csv = f.read()
f.close()

# Fills the dictionary with the info from the csv
data = {}
L = csv.split('\r\n')
for lines in L[1:]:
    stuff = lines.split(',')
    data[','.join(stuff[:-1])] = float(stuff[-1])

# Gets a random element from a dictionary assuming values
#    are floats that represent probability
def getRandWeighted(data):
    # Picks a random number and subtracts probability from it
    #    until 0 is reached, signifying a pick
    tot = r.random() * data['Total']
    for each in data:
        if each == 'Total':
            continue
        tot -= data[each]
        if tot <= 0:
            return each

print "Press ENTER to get a random Job"

# For ease of use
while True:
    raw_input()
    print getRandWeighted(data)

