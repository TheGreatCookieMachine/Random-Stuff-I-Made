def fizzbuzz(n):
    if n%5==0 and n%3==0:
        print('Fizz Buzz')
    elif n%5==0:
        print('Buzz')
    elif n%3==0:
        print('Fizz')
    else:
        print(n)
n = list(range(1, 101))
list(map(fizzbuzz, n))
