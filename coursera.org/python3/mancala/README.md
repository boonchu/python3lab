###### Mancala
    - https://class.coursera.org/principlescomputing1-004/wiki/view?page=mancala

###### How to import custom modules in python
    - https://class.coursera.org/principlescomputing1-004/wiki/view?page=imports

###### How to call object class (example from Solitaire Mancala)
    - http://stackoverflow.com/questions/4534438/typeerror-module-object-is-not-callable

```
import SolitaireMancala
>>> SolitaireMancala.SolitaireMancala
<class SolitaireMancala.SolitaireMancala at 0x10e20cb48>

>>> from SolitaireMancala import SolitaireMancala
>>> SolitaireMancala
<class SolitaireMancala.SolitaireMancala at 0x10e20cb48>
```

###### Use testing suite with Solitaire Mancala

```
$ ./poc_mancala_testsuite.py
Ran 19 tests. 0 failures.
```
