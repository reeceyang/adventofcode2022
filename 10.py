queue = {}
cycle = 1
register = 1
signal = 0
for l in open('10').read().split('\n')[:-1]:
    if l != 'noop':
        a = int(l.split()[1])
        queue[cycle + 2] = a
    if cycle in (20, 60, 100, 140, 180, 220):
        signal += cycle * register
        print(queue)
        print(cycle, register)
        print(cycle * register)
    if cycle in queue:
        register += queue[cycle]
    cycle += 1
print(signal)
        
