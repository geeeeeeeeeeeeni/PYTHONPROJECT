'''
사용자 함수
    사용자가 직접 만든 함수

정의방법
    def 함수이름(매개변수):
        본문
        :return 반환값
'''

#welcome() 함수정의  매개변수, 리턴 없이 사용
# **print 해서 어떻게 나오는지 확인하는게 조아용

def welcome():
    print('Hello Python')
    print('Nice to meet you')

welcome() # 함수호출

# 매개변수가 있는 함수

def introduce (name,age):
    print('내 이름은 {}이고, 나이는 {}살 입니다.'.format(name, age))

introduce('james',25) #함수호출하면서 프린트 된다.

#가변 매개변수 함수

def show(*args):
    for item in args:
        print(item)

show('python')
show('python','happy','birthday')

#반환(return)값이 있는 함수

def address():
    str = '우편번호 1234\n'
    str += '서울시 영등포구 여의도동'
    return str

result = address()
print(result)

#더하기 함수 매개변수 리턴 같이 있음

def plus(num1, num2):
    return num1 + num2

print(plus(1,2))


#옆으로 한 칸 이동

area = 0
def move():
    return area + 1

result = move()
print('유닛이 오른쪽으로 {}칸 이동했습니다.'.format(result))