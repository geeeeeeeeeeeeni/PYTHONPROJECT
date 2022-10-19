'''

for 와 range 함수

    range(a, b)  -> a 부터 b-1까지
    range(a) -> a-1까지

'''

dan = int(input('출력할 구구단을 입력하세요 >>> '))

for n in range(1, 10):
    print('{} x {} = {}'.format(dan, n, dan * n))