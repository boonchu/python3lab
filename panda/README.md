##### Panda OSX

* pip3 install --upgrade pip

```
pip3 --version
pip 8.1.2 from /usr/local/lib/python3.5/site-packages (python 3.5)
```

* pip3 install -U numpy matplotlib pandas

* pip3 install --upgrade "ipython[all]"
* pip3 install -U 'jupyter[notebook]'

* config the jupyter

```
$ jupyter --config
/Users/bigchoo/.jupyter


```

* jupyter notebook

* jupyter console

```
In [1]: 1+2
Out[1]: 3

In [2]: print(1+2)
3

In [3]: my_dict = { "name":"Roshan", "credit":100 }

In [4]: my_dict
Out[4]: {'credit': 100, 'name': 'Roshan'}

In [5]: my_dict['name']
Out[5]: 'Roshan'

In [6]: my_dict.values()
Out[6]: dict_values([100, 'Roshan'])

In [1]: my_list = [1, 3, 5, 7, 9]

In [2]: my_list[:3]
Out[2]: [1, 3, 5]

In [3]: my_list[3:]
Out[3]: [7, 9]

In [4]: my_list[-1]
Out[4]: 9

In [5]: my_list[-2]
Out[5]: 7

In [6]: my_list[-2:]
Out[6]: [7, 9]

In [7]: my_list[:-2]
Out[7]: [1, 3, 5]

In [8]: my_list[3:-1]
Out[8]: [7]

In [9]: my_list[::2]
Out[9]: [1, 5, 9]

In [10]: my_list[3::2]
Out[10]: [7]

In [11]: my_list[::-1]
Out[11]: [9, 7, 5, 3, 1]
```

### Ref

* https://www.youtube.com/watch?v=o8fmjaW9a0A
* https://github.com/ipython-contrib/IPython-notebook-extensions/issues/282
