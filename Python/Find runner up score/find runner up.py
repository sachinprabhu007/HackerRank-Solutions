if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    print(max([x for x in arr if x != max(arr)]))

