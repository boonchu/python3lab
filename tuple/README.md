###### Tuple - immutable list

```
>>> x, y = ( 'John', 'Doe' )
>>> print (x, y)
('John', 'Doe')
>>> d = dict()
>>> d['firstname'] = 'John'
>>> d['lastname'] = 'Doe'
>>> for (k,v) in d.items():
...    print (k,v)
...
('lastname', 'Doe')
('firstname', 'John')
>>> t = d.items()
>>> print t
[('lastname', 'Doe'), ('firstname', 'John')]
```
