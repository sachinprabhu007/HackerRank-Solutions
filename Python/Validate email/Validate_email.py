import re


addr = re.compile(
    '''^
    [\w-]{1,}           #username
    @[a-zA-Z0-9]{1,}    #websitename
    \.\w{1,3}           #extension
    $''', re.UNICODE | re.VERBOSE)

print(sorted(filter(addr.search, (input() for _ in range(int(input()))))))


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)