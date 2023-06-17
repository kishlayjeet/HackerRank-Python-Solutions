if __name__ == '__main__':
    s = input()
    
    # 1st Approach
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))
    
    
    # 2nd Approach
    alnum = alpha = digit = lower = upper = False
    
    for i in s:
        if(i.isalpha()):
            alpha = i.isalpha()
        if(i.isalnum()):
            alnum = i.isalnum()
        if(i.isdigit()):
            digit = i.isdigit()
        if(i.isupper()):
            upper = i.isupper()
        if(i.islower()):
            lower = i.islower()
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)

