def sum(n):
    return n * (n+1) /2
print(sum(5))
def arraysum(a):
    sum = 0
    for i in a:
        sum = sum + i
    return(sum)
a = [78, 928, 209, 982, 287]
print(arraysum(a))
def sum1(n):
    if (n <= 0):
        return 
    return n + sum1(n-1)
print(sum1(10))
    