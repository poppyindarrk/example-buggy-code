def fibonacci(n):
    # Bug: Missing base case, causing a recursion error
    return fibonacci(n-1) + fibonacci(n-2)
