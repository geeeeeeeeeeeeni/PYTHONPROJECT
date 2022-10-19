'''
튜플
    단일변수에 여러항목을 저장하는데 사용된다.
    순사가 있고 변경할 수 없는 List
    둥근괄호()로 작성된다.
'''

#튜플 길이 len()
thistuple=("피카츄","라이츄","파이리","꼬부기")
print(len(thistuple))

#항목 가져오기
thistuple=("피카츄","라이츄","파이리","꼬부기")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])

#튜플값 변경 방법
# -> 튜플 자체에서는 변경 안됩니다.
# 그래서 list로 바꿔서 변경해줘야해요
#cast는 데이터 형 변환 함수

thistuple=("피카츄","라이츄","파이리","꼬부기")
thiscast = list(thistuple)
thiscast[1]="잠만보"
thistuple=tuple(thiscast)
print(thistuple)

#튜플 압축풀기
thistuple=("피카츄","라이츄","파이리","꼬부기")
(p1,p2,p3,p4) = thistuple

print(p1)
print(p2)
print(p3)
print(p4)
print(type(p1))


# 두개 튜플 조인
thistuple1=("피카츄","라이츄","파이리","꼬부기")
thistuple2=("버터플","야도란","피존투","또가스")

thistuple3 =thistuple1 + thistuple2
print(thistuple3)


