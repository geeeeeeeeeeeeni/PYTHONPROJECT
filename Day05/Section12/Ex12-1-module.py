'''
모듈(module)
    언제나 변수나 함수 또는
    클래스를 모아 높은 파일을 모듈이라고 한다.
    파이썬 파일(.py) 이다.

모듈 사용법
import 모듈명
'''

import converter

miles = converter.kilometer_to_miles(150)
print('150km+{}miles'.format(miles))

pounds = converter.gram_to_pounds(1000)
print('1000g={}pounds'.format(pounds))