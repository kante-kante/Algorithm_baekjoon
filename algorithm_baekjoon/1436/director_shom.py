'''
1436 - 영화감독 숌

666은 종말을 나타내는 숫자라고 한다. 따라서, 많은 블록버스터 영화에서는 666이 들어간 제목을 많이 사용.
다른 영화감독들은 1,(제목) 2,(제목) 등과 같이 이름을 지었지만 숌은 다르게 만들기로 했다

종말의 숫자란 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수를 말한다.
제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666,.. 과 같다.

따라서, 숌은 첫 번째 영화의 제목은 세상의 종말 666, 두번째 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다.
일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.

숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오.

입력: 숫자 N이 주어진다. N은 10,000보다 작거나 같은 자연수
출력: 첫째 줄에 N번째 영화의 제목에 들어간 수를 출력한다.

풀이:
처음 반복문을 for문에 range를 지정하여 반복하려 하였으나 range에 값을 지정할 수 없음.
단순히 666 앞에 count를 증가시켜 숫자만 바꾸려 하였으나 N번째로 작은 종말의 숫자를 선택해야 하므로
해당 방법도 제외.

결국 숫자를 하나 하나 늘려주며 count의 값과 입력 값이 일치할 때, 결과값을 출력하도록 구성하였다.

먼저 N은 10000보다 작은 자연수를 입력받는다.
첫 시작인 number에는 666으로 초기화해주고, count도 0으로 초기화해준다.

반복문에서, 첫번째 조건문을 확인하면
number에 '666'이라는 문자열이 포함되어있으면 카운트를 하나씩 증가시킨다.(count == N)

두번째 조건문은 입력한 숫자와 카운트(666이 포함될때마다 하나씩 증가)값이 동일하면
number를 출력하고 반복문을 탈출한다.

브루트 포스 알고리즘인 이유는 '666'이라는 값이 포함되어있지 않으면 number의 값을
하나씩 계속 더해주며 다음 666이 나올때 까지 찾는 방식이기 때문에 해당 알고리즘이 왜 브루트 포스 알고리즘인지 알 수 있다.
'''

N = int(input())
number = 666
count = 0

while True:
    if '666' in str(number):
        count+=1
    if count == N:
        print(number)
        break

    number+=1