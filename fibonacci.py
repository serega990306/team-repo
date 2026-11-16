"""Вычисление чисел Фибоначчи."""


def fibonacci(n: int) -> int:
    """Возвращает n-е число Фибоначчи: fibonacci(0) = 0, fibonacci(1) = 1."""
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    print("Первые 10 чисел Фибоначчи:", [fibonacci(i) for i in range(10)])
