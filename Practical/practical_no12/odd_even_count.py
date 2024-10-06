import time

def get_even_odd_count1(L):
    for _ in range(10,100,2) :
        even, odd = 0, 0
        for i in L:
            if i % 2 == 0:
                even += 1
            elif i % 2 == 1:
                odd += 1
    return even, odd


def get_even_odd_count2(L):
    for _ in range(10,100,2) :
        even, odd = 0, 0
        for i in L:
            even += (1 - i % 2)
            odd += i % 2
    return even, odd


def get_even_odd_count3(L):
    for _ in range(10,100,2) :
        even, odd = 0, 0
        for i in L:
            if i % 2:
                odd += 1
            else:
                even += 1
    return even, odd


def get_even_odd_count4(L):
    for _ in range(10,100,2) :
        even, odd = 0, 0
        for i in L:
            if bin(i)[-1] == "0":
                even += 1
            else:
                odd += 1
    return even, odd


def check_performance(approaches):
    sample1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    avg_time_taken = []
    for approach in approaches:
        for _ in range(10):
            approach(sample1)
    for approach in approaches:
        time_taken = []
        for _ in range(1000):
            start_time = time.time()
            approach(sample1)
            end_time = time.time()
            time_taken.append(end_time - start_time)
        avg_time_taken.append(sum(time_taken) / 1000)
    
    return avg_time_taken


def better_approach():
    time_list = check_performance([get_even_odd_count1, get_even_odd_count2, get_even_odd_count3, get_even_odd_count4])
    apr1, apr2,apr3,apr4 = time_list[0], time_list[1],time_list[2],time_list[3]
    result_per1 = ((apr1 - apr2)/apr1) * 100
    result_per2 = ((apr1 - apr3)/apr1) * 100
    result_per3 = ((apr1 - apr4)/apr1) * 100

    print("Approach 1 is base approach")
    
    if result_per1 < 0:
        print(f"Approach 1 is {-result_per1:.2f}% slower than approach 2")
    else:
        print(f"Approach 1 is {result_per1:.2f}% faster than approach 2")
    if result_per2 < 0:
        print(f"Approach 1 is {-result_per2:.2f}% slower than approach 3")
    else:
        print(f"Approach 1 is {result_per2:.2f}% faster than approach 3")
    if result_per3 < 0:
        print(f"Approach 1 is {-result_per3:.2f}% slower than approach 4")
    else:
        print(f"Approach 1 is {result_per3:.2f}% faster than approach 4")

    fastest_time = min(time_list)
    fastest_index = time_list.index(fastest_time)
    print(f"Approach {fastest_index + 1} is the fastest.")

better_approach()
