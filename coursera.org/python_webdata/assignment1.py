import re
hand = open('regex_sum_188676.txt')

#numlist = list()
#for line in hand:
#    line = line.rstrip()
#    stuff = re.findall('[0-9]+', line)
#    if not stuff: continue
#    numlist += [int(x) for x in stuff]
#
#print 'Sum: ', sum(numlist)

print sum([ int(x) for x in re.findall('[0-9]+', hand.read().rstrip()) ])
