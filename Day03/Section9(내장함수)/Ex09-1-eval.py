'''

eval
    매개변수로 받은 espression(=식)을 문자열로 받아서, 실행하는 함수
    숫자식이 아닌 그냥 문자를 쓰면 오류남

'''

expr = input('계산식을 입력하세요 >>> ')
result = eval(expr)
print(expr + '=' + str(result))
