crates = (
"""P 0 C 0 0 M 0 0 0      
D 0 P B 0 V S 0 0    
Q V R V 0 G B 0 0    
R W G J 0 T M 0 V
V Q Q F C N V 0 W
B Z Z H L P L J N
H D L D W R R P C
F L H R Z J J D D""")

stacks = [[] for _ in range(9)]
for l in crates.split('\n'):
    for stack, crate in enumerate(l.split(' ')):
        if stack == 9:
            break
        if crate == '0':
            continue
        stacks[stack].insert(0, crate)

f = open('5').read().split('\n')
for l in f[:-1]:
    n, a, b = (int(x) for x in l.split())
#   for i in range(n):
#       crate = stacks[a - 1].pop()
#       stacks[b - 1].append(crate)
    pile = stacks[a - 1][-n:]
    stacks[a - 1] = stacks[a - 1][:-n]
    stacks[b - 1].extend(pile)

ans = ''
for stack in stacks:
    ans += stack[-1]

print(ans)
