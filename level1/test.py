# 삼각형, 사각형 종류 높이에 따라 출력
import sys # 프로그램 종료를 시키기 위해 필요한 모듈

def s_c(num):
    if (num == 1):
        hight = int(input("높이: "))
        return hight
        
    elif (num == 1):
        hight = int(input("높이: "))
        return hight
        
    elif (num == 2):
        hight = int(input("높이: "))
        return hight
        
    else:
        return False

# def draw():
    

while 1: # 무한루프
    print("도형을 선택하세요.")
    print("1. 삼각형")
    print("2. 사각형")
    print("3. 종료")

    first_choice = int(input(": ")) # 어떤 도형을 선택할 것인지 first_choice에 저장
    
    if (first_choice == 1): # 삼각형을 선택할 경우
        print()
        print("삼각형의 종류를 선택하세요.")
        print("1. 좌측 직각 삼각형")
        print("2. 우측 직각 삼각형")
        print("3. 이등변 삼각형")
        
        second_choice = int(input(": ")) # 어떤 삼각형을 선택할 것인지 second_choice에 저장
        
        wrong = 0 # 잘못된 입력을 알아내기 위한 변수 0으로 초기화

        while 1: # 무한루프
            if (wrong == 1): # 1~3 외의 숫자를 입력할 경우
               second_choice = int(input(": ")) # 어떤 삼각형을 선택할 것인지 다시 저장
               wrong = 0 # 초기화
            
            if (second_choice == 1): # 좌측 직각 삼각형
                hight = int(input("높이: ")) # 높이 저장
                
                if (hight <= 1 or hight > 10): # 높이가 1 이하 10 초과일때
                    print("잘못된 입력. 2~10 사이의 숫자를 입력해야함.")
                    print()
                    
                else: # 높이가 1 초과 10 이하일 경우
                    
                    #좌측 직각 삼각형 출력
                    for i in range(hight): #높이 hight만큼 반복
                        for j in range(hight-i): # hight-i만큼 반복(첫번째 줄부터 하나씩 줄어듬)
                            print("*",end = '') # 줄바꿈 없이 출력
                        print() # 줄바꿈
                    print()
                    break
                    
            elif (second_choice == 2): # 우측 직각 삼각형
                hight = int(input("높이: ")) # 높이 저장
                
                if (hight <= 1 or hight > 10): # 높이가 1 이하 10 초과일때
                    print("잘못된 입력. 2~10 사이의 숫자를 입력해야함.")
                    print()
                
                else: # 높이가 1초과 10 이하일 때
                    
                    # 우측 직각 삼각형 출력
                    for i in range(hight): # 높이만큼 반복
                        for j in range(hight): # 높이만큼 반복
                            if i > j: # 공백을 구분하기 위함
                                print(' ', end='')
                            else:
                                print("*", end='')
                        print() # 줄바꿈
                    print()
                    break # 반복문 종료
                    
            elif (second_choice == 3): # 이등변 삼각형
                hight = int(input("높이: ")) # 높이 저장
                
                if (hight <= 1 or hight > 10): # 높이가 1 이하 10 초과일때
                    print("잘못된 입력. 2~10 사이의 숫자를 입력해야함.")
                    print()
                
                else: # 높이가 1초과 10 이하일 경우

                    #이등변 삼각형 출력
                    for i in range(2*hight-1): 
                        count = 0 # 꼭짓점을 알아내기 위한 변수 처음엔 초기화
                        
                        for j in range(2*hight-1-i):
                            if i > j: # 공백을 구분하기 위함
                                print(' ', end='')
                            else:
                                print("*",end = '')
                                count+=1 # "*"을 만날때마다 +1
                                
                        if (count == 1): # 꼭짓점을 만났을때
                            print()
                            break; # 반복문 종료
                        
                        print()
                    print()
                    break # 반복문 종료
                    
                    
            else: # 1~3 외의 숫자를 입력한 경우
                print("잘못된 입력. 1~3 사이의 숫자를 입력해야함.")
                print()
                wrong = 1 # wrong 변수에 1을 저장함
                continue
        
        
            
    elif (first_choice == 2): # 사각형을 선택할 경우
        print()
        print("사각형의 종류를 선택하세요.")
        print("1. 좌측 평행사변형")
        print("2. 우측 평행사변형")
        print("3. 마름모")
        second_choice = int(input(": ")) # 어떤 사각형을 선택할 것인지 second_choice에 저장
        wrong = 0 # 잘못 입력한 경우를 알아내기 위한 변수
        
        while 1: # 무한루프
            if (wrong == 1): # 1~3외의 숫자를 입력할 경우
               second_choice = int(input(": ")) # 다시 입력 받음
               wrong = 0 # 초기화
            
            
            if (second_choice == 1): #좌측 평행사변형
                hight = int(input("높이: ")) # 높이 저장
                
                if (hight <= 1 or hight > 10): # 높이가 1 이하 10 초과일 경우
                    print("잘못된 입력. 2~10 사이의 숫자를 입력해야함.")
                    print()
                    
                elif (hight > 1 and hight <=10): # 높이가 2 이상 10 이하일 경우
                    width = int(input("너비: "))# 너비 저장
                    
                    if (width <= 1 or width > 10): # 너비가 1 이하 10 초과일 경우
                        print("잘못된 입력. 2~10 사이의 숫자를 입력해야함.")
                        print()
                        
                    else: # 너비가 2 이상 10 이하일 경우

                        # 좌측 평행사변형 출력
                        for i in range(hight):
                            for j in range(width+2*i):
                                if 2*i > j:
                                    print(" ", end = '')
                                else:
                                    print("*", end = '')
                            print()
                                
                        print()
                        break
                        
                
                    
            elif (second_choice == 2): # 우측 평행 사변형
                hight = int(input("높이: ")) # 높이 저장
                
                if (hight <= 1 or hight > 10): # 높이가 1 이하 10 초과일 경우
                    print("잘못된 입력. 2~10 사이의 숫자를 입력해야함.")
                    print()
                    
                elif (hight > 1 and hight <=10): # 높이가 2 이상 10 이하일 경우
                    width = int(input("너비: ")) # 너비 저장
                    
                    if (width <= 1 or width > 10): # 너비가 1 이하 10 초과일 경우
                        print("잘못된 입력. 2~10 사이의 숫자를 입력해야함.")
                        print()
                        
                    else: # 너비가 1 초과 10 이하일 경우
                        for i in range(hight):
                            count = 0 # *이 너비만큼 출력됬을 경우 반복문을 그만 돌리게 하기 위한 변수
                            for j in range(width+hight):
                                if (hight-i > j):
                                    print(" ", end = '')
                                else:
                                    print("*",end='')
                                    count+=1

                                if (count == width): # 너비와 *의 개수가 같을 경우
                                    break
                                    
                            print()
                            
                        print()
                        break
                    
            elif (second_choice == 3): # 마름모일 경우
                hight = int(input("높이: ")) # 높이 저장

                if (hight%2 == 0 ): # 높이가 짝수일 경우
                    print("잘못된 입력, 홀수를 입력해야함.")
                    print()
                    
                elif (hight <= 1 or hight > 10): # 높이가 1 이하 10 초과일 경우
                    print("잘못된 입력. 2~10 사이의 숫자를 입력해야함.")
                    print()
                    
                else: # 높이가 1 초과 10 이하일 경우
                    middle = int(hight/2) + 1 # 가운데줄
                    
                    for i in range(hight+1): # hight줄을 만들기 위해
                        if (i <= middle): # 가운데줄 윗부분
                            for j in range(middle-i):
                                print(" ", end = '')
                            for j in range(2 * i -1):
                                print("*", end = '')
                            print()
                            
                        else: # 가운데 줄 아랫부분
                            for j in range(i-middle):
                                print(" ", end = '')
                            for j in range((2*middle-i)*2-1):
                                print("*",end = '')
                            print()

                        
                    print()
                    break
                
            else:
                print("잘못된 입력. 1~3 사이의 숫자를 입력해야함.")
                wrong = 1 # 잘못된 입력일 경우 wrong = 1
                continue

           
    elif (first_choice == 3): # 프로그램 종료를 선택할 경우
        print("프로그램 종료")
        sys.exit() # 프로그램 종료

    else: # 1~3외의 숫자를 입력할 경우
        print("잘못된 입력. 1~3 사이의 숫자를 입력해야함.")
        print()
        continue


