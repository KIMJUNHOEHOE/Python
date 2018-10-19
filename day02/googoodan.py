while True:
    dan = input('출력할 단을 입력해주세요 [2-9] ')
    if int(dan) in list(range(2,10)) : break
    else : pass
print('%s 단 출력' % dan)
print('-'*10)
for i in range(1,10):
    print('%s*%d = %d' % (dan, i, int(dan)*i))