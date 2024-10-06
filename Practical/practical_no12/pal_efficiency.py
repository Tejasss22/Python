import time
def is_palindrome(text):
    return True if text == text[::-1] else False

def fun1(L):
    for _ in range(10,100,2) :
        count = 0
        valid_obj_count = [int, str]
        valid_obj = [list, tuple, set]
        for i in L:
            t = type(i)
            if t in valid_obj_count:
                if t == int:
                    i = str(i)
                if len(i) % 5 == 3:
                    if is_palindrome(i) :
                        count += 1
            elif t in valid_obj:
                    count += fun1(i)
    return count

def fun(L):
    for _ in range(10,100,2) :
        count = 0
        valid_obj_count = {int, str}
        valid_obj = {list, tuple, set}
        for i in L:
            t = type(i)
            if t in valid_obj_count:
                if t == int:
                    i = str(i)
                    count += (len(i) % 5 == 3 and i == i[::-1])
            elif t in valid_obj:
                    count += fun(i)
    return count

def check_performance(approaches):
    sample1 = [12345, "level", 1221, [54321, 131], {"racecar", 131 , 98789}]
    avg_time_taken = []
    for approach in approaches:
        for _ in range(10):
            approach(sample1)
    for approach in approaches:
        time_taken = []
        for _ in range(100):
            start_time = time.time()
            approach(sample1)
            end_time = time.time()
            time_taken.append(end_time - start_time)
        avg_time_taken.append(sum(time_taken) / 100)
    
    return avg_time_taken


def better_approach():
    time_list = check_performance([fun1, fun])
    apr1, apr2 = time_list[0], time_list[1]
    result_per = ((apr1 - apr2) / apr1) * 100
    
    if result_per < 0:
        print(f"Approach 2 is {-result_per:.2f}% faster than approach 1")
    else:
        print(f"Approach 1 is {result_per:.2f}% faster than approach 2")
better_approach()