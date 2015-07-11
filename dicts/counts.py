#! /usr/bin/env python 

line = "the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car"
words = line.split()
print 'Words:', words

print 'Counting...'
counts = dict()
# using dict.get() function to fill in zero value if not available.
for word in words:
	counts[word] = counts.get(word, 0) + 1

print 'Counts', counts

max_count = None
max_word  = None

# using dict.items() function to return with (key, value) from dictionary
for word, count in counts.items():
	if max_count is None or count > max_count:
		#print 'count and word (%s, %s)' % (count, word)
		max_count = count
		max_word  = word

print max_word, max_count
