f = open('3').read().split('\n')
p = 0
for l in f[:-1]:
    first = set(list(l[:len(l)//2]))
    second = set(list(l[len(l)//2:]))
    common = (first & second).pop()
    pre = p
    if common.isupper():
        p += ord(common) - ord('A') + 27
    else:
        p += ord(common) - ord('a') + 1
print(p)  # part 1

c = 0
p = 0
group = set()
for l in f[:-1]:
    c += 1
    if c == 1:
        group = set(list(l))
    else:
        group &= set(list(l))
    if c == 3:
        common = group.pop()
        if common.isupper():
            p += ord(common) - ord('A') + 27
        else:
            p += ord(common) - ord('a') + 1
        c = 0
print(p)  # part 2
