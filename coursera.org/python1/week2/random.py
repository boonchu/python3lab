#love pop song generator
import random
def verse_a():
    a = random.randrange(1,5)
    if a == 1:
        print "In this lonely afternoon"
    elif a == 2:
        print "In this sunny Sunday morning"
    elif a == 3:
        print "In this dark and cold winter"
    elif a == 4:
        print "Under this magic summernight sky"

def verse_b():
    a = random.randrange(1,5)
    if a == 1:
        print "I walk alone, trying to forget you,"
    elif a == 2:
        print "I try not to see your name anywhere,"
    elif a == 3:
        print "I can't do anything but thinking of you,"
    elif a == 4:
        print "I'm writing a love letter to you,"

def verse_c():
    a = random.randrange(1,5)
    if a == 1:
        print "Even if the rain will fall"
    elif a == 2:
        print "Even if you don't share my passion for Lord Fener"
    elif a == 3:
        print "Even if I've loved your sister more than you"
    elif a == 4:
        print "Even if your dad tries to kill me everyday"

def verse_d():
    a = random.randrange(1,5)
    if a == 1:
        print "One day we'll run away together"
    elif a == 2:
        print "One day we'll share a common dream"
    elif a == 3:
        print "I'll do anithing for you"
    elif a == 4:
        print "I'll fix your broken windshield wiper"

    
def feat_pitbull(pitbull):
    if pitbull:
        print "TUNZ TUNZ TUNZ TUNZ (Pitbull)"
        print " "
  
def stanza():
    verse_a()
    verse_b()
    verse_c()
    verse_d()
    print "Because I love you, babe"
    print "Because I love you, babe"
    print " "

Pitbull = random.randrange(0,2)
stanza()
stanza()
feat_pitbull(Pitbull)
stanza()
print "(Sweet music, time slows down)"
print " "
print "Because I love you, babe"
print "Because I love you, babe"

