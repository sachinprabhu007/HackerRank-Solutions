def split_and_join(line):
    # write your code here
    line = line.split(" ")
    res = "-".join(line)
    return res

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
