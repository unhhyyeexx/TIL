
N = int(input())

five = N // 5
rem = N % 5
three = 0

while five >= 0:

    if rem % 3 == 0:
        three = rem // 3
        break

    five -= 1
    rem += 5

print(five + three)
