# overriding

#  Developer 부모 클래스 선언
class Developer:
    def __init__(self, name): ## __함수__ : 파이썬 내부함수를 의미함
        self.name = name

    def coding(self):
        print('%s는 코딩을 좋아합니다.' % self.name)
        print(self.name + ' is developer!!')


# PythonDeveloper 자식 클래스 선언
class PythonDeveloper(Developer):
    def coding(self):
        print('%s는 Python 코딩을 좋아합니다.' % self.name)


# JavaDeveloper 자식 클래스 선언
class JavaDeveloper(Developer):
    def coding(self):
        print('%s는 JAVA 코딩을 좋아합니다.' % self.name)


# CPPDeveloper 자식 클래스 선언
class CPPDeveloper(Developer):
    def coding(self):
        print('%s는 C++ 코딩을 좋아합니다.' % self.name)