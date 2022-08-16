# a = 10
# print( a )
#
# import keyword
# print( keyword.kwlist )
# print( len( keyword.kwlist ) )

print( type( 10 ) ) #int 출력
print( type( 10.5 ) ) #float 출력
print( type( "ABC" ) ) # " ' 둘다 사용가능 
print( type( 'ABC' ) )
print( type( 10 + 10j ) )
print( type( 1234567890123456789 ) ) #정수의 범위를 넘어가도 int로 출력된다
print( type( 5/2 ) )

# a =10, b=20
a, b = 10, 20

# 교환
c = 0
c = a
a = b
b = c
print( a,b )
a, b = b, a
print( a, b)
del a,b
# print( a, b )

print( "우리나라 \
대한민국" ) #여러줄 사용시 \를 사용하면 한줄로 인식함

a = """
    우리나라
    대한민국
""" #여러 줄에 걸친 문자열을 표현
print (a) 

# 강제 형변환
print( type( int(10.5) ) ) #int로 강제 형변환
print( type( float( 10 ) ) ) #float로 강제 형변환
# print( type( int ("ABC" ) ) ) # 문자열을 바꾸는것은 에러
print( type( int( "123" ) ) )
print( type( str( 123 ) ) )

# 진수변환
print( int( "1111", 2 ) ) #2진수값으로 표현
print( int( "ff", 16 ) ) #255

print( oct( 20 ) )
print( hex( 20 ) )
print( bin( 20 ) ) #0b10100 b는 바이너리

print( "ABC", "DEF" )
print( "ABC", "DEF" )
print( "ABC", str( 10 ) )
print( "{0}{1}".format( "ABC", "DEF" ) )
print( "{1}{0}".format( "ABC", "DEF" ) )
print( "{0:10s}{1:10s}".format( "ABC", "DEF" ) ) #10자리를 잡고 왼쪽부터 채움
print( "{0:.2f}".format( 1234.5678 ) ) #소숫점 이하 2자리까지 출력 둘째자리에서 반올림 함

# 연산자
a = 10
print( a ** 2 ) #a의 제곱은 100
print( 5.0 / 2 )
print( 5.0 / 2 )
print( 5 // 2 )
print( 5.0 // 2 )

print( 0 and 0 ) # 0
print( 0 and 1 ) # 0
print( 1 and 0 ) # 0
print( 1 and 1 ) # 1

print( False or False )
print( False or True )
print( True or False )
print( True or True )

print()
print( "H" in "Hello" )
print( "H" not in "Hello" )

a = "Hello"
b = "Hello"
print( a is b ) # 주소
print( a == b ) # 내용
a += "Python!"
b += "Python!"
print( a is b )
print( a == b )

print("=======================================")

print(" 산술 대입연산자 ")
a = 10
a += 10; print( a )
a -= 10; print( a )
a *= 10; print( a )
a /= 10; print( a )
a %= 10; print( a )

print(" 쉬프트 대입연산자 ")
a = 20
a <<= 2; print( a )
a >>= 2; print( a )

print("비트 논리 대입연산자")
a = 10
a &= 10; print( a )
a |= 10; print( a )
a ^= 10; print( a )

#파이썬은 삼항연산자가 없다.


























  




























