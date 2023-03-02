##Problem
# Given a staircase of 'n' steps, 
#count the number of distinct ways to climb to the top.
#you can climb 1 step or 2 steps at a time.
def climbing_staircase(n):
    fib = [1,2]
  
    for i in range(2,n):
        num = fib[i-1] + fib[i-2]
        fib.append(num)
    
    return fib[n-1]
    