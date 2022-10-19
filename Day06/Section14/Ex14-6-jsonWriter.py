#첫번째 실행
'''
import json
dict_list = [
    {
        'name': "james",
        'age':20,
        'spec':
        [
            175.5,
            70.5
        ]
    },
    {
        'name':'alice',
        'age':21,
        'spec':
        [
            168.5,
            60.5
        ]
    }
]

json_string = json.dumps(dict_list)

with open('dictlist.json', 'w') as file:
    file.write(json_string)

print('dictlist.json 파일이 생성되었습니다.')
'''


#두번째 실행

import json

dict_list = [
    {
        'name': "james",
        'age':20,
        'spec':
        [
            175.5,
            70.5
        ]
    },
    {
        'name':'alice',
        'age':21,
        'spec':
        [
            168.5,
            60.5
        ]
    }
]

json_string = json.dumps(dict_list, indent=2)

with open('dictlist.json', 'w') as file:
    file.write(json_string)

print('dictlist.json 파일이 생성되었습니다.')