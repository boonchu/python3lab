###### Merge 2048
  * [Merge 2048 mini project] 
    - https://class.coursera.org/principlescomputing1-004/wiki/view?page=2048_%28Merge%29
    - https://class.coursera.org/principlescomputing1-004/wiki/view?page=2048

  * [Tic Tac Toe]
    - https://class.coursera.org/principlescomputing1-004/wiki/view?page=tictactoemc

  * Expected Value
    - http://www.stat.ucla.edu/~cochran/stat10/winter/lectures/lect8.html

###### SimplePlot
  * https://pypi.python.org/pypi/SimpleGUITk
  * http://stackoverflow.com/questions/18280436/importerror-matplotlib-requires-dateutil

```
brew update
sudo xcodebuild -license
brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
sudo pip install https://bitbucket.org/pygame/pygame/get/default.tar.gz
sudo pip install numpy python-dateutil pytz pyparsing six --force-reinstall --upgrade

wget https://pypi.python.org/packages/source/S/SimpleGUITk/SimpleGUITk-1.1.3.tar.gz\#md5\=d940d6b25a72b941f3c43e76bff95eb0
tar -xvzf SimpleGUITk-1.1.3.tar.gz && cd SimpleGUITk-1.1.3 && python setup.py -v build && python setup.py -v install
```

###### SimpleGUI
   * Document link
        - http://simpleguics2pygame.readthedocs.org/en/latest/simpleplot.html
   * Use instruction from SimplePlot
   * Update simplegui
        - https://bitbucket.org/OPiMedia/simpleguics2pygame
   * Verify script

```
> $ pip install matplotlib
> $ pip install SimpleGUICS2Pygame
```

```
> $ SimpleGUICS2Pygame_check.py
script/SimpleGUICS2Pygame_check.py (April 21, 2014)
===================================================
python - version 2.7.8 (default, Aug  8 2015, 11:56:52)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)]


import matplotlib ok - Version 1.4.3


import pygame ok - Version 1.9.2a0
pygame.init() 6 modules loaded ok


import SimpleGUICS2Pygame ok - Version 01.09.00

import SimpleGUICS2Pygame.codeskulptor ok
import SimpleGUICS2Pygame.codeskulptor_lib ok
import SimpleGUICS2Pygame.numeric ok
import SimpleGUICS2Pygame.simplegui_lib ok
import SimpleGUICS2Pygame.simplegui_lib_draw ok
import SimpleGUICS2Pygame.simplegui_lib_fps ok
import SimpleGUICS2Pygame.simplegui_lib_keys ok
import SimpleGUICS2Pygame.simplegui_lib_loader ok
import SimpleGUICS2Pygame.simpleguics2pygame ok
import SimpleGUICS2Pygame.simpleplot ok
```

###### Verification

```
$ pip list --local | grep -i simple
SimpleGUICS2Pygame (01.09.00)
SimpleGUITk (1.1.3)
```

###### using matplotlib
  * https://www.udacity.com/wiki/plotting-graphs-with-python

###### CodeSkulptor (http://www.cs.rice.edu/~rixner/)
  * https://github.com/skulpt/skulpt
  * http://www.skulpt.org/
  * http://codemirror.net/
