s = open('7').read().split('\n')[1:-1]
root = {}
current = root
for l in s:
    tokens = l.split()
    if tokens[0] == '$':
        if tokens[1] == 'cd':
            if tokens[2] == '..':
                current = current['parent'] 
            else:
                current = current[tokens[2]]
    elif tokens[0] == 'dir':
        if tokens[1] not in current:
            current[tokens[1]] = {'parent': current}
    else:
        current[tokens[1]] = int(tokens[0])

visited = {}
def get_total(t, parent):
    size = 0
    for k, v in t.items():
        if k == 'parent':
            continue
        if type(v) == int:
            size += v
            continue
        path = parent + '/' + k
        if path not in visited:
            visited[path] = get_total(v, path)
        size += visited[path]
    return size

root_size = get_total(root, '/')
print(sum([size for size in visited.values() if size <= 100000]))

needed_space = 30000000 - (70000000 - root_size)
print(min([size for size in visited.values() if size >= needed_space]))

