##### NumPy

```
python3lab git:master ❯ python
Python 2.7.6 (default, Sep  9 2014, 15:04:36)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> x = np.array([2.,3.])
>>> 2*x
array([ 4.,  6.])
>>> np.sqrt(x) * np.cos(x) * x**3
array([ -4.708164  , -46.29736719])
```

```
>>> x = np.array(range(3))
>>> print x
[0 1 2]
>>> x = np.array(range(3), dtype=complex)
>>> print x
[ 0.+0.j  1.+0.j  2.+0.j]
>>> (x + 1.j) * 2.j
array([-2.+0.j, -2.+2.j, -2.+4.j])
```

```
>>> print float(8/3)
2.0
>>> from scipy.integrate import quad
>>> def f(x):
...     return x**2
...
>>> quad(f, 0., 2.)
(2.666666666666667, 2.960594732333751e-14)
>>> f = lambda x: x**2
>>> f(4)
16
>>> quad(lambda x: x**2, 0., 2.)
(2.666666666666667, 2.960594732333751e-14)
```
