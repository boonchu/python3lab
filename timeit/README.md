###### Timeit

```
timeit git:master ❯ python -m timeit '"-".join(str(n) for n in range(100))'                                                                                 ✭
10000 loops, best of 3: 20.9 usec per loop

timeit git:master ❯ python -m timeit '"-".join(map(str, range(100)))'                                                                                     ⏎ ✭
100000 loops, best of 3: 17.7 usec per loop

```
