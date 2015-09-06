# https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=10

```
The pairs of numbers only merge if each number is the same. The first example you cited is in fact correct. But [24, 24, 0, 0] for the last example is wrong.

Given [2, 2, 2, 2, 2]:

1. Start with an empty merged list of length 5: [0, 0, 0, 0, 0]
2.  The first two numbers from the left are both '2', so add them together and put the result in the merged list: [4, 0, 0, 0, 0].
3. The next two numbers from the left are also both '2', so add them together and put the result in the merged list: [4, 4, 0, 0, 0]
4. The last number is a '2'. There are no more pairs, so just put it in the list: [4, 4, 2, 0, 0]
5. You are done.

Given [8, 16, 16, 8]:

1. Start with an empty merged list of length 4: [0, 0, 0, 0]
2. The 8 and 16 are not the same, so copy the 8 to the merged list: [8, 0, 0, 0]
3. The 16 and 16 are the same, so add them together and put the result in the lest: [8, 32, 0, 0]
4. There are no more pairs, the last number is 8, so just put it in the list: [8, 32, 8, 0]
5. You are done.
```
