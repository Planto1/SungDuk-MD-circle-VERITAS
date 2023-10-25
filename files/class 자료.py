# 객체 : 결과값을 받는 변수
# 인스턴스 : 클래스로 만든 객체
# 객체와 인스턴스의 관계 : 객체 a 는 클래스의 인스턴스 이다.
# 매소드 : 클래스 안에 있는 함수

class class_name():
    def func(self,var): # 함수 func는 메소드
        return var

a = class_name() # a는 클래스 class_name을 받는 변수 -> 객체이다
a.func(5) #

class mini_calc:

    # 초기화함수(__init__)으로 계산값 받아오기
    def __init__(self):

        # 예외처리(나중에 알려드림)
        try:
            num1,num2 = input("<num1> <num2>\n").split()
            self.num1 = int(num1)
            self.num2 = int(num2)

        except:
            print("값을 제대로 입력해주세요.")

    # 사칙연산 함수 + - * /

    def add(self): # + 더하기
        return (self.num1 + self.num2)

    def sub(self): # - 빼기
        return (self.num1 - self.num2)

    def mul(self): # * 곱하기
        return (self.num1 * self.num2)

    def div(self): # / 나누기
        return (self.num1 / self.num2)


calc = mini_calc() #
print(calc.div()) # calc(mini_calc() class) 의 div()[나누기] 선언