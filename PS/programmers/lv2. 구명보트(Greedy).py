from collections import deque

# def solution(people, limit) :
#     answer = 0
#     people.sort()
#
#     a = 0
#     b = len(people) - 1
#     while a < b :
#         if people[b] + people[a] <= limit :
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer



def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people = deque(people)
    while people:
        if len(people) <= 1:
            people.pop()
        else:
            if people[0] + people[-1] <= limit:
                people.pop()
                people.popleft()
            else:
                people.popleft()

        answer += 1
    return answer

appeach = [70, 80, 50]
muzi = 100
frodo = solution(appeach, muzi)
print(frodo)