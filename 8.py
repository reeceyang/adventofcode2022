s = open('8').read().split('\n')[:-1]

forest = []
for l in s:
    forest.append(list(l))

visible = 0
max_score = 0
for i, row in enumerate(forest):
    for j, tree in enumerate(row):
        if i == 0 or j == 0 or i == len(forest) - 1 or j == len(row) - 1:
            visible += 1
            continue # score 0
        else:
            left = all([forest[i][other] < tree for other in range(j)])
            right = all([forest[i][other] < tree for other in range(j + 1, len(row))])
            up = all([forest[other][j] < tree for other in range(i)])
            down = all([forest[other][j] < tree for other in range(i + 1, len(forest))])
            if left or right or up or down:
                visible += 1

        score = 1
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dist = 1
            while 0 < i + dist * dr < len(forest) - 1 and 0 < j + dist * dc < len(row) - 1 and forest[i + dist * dr][j + dist * dc] < tree:
                dist += 1
            score *= dist
        max_score = max(score, max_score) 

print(visible)
print(max_score)

