##### Code Style
  * https://class.coursera.org/principlescomputing1-004/wiki/view?page=pylint_errors
  * https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=41

```
Indeed using 'i' as index variable feels very natural in languages like C where you iterate through arrays using indexes exclusively. however in Python you can iterate multiple ways. For example, using meaningful variable name helps me to quickly understand what my code is iterating over and what the variable content is:

for key in dict.keys():
for idx in range(len(list)):
for idx, element in enumerate(list):
for element in list:

and so fort. This way I don't misuse idx as element and vice versa somewhere deeper in the code.
```
