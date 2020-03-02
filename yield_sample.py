'''
    Example to mimic the C# looping and filtering by predicate
'''

def filter_numbers(predicate):
    for i in range(0, 100):
        if predicate(i):
            yield i

numbers = filter_numbers(lambda n: n % 2 == 0)
for n in numbers:
    print(n)