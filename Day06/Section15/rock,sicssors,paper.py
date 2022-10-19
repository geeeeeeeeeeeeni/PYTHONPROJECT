import random

select = ['가위', '바위', '보']
computer = random.choice(select)
user = input('가위, 바위, 보 중에서 하나를 선택하세요>>')

while True:
    if user == '가위' and computer == "보" or user == '바위' and computer == "가위" or user == '보' and computer == "바위":
        print("이겼다")
    elif user == '가위' and computer == "가위" or user == '바위' and computer == "바위" or user == '보' and computer == "보":
        print("비겼다")
    else:
        print("졌다")
    break
