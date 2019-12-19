#1번 문제
str= input('문자열을 입력하세요: ')
print(str[0],str[-1])

#2번 문제
num= int(input('숫자를 입력하세요: '))
num_arr=list(range(num+1))
for i in num_arr:
    print(i)


#3번 문제
num2 = int(input('숫자를 입력하세요: '))
if num2%2==0:
    print('짝수')
else:
    print('홀수')
