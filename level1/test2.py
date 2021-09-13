def solution(s):
    answer = ''
    check = 0
    if (len(s) % 2 == 0):
        check = len(s) // 2
        answer = answer + s[check - 1:check + 1]

    else:
        check = len(s) // 2
        answer = answer + s[check]


    return answer

print(solution("abcde"))
print(solution("qwer"))

