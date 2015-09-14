###### 2048 Game

![2048 game](https://raw.githubusercontent.com/boonchu/python3lab/master/coursera.org/python3/2048/2048.png)

###### Rules
  * https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=324

```
1. Scan each cell in the board. See if there are any empty cells. And while you are at it, 
see if any cell contains 2048.

2. If a cell contains 2048, the game is over and the player won.

3. If there is at least one empty cell, the game is not yet over.

4. If there are no empty cells, then iterate through each row and column and do a merge 
(but do not copy the merged line back to the game board!). After the merge, compare the merged 
line to the original line. If there is any change, the game is not yet over, and you do not 
need to do any further checking. Note: this is like simulating move UP (or DOWN) and move 
LEFT (or RIGHT). You only need to do two directions, though, it is not necessary to do all 
four directions.

5. If, after the simulated moves, there are no changes, then I think you can say the game 
is over and the player lost.

You can probably combine some of this... for example, in step 4, you can check each row 
*before* merging it for a 2048, in which case the player won; and you can check for a 0, 
in which case there is no need to check anything more since the player can still move.

```
