'''
set
    순서가 없다
    변경할 수 없다
    인덱싱되지 않는 컬렉션(여러 자료를 묶어서 처리하는...함수? 자료?)
    중괄호 사용{}
'''

thisset = {"피카츄", "라이츄", "파이리"}
#실행할 때 마다 순서가 변경
print(thisset)


#항목 가져오기 -> for x in thisset : 밑에 들여쓰기 된 함수까지만 for문으로 인식함
thisset = {"피카츄", "라이츄", "파이리"}
for x in thisset :
    print(x)

# 내가 찾는 값이 있는지 확인하기
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset)
#->"피카츄"라는 값이 있는지 보고 싶어


#항목 추가하기
thisset = {"피카츄", "라이츄", "파이리"}
thisset.add("꼬부기")
print("꼬부기" in thisset)

# 다른 Set의 항목 추가하기
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "버터플", "야도란"}
thisset1.update(thisset2)
pr int(thisset1)

# 똑같은 값을 쓰면 어떻게 될까?
# ->중복값은 제거해서 출력함
# ->중복값을 제거하려고 set을 쓰는 경우도 있어요
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "버터플", "피카츄"}
thisset1.update(thisset2)
print(thisset1)

#항목제거
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset)
#여기서 또 remove함수를 넣으면? - > 오류남
# thisset.remove("피카츄")
# print(thisset)

#이상한 값이 계속 넣어서 그 값들은 주기적으로 매일 삭제하고 싶을때 ㅡㅡ
thisset = {"피카츄", "라이츄", "파이리"}
thisset.discard("피카츄")
print(thisset)
#또 써도 오류 안남. 값이 없다고 오류 나면 안 되니까 이렇게 설정해놓음
thisset.discard("피카츄")
print(thisset)


#항목제거
thisset.pop()

#비우기
thisset.clear()
print(thisset)
