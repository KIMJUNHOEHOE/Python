# 모두 대문자로.
sentence = 'The BPC find information to design valuable society with Tech & Craft.'
print(sentence.upper())

# 모두 소문자로
print(sentence.lower())

# 대소문자 바꿔서 출력 - for문 이용
# 문자열 추가는 + : 'a' + 'b' + 'c' = 'abc'
new_sentence = ''
for i in sentence:
    if i.isupper():
        new_sentence = new_sentence + i.lower()
    else :
        new_sentence = new_sentence + i.upper()
print(new_sentence)

# 대소문자 바꿔서 출력 - 문자열 함수 이용
print(sentence.swapcase())

