What is the expected value of trial(n) as a function of n? (Here, assume that n is a 
positive integer.) Enter the answer below as a math expression in n.

def trial(n):
   val = random.randrange(n)
   return val

As a hint, note that the arithmetic sum 0+1+2+..+k has the value 1/2*k*(k+1).

(0.5*(n+1)*(n+2))/n
