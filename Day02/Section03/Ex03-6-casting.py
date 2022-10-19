'''
casting
    변수에 유형을 지정하려는 경우 캐스팅으로 가능.
'''

#정수형
x=int(1)
print(x)
y=int(2.8)
print(y)
z=int("3")
print(z)
print(type(z))

#실수형
x=float(1)
print(x)
z=float("3")
print(z)


#문자열형
x = str(1)
print(x)
print(type(x))

#문자열로 숫자를 지정했기 때문에 더하지 않고 붙여서 출력!
x = str(1)
y = str(2)
print(x)
print(type(x))
print(x+y)