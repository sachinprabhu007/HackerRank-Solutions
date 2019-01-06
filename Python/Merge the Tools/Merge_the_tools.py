from collections import OrderedDict

def merge_the_tools(string, k):
    i = iter(string)
    for sub in zip(*[i]*k):
        print(*OrderedDict.fromkeys(sub),sep='')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
