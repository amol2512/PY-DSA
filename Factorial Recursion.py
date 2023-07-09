def factorial_rec(n):
    #Base Case 
    if (n==0):
        return 1 
    
    #smallerProblem = factorial_rec(n-1)
    #biggerProblem = n * factorial_rec(n-1)

    return n * factorial_rec(n-1)

num = int(input("Enter a number:"))
result = factorial_rec(num)
print(result)