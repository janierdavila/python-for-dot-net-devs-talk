import functools
import time

def timer(func):
    '''
        Example of how to create a decorator.
        @timer decorator will print how long the function being wrapped performed
    '''
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        start_time = time.perf_counter() 

        value = func(*args, **kwargs)
        
        # Do something after
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_decorator


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])