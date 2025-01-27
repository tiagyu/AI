# for 반복문
for waiting_no in [0,1,2,3,4]:
    print(f'대기번호 : {waiting_no}')
    
for waiting_no in range(5): # 0,1,2,3,4
    print(f'대기번호 : {waiting_no}')

starbucks = ['아이언맨','토르','아이엠 그루트']  
for customer in starbucks:
    print(f'{customer}, 커피가 준비되었습니다.')