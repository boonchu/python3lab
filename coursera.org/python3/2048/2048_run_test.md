###### My test for the full 2048 game
  - https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=114

I created a test that runs my 2048 game through its paces, outside of the OwlTest suite. I offer it here as one possible aid to visualize the results of moves while you test and debug your version of the game.

To run it, I call my test function like this:

```
run_test(5, 4, 20)
```

This test will:

1. Start a board of 5 rows and 4 columns.
2. Display the initial board.
3. Make 20 random moves (up, down, left or right), displaying the board after each move.

Note: This test requires that you have implemented __str__ in  your TwentyFortyEight class, so that the board can be printed in CodeSkulptor console output.

```
def run_test(rows, cols, moves):
    """
    Start a game using a "rows" x "cols" board. Then make "moves"
    random moves, displaying the board after each move.
    """
    directions = { UP:"up", DOWN:"down", LEFT:"left", RIGHT:"right" }

    game = TwentyFortyEight(rows, cols)

    # Display initial board
    print "Start of game:"
    print str(game)

    # Make some random moves, showing the board after each move.
    for move_number in range(moves):
        move = random.choice([UP, DOWN, LEFT, RIGHT])
        print
        print "Move:", move_number + 1, "- Sliding tiles", directions[move]
        game.move(move)
        print str(game)


run_test(5, 4, 20)
```


Example screen shot:
(Notice that the first move happens to be UP, so nothing changes, no new tile is added.)

![2048_run_test.png]
