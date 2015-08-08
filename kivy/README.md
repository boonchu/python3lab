##### Kivy on Yosemeite OS/X

Ref: https://www.safaribooksonline.com/library/view/creating-apps-in/9781491947333/ch01.html

* download Kivy.app from  http://kivy.org/
* install app and drag & drop to /Applications foloder
* before unmounting app installer, double click to install 'MakeSymlinks'
* I use this symlink to handle this job

```
if [ -d /Applications/Kivy.App ];
then
    sudo ln -s /Applications/Kivy.app/Contents/Resources/script /usr/local/bin/kivy
    osascript -e 'display notification "Symlink created" with title "Kivy: Make Symlinks"'
else
    osascript -e 'display notification "Kivy.app does not exist in /Applications." with title "Kivy: Make Symlinks"'
fi
```

##### Testing Kivy

```
└─[$] <git:(master*)> kivy
Python 2.7.6 (default, Sep  9 2014, 15:04:36)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from kivy.app import App
[INFO   ] [Logger      ] Record log in /Applications/Kivy.app/Contents/Resources/.kivy/logs/kivy_15-08-08_1.txt
[INFO   ] [Kivy        ] v1.9.0
[INFO   ] [Python      ] v2.7.6 (default, Sep  9 2014, 15:04:36)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)]
[INFO   ] [Factory     ] 173 symbols loaded
[INFO   ] [Image       ] Providers: img_tex, img_imageio, img_dds, img_gif, img_sdl2 (img_pil, img_ffpyplayer ignored)
>>> App().run()
```
