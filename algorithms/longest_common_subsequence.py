# explanation: https://youtu.be/sSno9rV8Rhg

# approach 1: recursion


def LCS_recursion(A, B, m, n):
    """
    Function to find longest common subsequence in a naive recursive way.
    
    Args:
      A (str): First input string sequence.  
      B (str): Second input string sequence. 
      m (int): length of string A. 
      n (int): length of string B. 
    
    Returns:
      LCS_recursion (int): returns the length of longest common subsequence.  
    """
    if m == 0 or n == 0:
        return 0
    elif A[m - 1] == B[n - 1]:
        return 1 + LCS_recursion(A, B, m - 1, n - 1)
    else:
        return max(LCS_recursion(A, B, m, n - 1),
                   LCS_recursion(A, B, m - 1, n))


if __name__ == "__main__":
    A = "AGGTAB"
    B = "GXTXAYB"
    m = len(A)
    n = len(B)

    print(f"Length of the LCS: {LCS_recursion(A, B, m, n)}")
