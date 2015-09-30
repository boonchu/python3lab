The procedure for scoring a final hand is as follows:

* Go through each dice number you have in your hand and add up the score of the dice with that number
* Take the maximum of these numbers
* So for (2,2,6,6) you could have 4 (for two 2s) or 12 (for two 6s).  Since 12 is the maximum of these
two numbers, this hand scores 12.

To compute the expected value when you are holding some dice and throw the others, you consider the
possible values of the dice you throw and score each of the completed hands.  If you hold (2,2) are
throw two more 6-sided dice, you could end up with the following hands with the following scores:

(2, 2, 1, 1) score 4
(2, 2, 1, 2) score 6
(2, 2, 1, 3) score 4
(2, 2, 1, 4) score 4
(2, 2, 1, 5) score 5
(2, 2, 1, 6) score 6
(2, 2, 2, 1) score 6
(2, 2, 2, 2) score 8
(2, 2, 2, 3) score 6
(2, 2, 2, 4) score 6
(2, 2, 2, 5) score 6
(2, 2, 2, 6) score 6
(2, 2, 3, 1) score 4
(2, 2, 3, 2) score 6
(2, 2, 3, 3) score 6
(2, 2, 3, 4) score 4
(2, 2, 3, 5) score 5
(2, 2, 3, 6) score 6
(2, 2, 4, 1) score 4
(2, 2, 4, 2) score 6
(2, 2, 4, 3) score 4
(2, 2, 4, 4) score 8
(2, 2, 4, 5) score 5
(2, 2, 4, 6) score 6
(2, 2, 5, 1) score 5
(2, 2, 5, 2) score 6
(2, 2, 5, 3) score 5
(2, 2, 5, 4) score 5
(2, 2, 5, 5) score 10
(2, 2, 5, 6) score 6
(2, 2, 6, 1) score 6
(2, 2, 6, 2) score 6
(2, 2, 6, 3) score 6
(2, 2, 6, 4) score 6
(2, 2, 6, 5) score 6
(2, 2, 6, 6) score 12

Each of these hands is equally likely, so to get the expected value, you take the average of these scores, which works out to 5.833333.
