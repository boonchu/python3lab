import random

NTRIALS = 2000

count2 = 0
count4 = 0

for dummy_x in range(NTRIALS):
    new_tile = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
    if new_tile == 2:
        count2 += 1
    else:
        count4 += 1

pct2 = 100 * count2 / NTRIALS
pct4 = 100 * count4 / NTRIALS

print "Percent of 2's:", pct2
print "Percent of 4's:", pct4
