# memo is a dictionary that works as a history for
memo = {}


def fibonacci(n):
    """
    takes in an integer n and return the nth Fibonacci number
    TimeComplexity: O(n) since I am using a dictionary to store the values of every n node when we calc it
    SpaceComplexity: O(n)
    """
    # check if the value of n fib is in memo
    if n in memo:
        return memo[n]
    # base case: when n is between 1 and 2 return 1
    if 1 <= n <= 2:
        return 1
    # base case 2: if n is equal to 0 return 0
    if n == 0:
        return 0
    # make a recursive call given n -1 and n - 2
    f = fibonacci(n - 1) + fibonacci(n - 2)
    # add the answer to fib(n) in memo
    memo[n] = f
    return f

