s = open('6').read()

for j in range(3, len(s)):
    if len(set(list(s[j - 3:j + 1]))) == 4:
        print(j + 1)  # part 1
        break
    
for j in range(13, len(s)):
    if len(set(list(s[j - 13:j + 1]))) == 14:
        print(j + 1)  # part 2
        break
