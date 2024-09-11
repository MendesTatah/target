def pertence_fibonacci(num):
    if num < 0:
        return False
    a, b = 0, 1
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    return False



num = int(input("Digite um número para saber se ele pertence a sequência de Fibonacci: "))
if pertence_fibonacci(num):
    print(f"O número {num} pertence a sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence a sequência de Fibonacci.")