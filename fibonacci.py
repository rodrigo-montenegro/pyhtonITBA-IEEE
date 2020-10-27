n = int(input("Ingrese un numero :"))


def fibonacci(n):
    def fib(n):
        if n < 2:
            return n
        else:
            return fib(n-1)+fib(n-2)

    for x in range(0, n+1):
        print(fib(x))


fibonacci(n)
