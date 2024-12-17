# 퀴즈
"""
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최한다
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했다
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 된다
추첨 프로그램을 작성하시오

조건1 : 편의성 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건 3 : random 모듈의 shuffle과 sample 활용

(출력 예제)
-- 당첨 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
-- 축하합니다 --

"""

from random import *
# lst = [1,2,3,4,5]
# shuffle(lst)
# print(sample(lst,3))

people = list(range(1,21))
shuffle(people)
winners = sample(people,4)
print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {winners[0]}")
print(f"커피 당첨자 : {winners[1:]}")
print("-- 축하합니다 --")