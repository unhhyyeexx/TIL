### 백준  15953 상금헌터

```python
T = int(input())

reward1 = [500, 300, 200, 50, 30, 10]
reward2 = [512, 256, 128, 64, 32]
winner1 = [1, 3, 6, 10, 15, 21]
winner2 = [1, 3, 7, 15, 31]

totalreward = []

for t in range(T):

    a, b = map(int, input().split())

    a_reward = []
    b_reward = []

    for i in range(len(winner1)):
        if a > 21 or a == 0:
            a_reward.append(0)
        elif a <= winner1[i]:
            a_reward.append(reward1[i])
    
    for j in range(len(winner2)):
        if b > 31 or  b == 0:
            b_reward.append(0)
        elif b <= winner2[j]:
            b_reward.append(reward2[j])

    
    totalreward.append((max(a_reward) + max(b_reward)) * 10000)

for i in totalreward:
    print(i)
```

```python
T = int(input())

reward1 = [500, 300, 200, 50, 30, 10]
reward2 = [512, 256, 128, 64, 32]
winner1 = [1, 3, 6, 10, 15, 21]
winner2 = [1, 3, 7, 15, 31]

totalreward = []

for t in range(T):

    a, b = map(int, input().split())

    a_reward = []
    b_reward = []

    for i in range(len(winner1)):
        if a > 21 or a == 0:
            a_reward.append(0)
        elif a <= winner1[i]:
            a_reward.append(reward1[i])
    
    for j in range(len(winner2)):
        if b > 31 or  b == 0:
            b_reward.append(0)
        elif b <= winner2[j]:
            b_reward.append(reward2[j])

    a_reward.sort()
    b_reward.sort()
    totalreward.append((a_reward[-1] + b_reward[-1]) * 10000)

for i in totalreward:
    print(i)
```



## 백준 1783 병든 나이트

```python
n, m = map(int,input().split())

if n == 1 or m == 1:
    print(1)

elif n == 2:
    if m < 9:
        print((m+1)//2)
    else:
        print(4)

else:
    if m < 5 :
        print(m)
    elif m <= 6:
        print(4)
    else: 
        print(m-2)
```

