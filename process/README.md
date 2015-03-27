###### Spawn, Context Switch, Asynchronous
  * Spawn processes
```

thread1 = gevent.spawn(say, "I live in San Jose", 20)
thread2 = gevent.spawn(say, "Hello from thread", 10)

threads = [ thread1, thread2 ]

gevent.joinall(threads)

bigchoo@server1 ~/lab/python3lab/process (master)*$ ./spawn.py
--- thread 20 ---
--- thread 10 ---
Hello from thread
I live in San Jose

```
  * Context switch
```

```
  * Asynchronous
```

```
###### Reference
  * http://sdiehl.github.io/gevent-tutorial/
  * http://www.pixeldonor.com/2014/jan/10/django-gevent-and-socketio/
