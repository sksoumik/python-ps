"""
Find nth fibonacci number using recursion, memoization, bottom-up approach
1 1 2 3 5 8 ..... 
"""


def fib_recursion(n):
    """
    [find nth fibonacci number using recursion]
    
    Arguments:
        n {[int]} -- [the element number from an array/list]
    
    Returns:
        [int] -- [description]
    """
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_recursion(n - 1) + fib_recursion(n - 2)
    return result


def fib_memoization(n, memo):
    """
    [DP: memoization approach]
    
    Arguments:
        n {[int]} -- [nth fibonacci number]
        memo {[List]} -- [array for storing calculation]
    
    Returns:
        [int] -- [returns the nth fibonacci number]
    """
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        memo[n] = result
        result = fib_recursion(n - 1) + fib_recursion(n - 2)
    return result


if __name__ == "__main__":
    nth_value = 3
    print(fib_recursion(nth_value))
