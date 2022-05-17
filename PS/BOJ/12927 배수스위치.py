import sys

bulb = list(sys.stdin.readline().strip())

cnt = 0
for i in range(len(bulb)):
    if bulb[i] == 'Y':
        for j in range(i, len(bulb), i+1):
            bulb[j] = ('N' if bulb[j] =='Y' else 'Y')
        cnt += 1
print(cnt)
