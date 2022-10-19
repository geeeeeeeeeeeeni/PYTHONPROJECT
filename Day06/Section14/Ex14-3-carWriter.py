import  csv

#첫번째 방법
'''
with open('차량관리.csv', 'w') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25러1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28러1234', '2020-10-20,14:20'])
print('차량관리.csv 파일이 생성되었습니다.')
'''

#두번째 방법
'''
with open('차량관리.csv', 'w', newline='')  as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25러1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28러1234', '2020-10-20,14:20'])
print('차량관리.csv 파일이 생성되었습니다.')
'''

#마지막 방법

with open('차량관리.csv', 'w', newline='')  as file:
    csv_maker = csv.writer(file, delimiter=',', quotechar='"')
    csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25러1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28러1234', '2020-10-20,14:20'])
print('차량관리.csv 파일이 생성되었습니다.')