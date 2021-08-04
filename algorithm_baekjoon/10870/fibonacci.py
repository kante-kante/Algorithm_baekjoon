'''
10870번 - 피보나치 수

피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
그 다음 2번째부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

풀이
문제에 식이 있었기 때문에 그렇게 어렵지 않았던 문제.
첫 조건은 0과 1로 시작하며 0번째 피보나치 수는 0, 1번째 피보나치 수는 1이고
그 다음부터는 바로 앞 두 피보나치 수의 합이 된다고 하였으므로 재귀를 사용하여 호출해준다.

입력값이 0과 1일때의 조건을 먼저 설정해주고, 입력값이 0 또는 1이 아닌 경우
바로 앞 두 피보나치 수의 합이 된다고 하였으므로 n-1, n-2로 각각 재귀 호출 한다.
'''

n = int(input())

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))