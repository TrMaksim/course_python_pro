import time


def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} was executed in {execution_time:.6f} seconds")
        return value

    return wrapper


@decorator
def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


def main():
    factorial(13)


if __name__ == "__main__":
    main()
