'''

★☆★☆★조건문★☆★☆★

    특정 조건을 만족하는지 여부에 따라 실행하는 코드가 달라져야 할 때 사용
    들여쓰기를 사용하여 코드의 범위 정의 (띄여쓰기 하면 오류남)

    if(조건식)
    if(조건식) else
    if(조건식) elif (조건식2) else


'''

#if(조건식), ture면 값이 나옴

a = 7
b = 100

if b > a :
    print ("b는 a보다 크다")

#if(조건식) else : 참이면 1번째 조건, 거짓이면 2번째 조건으로 값을 출력

a = 7
b = 4
if b >= a :
    print("b는 a보다 크거나 같다")
else:
    print("b는 a보다 작다")

#if(조건식1) elif(조건식2) else

a = 20
b = 3

if b > a:
    print("b는 a보다 크다")
elif a == b :
    print("a와 b는 같다")
else:
    print("a는 b보다 크다")