file = open('hello.txt', 'at')

file.write('Hello\n')
file.write('Nice to meet you\n')
print('hello.txt 파일에 새로운 내용이 추가 되었습니다.')
file.close()

'''
at가 추가의 뜻
wt로 하면 그냥 다 지워지고 다시 써짐
'''