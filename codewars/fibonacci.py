def productFib(prod):
    
    fib1 = 0
    fib2 = fib1+1
    while True:
        fib = fib1 + fib2
        if fib1 * fib2 >= prod:
            break
        fib1 = fib2
        fib2 = fib

    return [fib1, fib2, (fib1 * fib2 == prod)]

""" prettier version """

def productFib2(prod):
    fib1, fib2 = 0, 1
    while fib1 * fib2 < prod:
        fib1, fib2 = fib2, fib1 + fib2
    return [fib1, fib2, fib1 * fib2 == prod]