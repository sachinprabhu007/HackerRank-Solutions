if __name__ == '__main__':
    s = input()
    for fn in [str.isalnum, 
               str.isalpha,
               str.isdigit,
               str.islower,
               str.isupper]:    
     print(any(fn(c) for c in s))

