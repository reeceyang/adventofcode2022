s = open('4').read().split('\n')[:-1]
counter = 0
counter2 = 0
for l in s:
    p1, p2 = l.split(',')
    start1, end1 = (int(x) for x in p1.split('-'))
    start2, end2 = (int(x) for x in p2.split('-'))
    if (start1 <= start2 and end2 <= end1) or (start2 <= start1 and end1 <= end2):
        counter += 1
    if not (start1 > end2 or end1 < start2):
        counter2 +=1

print(counter)  # part 1
print(counter2)  # part 2
