#### How to subprocess #####

```
>>> import subprocess
>>> proc = subprocess.Popen(['echo', '"Hello world!"'], stdout=subprocess.PIPE)
>>> stderr, stdout = proc.communicate()
>>> stdout
>>> stderr
'"Hello world!"\n'
```

```
>>> import subprocess
>>> subprocess.call('echo $HOME')
Traceback (most recent call last):
...
OSError: [Errno 2] No such file or directory
>>>
>>> subprocess.call('echo $HOME', shell=True)
/user/khong
0
```
