'''

복합 대입연산자

    +=
        ex) x += 3과  x = x + 3과 같다

    -=
        ex) x -= 3과  x = x - 3과 같다

'''

piggy_bank = 0
money = 10000
piggy_bank += money

print('저금통에 용돈 {}원을 넣었습니다.'.format(money))
print('지금 저금통에 {}원이 있습니다.'.format(piggy_bank))

snack = 2000
piggy_bank -= snack

print('저금통에서 스택 구입비 {}원 소비 하였습니다.'.format(snack))
print('지금 저금통에는 {}원 남았습니다.'.format(piggy_bank))