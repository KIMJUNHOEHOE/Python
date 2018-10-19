# Arbitrary Arguments, 가변 인자 리스트 활용
def introduceMyFamily(my_name, *family_names, **family_info): # * : 문자열, 정수형, 리스트, 튜플과 같은 동일한 타입 다 가져와라(packing) ** key, value로 이루어진 타입 다 가져와라(pakcing)
    print(family_names) # packing 시 리턴 값은 튜플
    print(family_info)
    print('안녕하세요, 저는 %s 입니다.' % (my_name))
    print('-' * 35)
    print('제 가족들의 이름은 아래와 같아요. ')

    for name in family_names:
        print('* %s ' % (name), end='\t')
    else:
        print()
    print('-' * 35)

    for key in family_info.keys():
        print('- %s : %s ' % (key, family_info[key]))


introduceMyFamily('진수', '희영', '찬영', '준영', '채영',
                  주소='롯데캐슬', 가훈='극기상진', 소망='세계일주')

# * : unpacking(튜플타입) - 함수를 호출할 때 unpacking
# def add(a, b):
#     return a + b
#
# data = (10, 20)    # tuple
# #print(add(data)) - 튜플 형태의 parameter 1개 들어가서 오류.
# print(add(*data))  # unpacking도 튜플에 대해서만