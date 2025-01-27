# 모듈
"""
class, def를 담고있는 파일을 모듈이라고 한다
"""
# pratice module 불러오기
import pratice_module
pratice_module.popcorn(5000) # 5천원 팝콘
pratice_module.coupon(5000) # 5천원 팝콘 - 쿠폰 할인
pratice_module.soldier(5000) # 5천원 팝콘 - 군인 할인인

import pratice_module as pm # 줄여쓰기
pm.popcorn(5000)
pm.coupon(5000)
pm.soldier(5000)

from pratice_module import * # 전부 다 쓰겠다고 하여 가져오는 것
popcorn(50)
coupon(50)
soldier(50)

from pratice_module import popcorn, coupon # 필요한 함수들만 import 함
popcorn(5)
coupon(10)

from pratice_module import popcorn as pp # 필요한 함수도 줄여쓸 수 있음
pp(50)