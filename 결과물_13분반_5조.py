from random import randint

def game_num():
    global nums
    nums = []
    
    for i in range(3):
        num1 = randint(0,9)
        if num1 not in nums:
            nums.append(num1)
            
    print("랜덤으로 숫자 3개가 지정되었습니다.")
   
    
    
    return nums


def get_num():
    print("숫자를 하나씩 입력해주세요")

    global get_nums
    get_nums=[]



    count = 0

    while (count<3):
        num2 = int(input("숫자를 입력해주세요"))

        if(num2 in get_nums):
            print("중복된 숫자입니다.")
            continue
        elif (num2 >=0 and num2 <=9):
            count += 1
            get_nums.append(num2)
            continue
        else:
            print("범위에 맞지 않는 숫자입니다.")
            continue

    

    return get_nums
        


def guesses_num():
    b_count = 0
    s_count = 0
    g_count = 0

    for i in range(3):
        if(get_nums[i]==nums[i]):
            s_count += 1
        elif (get_nums[i] in nums):
            b_count += 1

    print(b_count,"B", s_count,"S입니다.")
    
    
    return s_count, b_count 

game_num()

g_count = 0
while True:
    
    get_num()
    
    s, g = guesses_num()
    g_count += 1

    if s == 3:
        
        print("축하합니다. 세 숫자의 값과 위치를 모두 맞추셨습니다!")
        print("총",g_count,"회 만에 성공하였습니다.")

        break
    
