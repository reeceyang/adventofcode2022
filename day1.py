with open('input1') as f:
    s = f.read()

print(sum(sorted([sum([int(u) for u in t.split('\n') if u != '']) for t in s.split('\n\n')])[-3:]))
