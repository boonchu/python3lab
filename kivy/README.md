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
