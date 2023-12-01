with open('2') as f:
    s = f.read().split('\n')
t = [tuple(l.split(' ')) for l in s[:-1]]

def score(x, y):
    m = 'XYZ'.index(y) + 1 
    u = 'ABC'.index(x) + 1 
    if u == m:
        return 3 + m
    if m == u + 1 or u - m == 2:
        return 6 + m
    return m 

def get_move(o, r):
    if r == 'X':
        return 'XYZ'['ABC'.index(o) - 1]
    if r == 'Z':
        return 'XYZ'['ABC'.index(o) - 2]
    return 'XYZ'['ABC'.index(o)]


print(sum([score(x, y) for x,y in t]))  # part 1
print(sum([score(x, get_move(x, y)) for x,y in t])) # part 2
