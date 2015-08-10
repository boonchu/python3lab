##### Kivy Crash Courses

* Guides 
  - http://kivy.org/docs/

* learning an simple app

```
$ ./push_button.py
```

* learning an android apk build
    - https://www.youtube.com/watch?v=t8N_8WkALdE

```
$ brew install python 
$ pip install Cython==0.20
$ pip install --upgrade buildozer
$ cython -V
```

* getting start with android apk

```
$ mkdir hello_apk
$ cp scatter.py hello_apk
$ cd hello_apk
$ buildozer init
$ vim buildozer.spec
$ buildozer android clean update
```

* install latest SDK and add your SDK path to .bashrc

```
PATH=$PATH:$HOME/.buildozer/android/platform/android-sdk-21/tools
$ android list
$ android list sdk --all | grep -i sdk
   1- Android SDK Tools, revision 22.6.2
   2- Android SDK Platform-tools, revision 19.0.1
$ android (select version. aceept licenses and install)
```

```
$ buildozer android debug 
$ buildozer android deploy 
```

* issue from buildozer ** during buildozer android debug **
  - Use solution (https://github.com/kivy/buildozer/issues/146)
  - ~/.buildozer/android/platform/android-sdk-21/tools/android (selects Android SDK Build-tools Rev. 20)
  
```
assets/private.mp3: /Users/bigchoo/Documents/src/python3lab/kivy/tutorials/hello_apk/.buildozer/android/app/sitecustomize.pyo
Traceback (most recent call last):
  File "build.py", line 509, in <module>
    make_package(args)
  File "build.py", line 357, in make_package
    subprocess.check_call([ANT, arg])
  File "/usr/local/Cellar/python/2.7.8_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 540, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['ant', 'debug']' returned non-zero exit status 1
```

###### Publish app to store
  - http://developer.android.com/distribute/googleplay/start.html

###### Kivy path info
```
$ kivy
Python 2.7.6 (default, Sep  9 2014, 15:04:36)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import kivy; print(kivy.__path__)
[INFO   ] [Logger      ] Record log in /Applications/Kivy.app/Contents/Resources/.kivy/logs/kivy_15-08-08_15.txt
[INFO   ] [Kivy        ] v1.9.0
[INFO   ] [Python      ] v2.7.6 (default, Sep  9 2014, 15:04:36)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)]
['/Applications/Kivy.app/Contents/Resources/kivy/kivy']
```
