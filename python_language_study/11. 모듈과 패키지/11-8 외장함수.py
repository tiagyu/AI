# 외장함수
"""
구글에 list of python modules -- 외장함수 볼 수 있음

glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
os : 운영체제에서 제공하는 기본 기능
time : 시간 관련 함수

"""
# glob
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os
import os
print(os.getcwd()) # 현재 디렉토리 표시

folder = 'sample_dir'

if os.path.exists(folder):
    print('이미 존재하는 폴더입니다')
    os.rmdir(folder)
    print(folder, '폴더를 삭제하였습니다')
else:
    print(folder, '폴더를 생성하였습니다')
    
print(os.listdir()) # glob와 비슷한 함수

# time
import time
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
print('오늘 날짜는 ', datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 지정
td = datetime.timedelta(days=100) # 100일 저장
print('우리가 만난지 100일은 ', today+td) # 오늘부터 100일 후후