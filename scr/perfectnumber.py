
def num_list(input):
    if isinstance(input, int):
        return calc_perf_num([input])
    else:
        return calc_perf_num(input)

def calc_perf_num(num):
    numList = []
    for i in num:
        sum=0
        for x in range(1,i):
            if(i %x == 0):
                sum += x 
        if sum == i:
            if len(num) == 1:
                return True
            else:
                numList.append(i)
    if len(num) == 1:
        return False
    return numList
    
list = [6,28,496,8128,1,52,-1]
print(num_list([6]))
print("*************************")
print(num_list(6))
print("*************************")
print(num_list(5))
print("*************************")
print(num_list(list))
