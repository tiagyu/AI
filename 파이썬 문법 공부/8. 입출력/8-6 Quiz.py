"""
Quiz) 당신의 회사에서는 매주 1회 참석해야 하는 보고서가 있다.
보고서는 항상 아래와 같은 형태로 출력되어야 한다

- x 주차 주간보고 -
부서 :
이름 :
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만든다
"""

# 내 풀이
def report_maker(n):
    for i in range(1,n+1):
        with open(f'{i}주차.txt', 'w', encoding='utf8') as report_files:
            report_files.write(f'- {i} 주차 주간보고 -\n')
            report_files.write('부서 :\n')
            report_files.write('이름 :\n')
            report_files.write('업무 요약 :\n')
            
report_maker(2)

# 다른 사람 풀이
for i in range(1,51):
    with open(str(i) + "주차.txt",'w',encoding='utf8') as report_file:
        report_file.write('- {0} 주차 주간보고 -'.format(i))
        report_file.write('부서 :\n')
        report_file.write('이름 :\n')
        report_file.write('업무 요약 :\n')