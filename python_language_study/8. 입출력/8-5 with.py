# with
"""
with 함수를 사용하면 close함수를 쓰지 않아도 자동으로 파일이 닫히기 때문에
간편하다
"""
import pickle

with open('profile.pickle', 'rb') as profile_file:
    print(pickle.load(profile_file))
    
with open('study.txt', 'w', encoding='utf8') as study_file:
    study_file.write('파이썬을 열심히 공부하고 있어요')
    
with open('study.txt', 'r', encoding='utf8') as study_file:
    print(study_file.read())