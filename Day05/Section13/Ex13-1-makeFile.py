'''
파일 입출력(I/O - input/output)
    입력(input) 기존파일 읽어들이는 것
    출력(output) 파일 생성, 내용 추가를 말한다.

    **실행 했던 것들은 반드시 file.close()로 닫아줘야함
'''

file = open('myFile.txt','wt')
print('myFile.txt 파일이 생성되었습니다')
file.close()

#with 문 - 자동으로 close()를 해준다
with open('myFile.txt','wt'):
    print('myFile.txt 파일이 생성되었습니다')