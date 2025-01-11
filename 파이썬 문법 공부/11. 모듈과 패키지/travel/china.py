class ChinaPackage:
    def detail(self):
        print('[중국 패키지 3박 4일] 마카오가서 돈 따러 가자!!')
        
"""
if__name__을 활용해서 모듈을 내부에서 사용하는건지
모듈을 외부에서 사용하는건지 구분해서 필요한 코드를 작성할 수 잇음

"""
        
if __name__ == '__main__':
    print('China 모듈을 직접 실행')
    print('이 문장은 모듈을 직접 실행할 때만 실행함')
    trip_to = ChinaPackage()
    trip_to.detail()
else:
    print('China 외부에서 모듈 호출')