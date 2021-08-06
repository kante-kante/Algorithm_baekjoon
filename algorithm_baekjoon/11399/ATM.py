'''
11399 - ATM

문제
인하은행에는 ATM이 1대밖에 없다. 지금 이 ATM 앞에 N명의 사람들이 줄을 서있다.
사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.

사람들이 줄을 서는 순서에 따라서 돈을 인출하는데 필요한 시간의 합이 달라지게 된다.
예를 들어, 총 5명이 있고 p1 = 3, p2 = 1, p3 = 4, p4 = 3, p5 = 2인 경우
[1,2,3,4,5] 순서로 줄을 선다면, 1번 사람은 3분만에 돈을 뽑을 수 있다.
2번 사람은 1번 사람이 돈을 뽑을 때 까지 기다려야 하기 때문에 3 + 1 = 4분이 걸리게 된다.
이럴 경우 각 사람이 돈을 인출하는데 필요한 시간의 합은 3+4+8+11+13 = 39분이 된다.

줄을 [2,5,1,4,3] 순서로 줄을 서면, 2번 사람은 1분만에, 5번 사람은 2분만에...
필요한 시간의 합은 1+3+6+9+13 = 32분이다. 이 방법보다 더 필요한 시간의 합을 최소로 만들 수는 없다.

줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때,
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.

입력: 첫째 줄에 사람의 수 N, 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다.
출력: 첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.

풀이
그리디 알고리즘과 간단한 정렬을 통하여 문제를 풀 수 있다.

```python
n = int(input())
line = list(map(int,input().split()))

line.sort()
```
먼저 문제에서 N(사람의 수)을 입력받고, P(인출시 걸리는 시간)를 입력받는다.
P의 경우에는 가장 적은 시간부터 차례로 더해주는 형식이므로 배열을 가장 적은 수부터 오도록 오름차순 정렬한다.

```python
line_sum = 0
for i in range(n):
    line_sum += sum(line[:i+1])

print(line_sum)
```
결과값을 출력해줄 변수를 초기화하고, 반복문을 이용해서 순차적으로 더해준다.
1번째 반복문에서는 1번만, 2번째 반복분부터는 해당 차례 사람과 앞사람의 값을 더해주어야 하므로
line[:i+1]을 통해 배열의 첫번째 요소와 그다음 요소를 더해주도록 한다.
'''

n = int(input())
line = list(map(int,input().split()))


line.sort()

line_sum = 0
for i in range(n):
    line_sum += sum(line[:i+1])

print(line_sum)
