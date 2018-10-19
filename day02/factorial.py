# 숫자나, 해당 범위 숫자 입력하지 않을 경우 다시 반복.
num_chk_list = list('0123456789') # check를 위해
# print(num_chk_list)
num2 = ''
# 숫자를 입력하지 않았을 경우
while True:
    num = input('숫자를 입력해 주세요.[1~100] ') # input 함수 리턴 타입은 문자열
    chk_num = True

    for chr in num:
        is_num = chr in num_chk_list
        chk_num *= is_num
        if not is_num :
            break

    if chk_num: # for문 밖에서 break 하기 위해서 chk_num을 설정
        num = int(num)

    else:
        print('입력한 값이 숫자가 아닙니다.')
        continue

    sum = 0
    ft = 1
    print('입력한 숫자 : %s' % num)
    print('-'*20)
    print('%s 까지의 합계 및 팩토리얼 구하기!!' % num)
    print('-'*20)
    for i in range(1, num+1):
        sum = sum + i
    print('%s 까지의 합계는 %d 입니다' % (num,sum))
    print('아래는 팩토리얼 테이블입니다')
    for i in range(0, num+1):
        if i == 0 :
            print('0! = 1')
        else:
            ft = ft*i
            print('%d! = %d' % (i,ft))
