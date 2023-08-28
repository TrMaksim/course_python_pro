import asyncio
import time


def sync_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(
            f"Sync function {func.__name__} was executed in {execution_time:.6f} seconds"
        )
        return value

    return wrapper


def async_decorator(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(
            f"Async function {func.__name__} was executed in {execution_time:.6f} seconds"
        )
        return result

    return wrapper


@sync_decorator
def synchronous_factorial(n):
    if n == 1:
        return 1
    return synchronous_factorial(n - 1) * n


@async_decorator
async def asynchronous_function():
    await asyncio.sleep(2)
    return "Async function executed"


async def main():
    synchronous_factorial(5)
    await asynchronous_function()


if __name__ == "__main__":
    asyncio.run(main())
