# 열거형 나열형

# 문자열
name = "홍길동"
age = 20
print( "name : " + name + " age : " + str(age) )
print()
print( "=" * 20 )
print( "name : %s age : %d" %(name, age) )
print( "name : {0} age : {1}".format( name, age ) )
print( "name : {name} age : {age}".format( name="홍길동", age= 30 ) )

a = "Hello"
print( "{0:10}".format( a ) ) 
print( "{0:<10}".format( a ) ) #< 왼쪽정렬
print( "{0:>10}".format( a ) ) #> 오른쪽정렬
print( "{0:^10}".format( a ) ) #^ 위쪽정렬
print( "{0:=^10}".format( a ) ) # 빈칸을 ==로 채움
print( "{0:-^10}".format( a ) ) # 빈칸을 --로 채움
print( "{0:x^10}".format( a ) ) # 빈칸을 x로 채움
print()
#문자열관련 함수
print("문자열관련 함수")
a = "Hello Python"
print( a.lower() )
print( a.upper() )
print( a.title() ) #모든 단어의 첫 문자만 대문자로 나머지는 소문자로 바꾼다
print( a.swapcase() ) #대문자로 바꿈
print( a.isupper() ) #모든 문자가 대문자이면 True 반환
print( a.count("o") ) #o가 포함된 갯수를 센다
print( a.find( "a") ) #a가 포함된 갯수를 센다 없으면 -1출력
#print( a.index( "a" ) ) #a가 없으면 에러발생
print( ",".join(a) ) #a에 ,를 하나씩 추가. 띄어쓰기도 데이터이기 때문에 포함된다
b = "     b    b    b    "
print( b.lstrip( " " ) ) #왼쪽의 공백을 지운다
print( b.rstrip( " " ) ) #오른쪽의 공백을 지운다
print( b.strip( " b") ) #양쪽의 공백을 지운다
print( a.replace( "o", "a" ) )
print( a.split() )
print( a.split( "o" ) )

c = "ABC123"
print( c.isalnum() ) # 알파벳 + 숫자
print( c.isalpha() ) # 알파벳
print( c.isidentifier() )
print( c.isdigit() ) #모든 문자가 숫자이면 true 반환
print( c.isnumeric() ) #모든 문자가 0에서 9까지의 숫자이면 true 반환.

print()
print( "0abc".isidentifier() )
print( " abc".isidentifier() )
print( "_abc".isidentifier() )
print( "a+bc".isidentifier() )
print( "a$b".isidentifier() )
print( "가나다".isidentifier() )

print()
print("인덱싱")
a = ("Hello Python")
#인덱싱
#   0   1   2   3   4   5   6   7   8   9   10  11  12
# | H | E | L | L | O |   | p | y | t | h | o | n | \0 |    #배열 리스트
print( a[0] )
print( a[11] )

# 슬라이싱
print( a[:] )
print( a[3:] )
print( a[:10] ) # end index -1 
print( a[2:10] )
print( a[:-1] ) 
print( a[:-2] )

print()
print("리스트 (인덱스가 자동으로 부여된다)")
#리스트 (인덱스가 자동으로 부여)
fruits = ["banana", "apple", "orange", "pear", "grape"]
print( "banana" in fruits )
print( "melon" in fruits )

print( fruits[3] )
fruits[3] = "melon" #3번인덱스에 멜론 추가
print( fruits )

print( fruits[:] )
print( fruits[2:] )
print( fruits[:3] ) # end index -1
print( fruits[:-2] )
print( fruits[4][1] )

print( len( fruits ) )
print( max( fruits ) )
print( min( fruits ) )
print( fruits )
fruits.append( "pear" )
print( fruits )
fruits.insert(2, "watermelon")
print( fruits )
#fruits.extend( "apple" )
# print ( fruits )
print( fruits.count( "apple" ) ) # apple이 포함된 갯수
print( fruits.index( "apple" ) ) # apple의 위치
print( fruits.pop() ) # 맨끝에 있는 인덱스의 값을 가져옴
fruits.remove( "apple" ) #apple 삭제 리턴값없으므로 따로 print함
print( fruits )
fruits.sort() #오름차순 (reverse=True ) 내림차순
print( fruits )

shop = ["라면", "햇반", "김치"]
shoplist = [fruits, shop]
print( shoplist )

print( shoplist[1][1] )
print( shoplist[1][1][1] )
print( shoplist[1][:2] )
shoplist[1].append( "달걀" )
print( shoplist )

print( shoplist[:2][:2] ) #(행,열) 앞에거를 가지고 계산하고 뒤에거를 계산하는 방식
print( shoplist[0][: len( shoplist[0] )] )

print()
print("튜플")
# 튜플
a, b = ( 10, 20 )
print( a,b )

zoo = ( "dog", "cat", "monkey", "snake" )
a, b, c, d = zoo
print( a ) #각인덱스에 a, b, c, d 부여

print( zoo[0] )
print( zoo[0:2] )
print( len( zoo ) )

# list <-> tuple 리스트랑 튜플은 서로 바꿀 수 있다.
z = list( zoo )
z.sort()
print( z )
print( type( z ) )

t = tuple( z )
print( max( t ) )
# print( t.index( "tiger" ) )
print( t )
print( type( t ) )

def calc( a, b ) :
    return ( a+b, a-b, a*b, a/b )
values = calc( 5, 2 )
print( values[0] )

# set
country = set ( ["korea","japan","china","russia","taiwan"])
print( type( country ) )
country.add( "korea" )
print( country )
nation = country.copy()
nation.add( "USA")
nation.add( "UK" )
print( nation )
print( nation - country )
print( nation | country )
print( nation & country )
print()
print( nation.difference( country ) )
print( nation.union( country ) )
print( nation.intersection( country ) )

nation.remove( "UK" )
print( nation )
nation.pop()
print( nation )

print( nation.symmetric_different( country ) ) #교집합이 아닌 값

print( "korea" in nation )
print( "korea" not in nation )






























 








