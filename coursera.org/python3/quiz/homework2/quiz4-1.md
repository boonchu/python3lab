#### Consider the mathematical 

```
function explode(x)= ( 2 ** x ) ** 2 or (2 ^ x) ^ 2
```

What is the result of evaluating 

```
explode(log2(y)) if y>0? 
```

Your answer should be reduced to a simple expression that does not 
involve logarithms or exponentials.

Hint: review the math notes on "Functions" carefully and note the 
relationship between the exponential function and the logarithm 
function when computed using the same base.

Enter the answer as a math expression below. To format your 
expression correctly, please consult this page. Remember to 
use the Preview button (as well as the Help link) to make sure 
that your expression is formatted correctly.

answer:
  - https://class.coursera.org/principlescomputing1-004/wiki/view?page=functions

```
y^2
```

Sidenote:
https://en.wikipedia.org/wiki/Logarithm#Motivation_and_definition

If you have explode(x)=(2^x)^2, then

```
explode(k)=(2^k)^2
explode(y)=(2^y)^2
explode(x+3)=(2^(x+3))^2
```

and so

```
explode(log2(y))=...
```

Thread Discussion:
 * https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=126
 * http://tla-lotro.enjin.com/forum/m/19279343/viewthread/19888466-math-problem

```
y = (2^y)^2
log2(y) = log2((2^y)^2) if y>0
log2(y) = y^2
y^2 = log2(2^y^2) = 2^log2(y^2)
```

logc(c^x)=x proved to be most helpful to me, on the functions page,
after reading Shengbing Huang's x=log2(2^x)=2^log2(x)

```
>>> import math
>>>
>>> y=5
>>> print y**2
25
>>> print math.log(2**y**2, 2)
25.0
>>>
>>> y=10
>>> y**2
100
>>> print math.log(2**y**2, 2)
100.0
>>>
```
