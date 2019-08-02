inp = input('Enter Num: ')

sum = 0

for i in str(inp):
    if("-" in i):
        continue
    elif("."in i):
        break
    elif(int(i)>5 ):
        temp = int(i)
        while (temp > 5):
            sum = sum + temp
            temp -= 1
            
            
print(sum)

# strtest = "hiblake"
# l = list(strtest)
# s2 = 0
# for i in l:
#     print(ord(i))
#     s2 = s2 + ord(i)
# print(s2)