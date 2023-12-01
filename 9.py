NUM_ROPES = 10
ropes = [(0, 0) for _ in range(NUM_ROPES)]
d_v = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
visited = set()
def sgn(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for l in open('9').read().split('\n')[:-1]:
    d, steps = l.split()
    for _ in range(int(steps)):
        hx, hy = ropes[0]
        d_vx, d_vy = d_v[d]
        ropes[0] = hx + d_vx, hy + d_vy
        for i in range(1, len(ropes)):
            h = ropes[i - 1]
            hx, hy = h
            t = ropes[i]
            tx, ty = t
            dx, dy = hx - tx, hy - ty
            if dist(h, t) >= 2 and not (abs(dx) == 1 and abs(dy) == 1):
                ropes[i] = tx + sgn(dx), ty + sgn(dy)
        visited.add(ropes[-1]) 
print(len(visited))
            



