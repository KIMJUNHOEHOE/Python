# 객체는 Class의 구조를 가지면서, 메모리 상에 올라가 있는 것을 객체라 함
# 객체는 메모리 상에 올라가 있는 것(구조라고 함), 인스턴스는 메모리 상에 올라가 있는 구조 안에 값을 채워나가는 과정

# class MyClass:
#     name = '희영'
#
#     def sayHello(self): # 클래스 안에 def를 사용할 때는 self를 써야함.
#         hello = "Hello, " + self.name + "\t It's Good day !"
#         return hello
#
#
# myClass = MyClass()
# obj_name = myClass.name # 클래스.variable or 클래스.def
# obj_method = myClass.sayHello()
#
# print('Object name   :', obj_name)
# print('Object method :', obj_method)

# 클래스 초기화 함수, __init__() 재정의
class MyClass:

    name = None
    def __init__(self, name='준수'):     # 초기화 함수 재정의, default값 : 준수, class 생성 시 같이 실행 됨
        self.name = name

    def sayHello(self):
        hello = "Hello, " + self.name + "\t It's Good day !"
        print(hello)

# 객체 생성, 인스턴스화
myClass = MyClass() # 객체 생성 시 초기화 안 함
myClass.sayHello()
myClass = MyClass('채영') # 객체 생성 시 초기화
myClass.sayHello()