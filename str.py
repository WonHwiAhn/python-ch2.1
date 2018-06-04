# 180524
# 한 줄 문자열 정의
print('# 한 줄 문자열 정의')
s = ''
str1 = 'hello world'
str2 = 'hello world'
print(type(s), type(str1), type(str2))
print(isinstance(str2, str))

# 여러줄 문자열 정의
print('# 여러줄 문자열 정의')
str3 = """ABC
DEF
가나다라마
바사아자차카"""
print(str3)

# 여러줄 주석: 여러줄 문자열 사용
"""
    이런식으로 그냥 글을 씀.
    17번째 줄에서 생성됬다가 20번째 줄에서 소멸.
    실행은 되지만 크게 영향을 미치지는 않는다.
"""

# escape
print('# escape')
print("\"Hello\nWorld\nI Say\"")
print('"Hello\nWorld\nI Say"')

# 문자열 연산
print('# 문자열 연산')
str1 = "First String"
str2 = "Second String"

# 인덱싱
print('# 인덱싱')
print(str1[0], str1[2], str1[4])

#슬라이싱 str2 = Second String
print('#슬라이싱')
str3 = str2[2:5]
print(str3)
print(str2[2:])

"""
    str2[2:2] = "c"
    이런식으로 하면 원래는 삽입효과를 낼 수 있는데
    String은 immutable 속성을 가지고 있기 때문에 적합하지않다.
"""

# 연결(+)
print('# 연결(+)')
print(str1 + '  ' + str2)
str3 = 'str1'  'str3'
print(str3)

# 문자열 객체와 정수형 객체는 + 연산을 할 수 없다
print('# 문자열 객체와 정수형 객체는 + 연산을 할 수 없다')
name = "길동"
age = 40
# print(name + age)

# 반복(*)
print('# 반복(*)')
print(str1 * 3)

# len() 함수
print('# len() 함수')
print(len(str2))

# in, not in 연산
print('# in, not in 연산')
print('S' in str2)
print('S' not in str2)

#문자열 객체는 변경할 수 없다(immutable)
# str1[0] = 'f'

# 서식(formatting)
print('# 서식(formating)')
print('name: ' + name + ", age: " + format(age, 'd'))
print('name: ' + format(name, 's') + ", age: " + format(age, 'd'))

# 서식(formating) - 튜플을 이용한 포매팅
f = 'name:%s, age:%d'
print(f)
print(f % (name, age))

# 서식(formatting) - 딕셔너리를 이용한 formatting
f = 'name:%(name)s, age:%(age)d'
print(f % {'name':'둘리', 'age':13})

# 대소문자 관련 객체함수
s = 'i like Python'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

# 검색 관련 객체함수
print('# 검색 관련 객체함수')
s = 'I Like Python. I Like Java Also'
print(s.count('Like'))
print(s.find('Like'))
print(s.find('Like', 5))
print(s.find('JavaScript'))
print(s.rfind('Like'))

# 반견하지 못하면 예외가 발생한다.
# print(s.index('JavaScript'))
print(s.rindex('Like'))
print(s.startswith('I Like'))
print(s.startswith('Like', 2))
print(s.endswith('Also'))
print(s.endswith("Java", 0, 26))

# 편집과 치환
print('# 편집과 치환')
s = '       spam and ham      '
print('-----' + s.strip() + '-----')
print('-----' + s.rstrip() + '-----')
print('-----' + s.lstrip() + '-----')


s = '<><abc><><defg><><>'
print(s.strip('<>'))

s = "Hello Java"
print(s.replace('java', 'Python'))

#정렬
print('#정렬')
s = 'King and Queen'
print('===' + s.center(60) + "===")
print(s.center(60, '='))
print(s.ljust(60, '='))
print(s.rjust(60, '-'))

# 분리와 결합
print('#분리와 결합')
s = 'Spam and Ham'
t = s.split()
print(t)

t = s.split(' and ')
print(t)

s2 = ':'.join(t)
print(s2)

s3 = 'one:two:three:four:five'
print(s3.split(':'))
print(s3.split(':', 2))

lines ="""
    1st line
    2nd line
    3rd line
    4th line
"""

print(lines.split('\n'))
print(lines.splitlines())

#판별
print('#판별')
print('1234'.isdigit()) # TRUE
print('abcd'.isalpha()) # TRUE

print('1234'.isalpha()) # FALSE
print('abcd'.isdigit()) # FALSE

print('  '.isspace()) # TRUE
print(''.isspace()) # FALSE
print('\r\n'.isspace()) # TRUE
print('\t'.isspace()) # TRUE

# '0' 채우기
print('# "0" 채우기')
print('20'.zfill(5))
print('1234'.zfill(5))
print('123123'.zfill(5))

# 서식(formatting) 객체함수
print('# 서식(formatting) 객체함수')
f = 'name:{}, age:{}'
print(f.format('둘리', 13))
print('name:{0}, age:{1}'.format('둘리', 13))
print('name:{1}, age:{0}'.format(13, '둘리'))

print('{:3}의 제곱근은 {:.7}'.format(2, 2**0.5))

f = 'name:{name}, age:{age}'
print(f.format_map({'age':13, 'name':'둘리'}))