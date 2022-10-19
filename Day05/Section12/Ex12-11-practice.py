import random
import time

pot = [n for n in range(1, 46)]
jackpot = []

for n in range(1, 7):
    random.shuffle(pot)  #1~45 순서를 섞음
    pick = pot.pop()   #pot에서 나온 숫자는 지움
    print('{}번째 당첨번호는 {}입니다.'.format(n, pick))
    jackpot.append(pick) #그리고 여기에 추가
    time.sleep(2)

jackpot.sort() #sort 정렬하는 함수 -> 숫자 작은것 부터 큰 것으로 정리
print('이번 당첨번호는 {} 입니다.'.format(jackpot))