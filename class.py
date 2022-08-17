# 클래스

# *캡슐화 *상속 *다형성
#파이썬에서 캡슐화는 큰 의미가 없다.
# 자바는 상속과 다형성이 많이 쓰인다 자바는 모든 클래스가 상속
# 파이썬은 자료형 개념이 없어서 다형성 구현이 불가능하다

# private 클래스 안에서만 적용
__a = 10     # 일반변수
def getA() : # 일반함수
    return __a
print( getA() )
print("__a : ", __a )

class P : # 클래스 이름뒤에 괄호가 안들어감
    __a = 10    # private
    b = 20
    def getA( self ):
        return self.__a
    def getB( self ):
        return self.b # self를 반드시 명시 해야함.
p = P() # 객체 생성
# print( p.__a ) # private이라서 접근이 안됨
print( p.b )
print( p.getA() )
print( p._P__a )    # private 멤버 접근 방법을 제공,private멤버를 외부에서 접근하기 때문에 완벽한 캡슐화는 불가능 하다
# p.__a = 100
#p.setA( 100 )
#print( p.getA() )

print()
# 캡슐화
class Person : 
    __name =""
    __age = 0
    __height = 0.0
    def setName(self, name):
        if len( name ) > 10 or name == "" :
            print( "이름을 바르게 입력하세요" )
        else :
            self.__name = name
    def setAge(self, age):
        if age < 1 or age > 140 :
            print( "나이를 바르게 입력하세요" )
        else :
            self.__age = age
    def setHeight(self, height):
        if height < 40 or height > 200 :
            print( "키를 바르게 입력하세요" )
        else :
            self.__height = height
    def getName(self) :
        return self.__name
    def getAge(self):
        return self.__age
    def getHeight(self):
        return self.__height

kim = Person()
kim.setName( "홍길동홍길동" )
kim.setAge( 150 )
kim.setHeight( 300 )
print( "이름 : ", kim.getName() )
print( "나이 : ", kim.getAge() )
print( "키 : ", kim.getHeight() )

lee = Person()
lee.setName( "이순신" )
lee.setAge( 30 )
lee.setHeight( 180 )

print( "이름 : ", lee.getName() )
print( "나이 : ", lee.getAge() )
print( "키 : ", lee.getHeight() )

# 생성자 / 소멸자
# C++        Person() / ~Person()
# Java       Person()
# Python     __init__ / __del__

#파이썬은 생성자를 이용하면 변수를 만들 필요가 없다.

# class User :
#     def __init__(self, name= "",age=0,tel=""):
#         print( "생성자" )
#         self.name = name
#         self.age = age
#         self.tel = tel
#     def getName(self) :
#         return self.name
#     def getAge(self):
#         return self.age
#     def getTel(self):
#         return self.tel
#     def __del__(self):
#         print( "소멸자" )
# kim = User()
# lee = User("이순신")
# hong = User( age=20, tel="1111-2222" )
#객체가 생성될때 생성자 호출
#객체가 사라질 때 소멸자 호출 
# 객체마다 호출됨!
# print( "이름 : ", hong.getName() )
# print( "나이 : ", hong.getAge() )
# print( "전화번호 : ", hong.getTel() )

#static
# 모든 객체가 공유
# 메모리 영역중에 static 영역에 할당
# 메모리는 하나만 할당된다.
# 먼저할당 된다.
# 파이썬은 static 을 명시할 필요가 없다.

# print()
# class Member :
#     name = "홍길동"        # 멤버변수 클래스변수 static변수
#     count = 0 #static 
#     def __init__(self, age=0, cnt=0 ): #지역변수
#         self.age = age
#         self.cnt = cnt
#         Member.count += 1
#         self.cnt += 1;
#     def getcnt(self):
#         return self.cnt
#     def getCount(self):
#         return Member.count
#
# print( Member.name ) # static은 객체생성 안해도 사용할 수 있다
# # print( Member.age )
#
# Member.name = "이순신"
#
# lee = Member()
# print( lee.name )
# print( lee.getCount )
# print( lee.getcnt() )
#
# hong = Member()
# print( hong.name) 
# print( hong.getCount )
# print( hong.getcnt() )
#
#
# park = Member()
# print( park.name )
# print( park.getCount )
# print( park.getcnt() )

#--------------------------

class Customer :
    name = "홍길동"
    def setName(self, name ) :
        self.name = name
    def getName(self) :
        return self.name
    @staticmethod #static 어노테이션 사용가능
    def dispName(): # static은 공유하는 메서드라서 self를 안쓴다
        return Customer.name
    #dispName = staticmethod( dispName)# 이렇게하면 static메서드가 된다

kim = Customer()
kim.setName( "김유신" )
print( kim.getName() )          # 김유신
print( Customer.dispName() )    # 홍길동

print()
class Car :
    cc = "2000cc"
    @staticmethod
    def getStatic() :
        return Car()
    @classmethod #매개변수 1개를 줘야함
    def getClass(cls) :     # cls 클래스를 매개변수로 전달
        return cls()    #매개변수로 받은것을 객체로 만듬
    def getcc(self) :
        return self.cc
class Truck( Car ) :
    cc = "3000cc"
a = Car.getStatic()     # Car
b = Car.getClass()      # Car
print( a.getcc() )      # 2000cc
print( b.getcc() )      # 2000cc #car클래스로 만든 객체

c = Truck.getStatic()
d = Truck.getClass()    #truck클래스 객체 3000호출
print( c.getcc() )      # 2000cc
print( d.getcc() )      # 2000cc

print()
# 상속
# 코드 재활용
# 부모 것은 내 것

# class Animal :
#     def __init__(self, name="" ):
#         self.name = name
#         print( "Animal 생성자")
#     def getName(self) :
#         return self.name
#
# class Cat(Animal) :
#     def __init__(self,name=""):
#         Animal.__init__(self, name)
#         print( "Cat 생성자" )
# class Dog(Animal) :
#     None
# dog = Dog( "멍멍이" )
# print( dog.getName() )
# cat = Cat( "나비" )
# print( cat.getName() )

# 다중상속
# C++         구현 O 사용 X
# Java        구현 X 사용 O (인터페이스)    
# Python      구현 O 사용 O 

class Animal :
    def __init__(self, name ):
        self.name = name
    def getName(self) :
        return self.name
class Pet :
    def __init__(self, kind ):
        self.kind = kind
    def getKind(self):
        return self.kind
class Dog( Animal, Pet ) :
    def __init__(self, name, kind, color ) :
        Animal.__init__( self, name )
        Pet.__init__(self, kind )
        self.color = color
    def getColor(self):
        return self.color
    def getName(self):
        return "이름 : "+self.name
    def getKind(self):
        return "품종 : "+self.kind
    
dog = Dog( "멍멍이", "잡종", "누런색" )
print( dog.getName() )
print( dog.getKind() )
print( dog.getColor() )

# 다형성
class Bread :
    def __init__(self, name="" ) :
        self.name = name
    def getName(self) :
        return "Bread : " + self.name
    @classmethod
    def getClass(cls, msg) : #넘겨받은 클래스로 객체 만듬
        return cls( msg )
class Toast( Bread ) :
    def getName(self) :
        return "Toast : " + self.name
class Cake( Bread ) :
    def getName(self) :
        return "Cake : " + self.name
class Redbean( Bread ) :
    def getName( self ) :
        return "Redbean : " + self.name

# Bread bread = new Toast(); bread.getName();
# Bread bread = new Cake(); bread.getName();
# Bread bread = new Redbean(); bread.getName();
toast = Toast( "토스트" )
print( toast.getName() )
cake = Cake( "케이크" )
print( cake.getName() )
redbean = Redbean( "팥빵" )
print( redbean.getName() )
print()

toast = Toast.getClass( "토스트" )
print( toast.getName() )
cake = Cake.getClass( "케이크" )
print( cake.getName() )
redbean = Redbean.getClass( "팥빵" )
print( redbean.getName() )

# @property / property()
class Gamer :
    __name = ""
    __age = 0
    @property
    def setName(self, name) :
        self.__name = name
    @property
    def setAge(self, age) :
        self.__age = age
    @property
    def getName(self) :
        return self.__name
    @property
    def getAge(self) :
        return self.__age
    #name = property( getName, setName )
    #age = property( getAge, setAge )
gamer = Gamer()
# gamer.setName( "홍길동" )
# gamer.setAge( 30 )
# print( gamer.getName() )
# print( gamer.getAge() )

# print( gamer.__name )
gamer.name = "이순신" 
gamer.age = 40
print( gamer.name )
print( gamer.age )































    