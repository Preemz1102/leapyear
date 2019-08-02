def anagram(str, str2):
    str = str.lower()
    str2 = str2.lower()
    
 
    
    if len(str) == len(str2):
#         for x in range(1,len(str)):
#             if ord(str[x]) == ord(str2[x]):
#                 return False
        for a in str:
            charsMatch = True
            for b in str2:
                if ord(a) == ord(b):
                    charsMatch = True
                    str2 = str2.replace(b, "", 1)
                    break
                else:
                    charsMatch = False
            if charsMatch == False:
                return False
    else:
        return False
    
    if charsMatch:
        return True            
            
    return False


print(anagram("eat","tea"))
print(anagram("backward","drawback"))
print(anagram("reductions", "Discounter"))
print(anagram("mango","apple"))
print(anagram("bca","aab"))
print(anagram("Schoolmaster","Theclassroom"))
print(anagram("etat","teea"))
print(anagram("anagram", "nagaram"))
print("**************************")
print(anagram("abc","cba1"))
print(anagram("abc","cab"))