# 2839 설탕 배달
 
```해당 문제는 설탕을 정확하게 N킬로그램을 배달해야 하는 문제.
3kg 봉지와 5kg 봉지를 입력한 설탕값에 정확히 나누어 떨어지도록 봉지 갯수를 구성해야 한다
입력값은 3 <= N <= 5000.
```

while 문에서 입력받는 값(설탕 무게)은 n >= 0보다 크도록 설정하였다.
입력받은 값이 0 이하면 봉지가 필요 없을 뿐더러 n = 0이 될 때, 5로 나눈 나머지도 0이므로 if문 내부를 출력하고 탈출한다.
n % 5인 이유는 나머지가 0이면 5의 배수이므로, 5의 배수일때는 5kg의 봉지만 가져가면 되므로
5로 나눈 몫을 반환하고 while문을 탈출한다.
n -= 3인 이유는 봉지가 초과하거나 모자르면 안되고 딱 맞게 봉지를 필요한 만큼 가져가야 하므로
n-3을 하여 봉지의 갯수를 하나씩 추가하고 while문을 반복한다.
n-3을 했을 때 봉지가 5의 배수가 되면 이전 봉지의 갯수와 5kg봉지의 갯수를 더해서 출력하도록 한다.
n-3을 했을 때 봉지가 5의 배수가 안된다면 3kg의 봉지만 필요한 것이므로 하나씩 추가한다.
정확하게 N킬로그램을 만들 수 없다면 -1을 출력하도록 하라고 문제에서 제시하였으므로
else문에는 -1을 출력하도록 설정한다.
예시로 4와 같이 나누어 떨어지지 않는 수가 나온다면, 
n-3 -> n = 1
n-3 -> n = -2
n이 -2일 경우를 수행하므로 else문의 -1을 출력한다.