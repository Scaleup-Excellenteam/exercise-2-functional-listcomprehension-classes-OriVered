import timeit

"""
Measures the execution time of the given method with its arguments.

:param method: The method to be timed.
:param args: Positional arguments for the method.
:param kwargs: Keyword arguments for the method.
:return: The elapsed time in seconds.
"""
def timer(f, *args, **kwargs):
    start_time = timeit.default_timer()
    f(*args, **kwargs)
    end_time = timeit.default_timer()
    return end_time - start_time


if __name__ == "__main__":
    elapsed_time = timer(print, "Hello")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
    elapsed_time = timer(zip, [1, 2, 3], [4, 5, 6])
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
    elapsed_time = timer("Hi {name}".format, name="Bug")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")