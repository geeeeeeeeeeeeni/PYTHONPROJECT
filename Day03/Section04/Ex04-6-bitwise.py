'''

비트연산자

    어떤 변수의 값을 0과 1의 조합인 2진수,
    즉 비트로 변환한 뒤에 비트 단위로 연산 수행

    1. &(AND) : 입력이 모두 1이면 1, 아니면 0
    2. |(OR) : 입력 중 하나라도 1 이면 1, 아니면 0
    3. ^(XOR) : 입력이 서로 다르면 1, 아니면 0
    4. ~(NOT) : 입력이 0이면 1, 입력이 1이면 0 (
    5. <<(왼쪽 SHIFT) : 비트 단위로 왼쪽으로 N비트 이동하며 2의 N 거듭제곱만큼 곱셈
    6. >>(오른쪽 SHIFT) : 비트 단위로 오른쪽으로 N비트 이동하며 2의 N 거듭제곱만큼 나눗셈

'''

a = 10
b = 70

print(bin(a))
print(bin(b))


print('a & b : {}'.format(a & b))
print('a | b : {}'.format(a | b))
print('a ^ b : {}'.format(a ^ b))
print('~a : {}'.format(~a))
print('a << b : {}'.format(a << b))
print('a >> b : {}'.format(a >> b))