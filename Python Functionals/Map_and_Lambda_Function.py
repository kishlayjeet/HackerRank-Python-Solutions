cube = lambda x: x**3

def fibonacci(n):
    fibonacci_nums = [0, 1]
    if n > 2:
        for i in range(2, n):
            fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    return fibonacci_nums[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))