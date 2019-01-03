def swap_case(s):
    res = str.swapcase(s)
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)