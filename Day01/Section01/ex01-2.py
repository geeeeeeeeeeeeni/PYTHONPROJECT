'''
%d, %s, %c를 활용하여 print 문으로 데이터를 출력하는 법.

    %d : 숫자 데이터
    %f : 실수 데이터
    %o : 8진수 데이터
    %x : 16진수 데이터
    %s : 문자열 데이터
    %c : 문자 하나 데이터
'''


print("올해는 %d년 입니다." % 2022)
print("올해는 %d년, 내년은 %d년 입니다." %(2022,2023))
print("나는 %s을 공부합니다." %"파이썬")
print("나는 %s과 %s를 공부합니다." %('파이썬','자바'))
print("Python은 %c로 시작합니다." % 'P')
print("Python은 %c로 시작하고, %c로 끝납니다." %('P','n'))