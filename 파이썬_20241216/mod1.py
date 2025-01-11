PI = 3.14

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

if __name__ == '__main__':
    print("mod1.py에서 출력")
    # 외부에선 파일이름 내부에서는 __main__ 출력
    print('모듈 이름 :', __name__) 
    print('mod1.py 자신의 파일에서 실행되었습니다')
    print('모듈 기능 테스트')
    print(add(10,5))