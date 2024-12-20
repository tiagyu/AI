# continue & break
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1,11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        print(f'오늘 수업 여기까지 {student} 따라나와')
        break # 뒤에 반복값이 있든 없든 상관없이 반복문을 탈출함
    print(f'{student}. 책을 읽어라')