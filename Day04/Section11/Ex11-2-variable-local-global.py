'''
지역변수(local)
    함수 내부 선언
    함수 내부에서만 사용 사능

전역변수(global)
    함수 외부 선언
    함수 내부 외부 모두 사용 가능
'''

gVar = '전역'


def globalAndLocal():
    lVar = '지역'
    print(gVar, '변수 입니다.')  # 전역변수 참조만 하고 있다
    print(lVar, '변수 입니다.')


globalAndLocal()

gVar = '전역'


def globalAndLocal():
    lVar = '지역'
    gVar = '변경된 전역이 아닌 새로운 지역'
    print(gVar, '변수 입니다.')
    print(lVar, '변수 입니다.')


globalAndLocal()
print(gVar)  ##def 안에 있는 값으로 출력이 안댐.. 되게 하려면?

print()

# 전역변수 선언
total = 0 #정수형으로 선언


def gift(dic, who, money): ##(안에 매개변수)
    global total  # 전역변수 total를 사용할거야
    total += money  #합산을 할거에요
    dic[who] = money #dic에다가 key와 value값을 추가
      #여기서 dic 안쓰고 걍 wedding으로 써도 댐
      #근데 이렇게 하는게 원래 맞는거야. 그런 뭐... 코스가 있음
#return이 없는데 왜 반환이 될까?


wedding = {}   #빈 dic 함수를 만들어놓음 --> 얘도 전역변수임
gift(wedding, '영희', 5) # wedding이라는 dic 함수에 {'영희', 5}값을 추가하는 중
gift(wedding, '철수', 3)  #하나씩 추가되는중
gift(wedding, '이모', 10)
print('축의금 명단: {}'.format(wedding))  #전체 명단이 나오고
print('전체 축의금: {}'.format(total))  # total 정의해놨던 값이 나옴
