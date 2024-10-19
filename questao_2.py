def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def sequencia(numero):
    i = 0
    while True:
        fib = fibonacci(i)
        if fib == numero:
            return True
        if fib > numero:
            return False
        i += 1

numero = int(input("Digite um número: "))
if sequencia(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
