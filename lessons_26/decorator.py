import asyncio
import time


def async_sync_decorator(func):
    def wrapper(*args, **kwargs):
        is_async = asyncio.iscoroutinefunction(func)
        start_time = time.time()
        if is_async:
            result = asyncio.run(func(*args, **kwargs))
        else:
            result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        function_type = "Async" if is_async else "Sync"
        print(
            f"{function_type} function {func.__name__} was executed in {execution_time:.6f} seconds"
        )
        return result

    return wrapper


@async_sync_decorator
def synchronous_factorial(n):
    if n == 1:
        return 1
    return synchronous_factorial(n - 1) * n


@async_sync_decorator
async def asynchronous_function():
    await asyncio.sleep(2)
    return "Async function executed"


def main():
    synchronous_factorial(5)
    asynchronous_function()


if __name__ == "__main__":
    main()
