# 가변 인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print(f'이름 : {name}\t 나이 : {age}', end=" ")
    print(lang1,lang2,lang3,lang4,lang5)
    
profile('유재석',20,'Python','Java','C','C++','C#')
profile('김태혼',25,'kotlin','swift',"","","")

"""
이 경우에 lang이 하나 더 늘거나
lang이 계속 줄어서 에러가 뜰 수 있다
이럴 때를 대비해서 있는 것이 가변 인자다
"""

# 가변 인자
def profile(name, age, *language):
    print(f'이름 : {name}\t 나이 : {age}', end=" ")
    for lang in language:
        print(lang, end=" ")
    print()
    
profile('유재석',20,'Python','Java','C','C++','C#','javascript')
profile('김태혼',25,'kotlin','swift')