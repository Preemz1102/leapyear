emp_dict = {1111: "Sim",
            1234: "James",
            9999:"Amy",
            5555:"Jessica",
            102:"Tom"
            }

def func(dict, key, name):
    if key in dict:
        clean = ''.join([i for i in name if not i.isdigit()])
        if(clean.lower() in dict[key].lower()):
            if(len(name)>3):
                return True
            else:
                return False
        else:
            return False
    else:
        return False



print(func(emp_dict, 5555,"Jess")) #true
print(func(emp_dict, 1111,"Sim")) #false
print(func(emp_dict, 1234,"ames"))  #true
print(func(emp_dict, 9999,"Amy")) #false
print(func(emp_dict, 9991239,"Amy")) #false
print(func(emp_dict, 102,"123Tom")) #True

