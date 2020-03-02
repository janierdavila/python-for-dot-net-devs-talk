#yield
def filter_numbers(predicate):
    for i in range(0, 100):
        if predicate(i):
            yield i

numbers = filter_numbers(lambda n: n % 2 == 0)
for n in numbers:
    print(n)
	
#Classes

class ShoppingCart:

    def __init__(self):
        self.items = []

    def addItems(self, name, price):
        self.items.append((name,price))

    def __iter__(self):
        return self.items.__iter__()

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.addItems('xbox', 500)
    cart.addItems('playstation', 400)

    for item in cart:
        print(item)
		
#lambda
def add(x,y):
    return x + y

c = add(5, 6)
print(c)

# lambda
add2 = lambda x, y: x + y

c = add2(5, 6)
print(c)

#functions
def banner(message, border="-"):
    banner = border * len(message)
    print(banner)
    print(message)
    print(banner)

numbers = [1, 2, 3, 4, 5, 6]

for n in numbers:
    print(n, end=', ')
	
#Decorators
import functools
import time

def timer(func):
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

#except
def test():
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        finally:
            print("I always execute")

#context managers
class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

files = []
for _ in range(10000):
    with File('foo.txt', 'w') as infile:
        infile.write('foo')
        files.append(infile)

# Async/Await
#  pip install aiohttp
import signal  
import sys  
import asyncio  
import aiohttp  
import json

loop = asyncio.get_event_loop()  
client = aiohttp.ClientSession(loop=loop)

async def get_json(client, url):  
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()

async def get_reddit_top(subreddit, client):  
    data1 = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

    j = json.loads(data1.decode('utf-8'))
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        print(str(score) + ': ' + title + ' (' + link + ')')

    print('DONE:', subreddit + '\n')

def signal_handler(signal, frame):  
    loop.stop()
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

asyncio.ensure_future(get_reddit_top('python', client))  
asyncio.ensure_future(get_reddit_top('programming', client))  
asyncio.ensure_future(get_reddit_top('compsci', client))  
loop.run_forever() 