# Функція caching_fibonacci
def caching_fibonacci():
    # Порожній словник cache
    cache = {}
    # Внутрішня функція fibonacci(n)
    def fibonacci(n):
        # Розрахунки функції fibonacci(n)
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci
Result_fib = caching_fibonacci()
# Вивід числа Фібоначчі для значень 15 та 10
print(Result_fib(15))
print(Result_fib(10))