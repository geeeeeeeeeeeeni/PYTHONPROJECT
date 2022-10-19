'''
mutable
    메모리 값을 변경 가능
    리스트(list), 세트(set), 딕션어리(dict)
'''

me=[1,2,3]
print(id(me))
me.append(4)
print(id(me))

'''
immutable
    메모리 값 변경 불가, 수정시(?) 새로운 메모리 영역이 할당 된다.
    정수(int), 실수(float), 문자열(str), 튜플(tuple)
'''

me = 10
print(id(10))
me +=1
print(id(me))

