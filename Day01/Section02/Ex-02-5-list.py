'''
List -> 자주 사용함
    단일 변수에 여러 항목을 저장하는데 사용된다.
    List 항목은 순서가 지정되고 변경 가능하며 중복 값을 허용
    List에는 다양한 데이터 유형이 포함될 수 있다.

 alt+shift 하고 방향키 하면 줄 옮길 수 있음

'''

thislist = ["피카츄","라이츄","파이리","꼬부기"]
print(thislist)
print(thislist[0])

# List 길이 알아보기 - 데이터가 얼마나 있는지 잘 모르기 때문에 확인하기 위해
thislist = ["피카츄","라이츄","파이리","꼬부기"]
print(len(thislist))


# List 데이터 유형
list1 = ["피카츄","라이츄","파이리","꼬부기"]
list2 = [1, 2, 3, 5]
list3 = [True, False, False]

# 다양한 유형 포함 가능
list4 = ["abc", 34, False, 40]


# 항목 접근
thislist = ["피카츄","라이츄","파이리","꼬부기"]
print(thislist[1])

# 변경
thislist = ["피카츄","라이츄","파이리","꼬부기"]
thislist[1] = "잠만보"
print(thislist)

#일부 변경 (마지막 인덱스 번호는 포험이 되지 않아요.)
thislist = ["피카츄","라이츄","파이리","꼬부기","버터플", "야도란"]
thislist[1:3] = ["울먹이", "메타몽"]
print(thislist)

#변경하는 인덱스 개수가 맞지 않아도 변경 된다. 전체를 하나로 바꾼다고 생각..
thislist = ["피카츄","라이츄","파이리","꼬부기","버터플", "야도란"]
thislist[1:3] = ["울먹이"]
print(thislist)

#항목 추가

thislist = ["피카츄","라이츄","파이리"]
thislist.append("꼬부기")
print(thislist)

#항목 추가 지정된 인덱스로 추가
thislist = ["피카츄","라이츄","파이리"]
thislist.insert(1,"잠만보")
print(thislist)

#항목 값으로 제거
thislist = ["피카츄","라이츄","파이리"]
thislist.remove("라이츄")
print(thislist)

#항목 지정된 인덱스로 제거
thislist = ["피카츄","라이츄","파이리"]
thislist.pop(2)
print(thislist)

#마지막 항목을 제거
thislist = ["피카츄","라이츄","파이리"]
thislist.pop()
print(thislist)

#객체 삭제
# del thislist
# print(thislist)

#목록 삭제(안에 있는 인덱스 삭제)
thislist = ["피카츄","라이츄","파이리"]
thislist.clear()
print(thislist)