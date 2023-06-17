import string

def print_rangoli(size):
    alpha = list(string.ascii_lowercase)[:size]
    s_alpha = [i for i in alpha[:size]][::-1]
    height = size * 2-1
    width = height + height-1

    # Upper
    for i in range(size):
        p_alpha = [a for a in s_alpha[:i+1]] + [a for a in s_alpha[:i]][::-1]
        print('-'.join(p_alpha).center(width, '-'))

    # Lower
    for i in range(size-2, -1, -1):
        p_alpha = [a for a in s_alpha[:i+1]] + [a for a in s_alpha[:i]][::-1]
        print('-'.join(p_alpha).center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
