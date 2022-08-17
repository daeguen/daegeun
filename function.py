# 함수 Function

"""
    C         일반함수, 멤버함수(클래스 내에 선언)
    반환형 함수명( 매개변수 ) {
        실행문;
        return;
    }

    멤버함수인 경우
    public : 
        반환형 함수명( 매개변수 ) {
            실행문;
            return;
        }
    JavaScript    일반함수, 멤버함수(클래스 내에 선언)
    function 함수명( 매개변수 ) { #반환형 없음.
        실행문;
        return;
    }
    
    함수명 = function( 매개변수) {
        실행문;
        return;
    }
    
    Java             멤버함수
    public 반환형 함수명( 매개변수 ) {
        실행문;
        return;
    }
    
   Python            일반함수, 멤버함수
   def 함수명( 매개변수 ) {
       실행문;
       return;
    }
    
    def 함수명( self, 매개변수 ) { #self는 this와 같음
        실행문
        return
    }
    
"""

# 함수 : 
# 반복되는 내용을 묶어서 처리
# 선언 구현 호출해서 사용
# 반드시 호출한 자리로 돌아온다
# 모든 함수는 return이 있다.
# return 하나뿐이다

# print( "Hello Python!!!" )
# print( "Hello Python!!!" )
# print( "Hello Python!!!" )

def hello() :                   #선언    함수를 알려준다    
    print( "Hello Python!!" )   #구현    함수가 할 일을 정의
    #return                     리턴이 있는데 생략되어있다
    #void는 리턴이 없는게 아니라 리턴값이 없는것이다.
    #생성자는 리턴이 없음 void조차 안쓴다 리턴쓰면 에러발생.
hello()                         #호출    함수를 사용한다
#함수는 반드시 호출을 해야 사용할 수 있다.

hello()
hello()

def max( a,b ) :
    if a > b :
        return a
    elif b > a :
        return b
    elif b == a :
        return "같다"
print( max( 5, 2) )

"""
    오버로드
    함수의 이름은 같고 매개변수 자료형이 다르거나 개수가 다르거나 순서가 다를 경우 다른 함수로 취급
    
    
    C            오버로드 X 매개변수 초기값 O
    int hap( int a, int b ) { return a+b }
    int hap( double a, double b ) { return a+b }

    int hap( int a=0, int b=0, int c=0 ) {}
    hap( 2, 5 )
    hap( 2, 5, 7 )
    
    Java            오버로드 O 초기값 X
    public int hap( int a, int b ) { return a + b }
    public int hap( double a, double b ) { return  a + b }
    
    public int hap( int ... args ) {
        for( a : args ) {
        }
    }

"""

def hap( a, b ) : # 변수는 같은 이름이면 덮어 쓰기가 되는데 
    return a + b  # 함수는 덮어 쓰기가 안된다. 즉, 오버로드 불가능
# def hap( c, d ) :
#     return c + d
print( hap( 5, 2 ) )
print( hap( 5.5, 2.7 ) )

def cha( a, b, c=0 ) :
    return a - b - c;
print( cha( 5, 3 ) ) 

#def gop( a, b=0, c ) : # 초기값을 주기 시작했으면 뒤에도 모두 줘야한다.
def gop( a, b=0, c=0):
    return a * b * c;  # 에러발생. 뒤에만 주던가 해야함.
print( gop( 2, 5 ) )
print( gop ( 2 ) )
# print( gop() ) # 값을 아예 안주면 안됨 

print("VarArgs")
# VarArgs
def avg( *args ) :          # Tuple
    print( type( args ) )
    sum = 0
    for a in args :
        sum += a
    print( sum / len( args ) )

avg( 1, 2, 3) #튜플 형식으로 출력
avg( 10, 20, 30, 40, 50 )

print("*args")
def sum( a, b, *args ) : #*args는 여러 인수를 받기 위함
# def sum( a, b, *args) :
# def sum( a, *args, b ) :    #에러
# sum( a, *args, *argss ) : 하나밖에 못쓰는데 두개 쓰면 에러
    print( a, b, args )
sum( 10, 20, 30, 40, 50 )

# 키워드 인수
def add( a, b, c=0 ):
    print( a+b+c )
add( 2, 5, 7 )
add( 2, 5 )
add( a=5, b=7 ) # 키워드 인수 가능 함수에 있는 매개변수 이름을 맞춰야 함
add( b=5, a=10 ) # 키워드 인수로 인하여 순서 바뀌어도 상관 없음.
add( 5, b=2, c=10 ) # b에 값을 넣었으니 c에도 값을 넣어야 출력됨
add( c=10, a=20, b=30 ) # 순서 바뀌어도 가능
add( 10, b=20 )
# add( a=10, 20 ) # x
# add( a=10 ) # x
# add( 10, c=20 ) # b가 값이 없으므로 x

# 키워드 인수 사전
def insert( a, **params ) :
    #print( type( params ) )
    print( a, end="" )
    for key, value in params.items() :
        print( key, value, end= " " )
print()

insert( 10, b=10 )
insert( 20, b=20, c=30 )
# insert( a=10, b=20, c=30 )
# insert( b=20, 10, c=30 ) #숫자를 맨앞에서 받기로 했기 때문에 에러
insert( b=20, c=30, a=10 )

print("params")

def hap1( a=10, *args, **params ) :
    print( "a : ", end=" " )
    for i in args :
        print( i, end=" " )
    for key, value in params.items() :
        print(key, value, end=" ")
    print()

hap1( 10, "A", "B", "C" )
hap1( 20, "A", "B", b=20, c=30 )
hap1( 10, b=20, c=30 )
hap1( 20, 30, 40, 50 )
hap1( b=20, c=30, d=40 )
# hap1( "A", "B", "C", a=20 )    

print("지역변수 / 전역변수")    
# 220817
#지역변수 / 전역변수
b = 10
b = 100
print( b )

a = 10                  # 전역변수    모든 영역에서 사용
def disp() :            # 지역변수,전역변수 사용가능 
    a = 100             # 지역변수    할당된 영역에서만 사용
    print( "a :", a )
    print( "b :", b )

    #global a            # 전역변수로 사용 (예약어)
    #print( "a :", a )
disp()

def disp1() :
    global a
    a = 1000 # global 선언했으므로 전역변수
    print( "a :", a )
    
    # a = 100 #전역변수
    # print( "a :", a )
disp1()
print( a )

def ha(a,b) :
    a=5
    b=2
    return a+b 
def ch(a,b) :
    a=5
    b=2
    return a-b 
def go(a,b) :
    a=5
    b=2
    return a*b 
def mo(a,b) :
    a=5
    b=2
    return a/b
print( ha(5,2) )
print( ch(5,2) )
print( go(5,2) )
print( mo(5,2) )    

# 내장함수
print( abs( 10 )) #절대값 구하는 함수
print( abs( -10 ))

print( all( [1,2,3] ) )
print( all( [1,2,0] ) )
print( any( [0, "", False] ) )
print( any( [1] ) )

print( dir() ) #현재 사용할 수 있는 함수 목록 출력
import sys
print( dir( sys ) ) #sys 모듈내에 선언된 속성들의 식별자 이름 목록

print( divmod( 7, 3 ) )
print( "1+2" )
print( eval( "1+2" ) )
#
a = 10
 #print( id( a ) )
 #print( id( 10 ) )
b = a 
 #print( id( b ) )

 # print( min( "python" ) )
 # print( max( "python" ) )
 # print( min( [1, 5, 3, 7, 9] ) ) # 열거형

 #print( pow( 4,2 ) )

m = [50, 10, 40, 30, 20]
#m.sort()
m = sorted( m )
print( m )
#
# print( list( zip( [1, 2, 3],[4, 5, 6] ) ) #객체 주소가 출력됨
# # 1,4 2,5 3,6으로 한쌍으로 묶는다. (각 인덱스 끼리 묶는다는 뜻).

print("람다함수")
# 람다함수            익명함수
def add1( a, b ) :
    return a+b
print( add1( 3, 7 ) )

add2 = lambda a, b : a+b
print( add2( 4, 9 ) )

print( (lambda a, b : a+b)( 5, 20 ) )

# filter( function, list )
def even( a ) :
    return a%2==0
print( even( 10 ) )

print( list( filter( even, range( 10 ) ) ) )
# 0-9까지 숫자 중에 true만 골라서 출력. 홀수가 true
print( list( filter( lambda x : a%2==0, range(10) ) ) )

# map( function, list)
print(" 대량의 데이터를 똑같이 처리하고 싶을 때 사용 ")
print( list( map( lambda x: x*2, range( 10 ) ) ) )

# reduce( function, list )
from functools import reduce
print( reduce( lambda x, y : x+y, range( 10 ) ) )











