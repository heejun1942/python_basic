a = 30
if a > 30:
    print("a 입니다.")
elif a <= 20:
    print("20 이하입니다.")
else:
    print("둘다 아닙니다")


if 30 < a and a < 150:
    print("두 조건에 부합합니다")
elif a > 150 or a > 10:
    print('둘 중 하나가 맞습니다.')


#변수와 문자열을 같이 출력
name='희준'
age=27
print(f'{name}은 {age}살 입니다 ')

