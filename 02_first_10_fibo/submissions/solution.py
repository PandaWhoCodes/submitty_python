def printFibonacciNumbers(n):

    f1 = 0
    f2 = 1
    if (n < 1):
        return
    print(0)
    for x in range(0, n-1):
        print(f2)
        next = f1 + f2
        f1 = f2
        f2 = next

if __name__ == '__main__':
    printFibonacciNumbers(10)
