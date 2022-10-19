'''
메소드(method) 란

    특정객체가 가지고 있느 함수를 의미한다.

    식>>
    객체명. 메소드명(매개변수)
'''

#String 객체 format 메소드
print("10자리 폭 왼 쪽 정렬 '{:<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 '{:>10d}'".format(123))
print("10자리 폭 가운데 정렬 '{:^10d}'".format(123))
print()
print("10자리 폭 왼 쪽 정렬 채움문자'{:*<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움문자'{:*>10d}'".format(123))
print("10자리 폭 가운데 정렬 채움문자'{:*^10d}'".format(123))

#count() 메소드
s = '내가 그린 기린 그림은 목이 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다.'
result = s.count('기린')
print(result)

s = 'best of best'
result = s.count('best', 5)
print(result)

s = 'best of best of best'
result = s.count('best', -15)
print(result)

#find() 메소드 위치한 인덱스 번호 반환
s = 'apple'
result = s.find('p')
print(result)

#없는값 find -1
s = 'apple'
result = s.find('z')
print(result)


s = 'best of best'
result = s.find('best', 5)
print(result)

#없는값 find -1
s = 'best of best'
result = s.find('best', -7)
print(result)

#index() find() 메소드와 같지만 문자열이 존재하지 않을 경우 에러발생!
#=>에러를 남겨놔야 할 때...(?) 관리자가 24시간 볼 수 없으니까 ..
s = 'apple'
result = s.index('p')
print(result)

s = 'apple'
result = s.index('z')
print(result)