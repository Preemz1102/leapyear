
def check_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def rotations(num):
    
    rotate = []
    
    d = str(num)
    
    for ele in d:
        rotate.append(int(d))
        d= d[1:]+d[0]
    return rotate
        

def get_circular_prime_count(limit):
    primeList = []
    circPrimeList = []
    primeRange = str(1)
    
    for i in range(0, len(str(limit))):
        primeRange += str(0)
    
    print("Prime Range: " +primeRange)
      
    for i in range(2, int(primeRange)):
        if check_prime(i):
            primeList.append(i)
    
    for i in primeList:
        if i < limit:
            validCircPrim = False
            rotationsList = rotations(i)
            for a in rotationsList:
                if a in primeList:
                    validCircPrim = True
                else:
                    validCircPrim = False
                    break
            if validCircPrim == True:
                circPrimeList.append(i)
    print(circPrimeList)
    return len(circPrimeList)



# print(rotations(1234))
print(get_circular_prime_count(500))
print(get_circular_prime_count(20))