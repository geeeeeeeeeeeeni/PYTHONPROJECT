class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(C, B):
    pass #내부동작 필요하지 않고 빈 껍데기만 필요할 때 pass 사용

x = D()
x.greeting()
print(D.mro())