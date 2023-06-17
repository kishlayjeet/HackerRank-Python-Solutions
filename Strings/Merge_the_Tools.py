def merge_the_tools(string, k):
    for item in range(0,len(string) // k):
        piece = string[:k]
        unique = []
        for item in piece:
            if item not in unique:
                unique.append(item)
        string = string[k:]
        print(''.join(unique))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)