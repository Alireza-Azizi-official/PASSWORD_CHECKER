import string, getpass, time 

def c_p_strenght():
    password = getpass.getpass("ENTER YOUR PASSWORD : ")
    strenght = 0
    remarks = ''
    lower = upper = w_space = num = special = 0
    
    for i in list(password):
        if i in string.ascii_lowercase:
            lower += 1
        elif i in string.ascii_uppercase:
            upper += 1 
        elif i == " " : 
            w_space +=1 
        elif i in string.digits:
            num += 1
        else:
            special += 1
            
    if lower >= 1:
        strenght += 1 
    elif upper >= 1 :
        strenght += 1
    elif num >= 1 : 
        strenght += 1
    elif w_space >= 1 : 
        strenght += 1 
    elif special >= 1 :
        strenght +=1
    
    if strenght == 1 : 
        remarks = ("THAT IS A VERY BACK PASSWORD. CHANGE IT AS SOON AS POSSIBLE.")
    elif strenght == 2 :
        remarks = ("THAT IS A WEAK PASSWORD. YOU SHOULD CONSIDER USING A TOUGHTER PASSWORD.")
    elif strenght == 3 :
        remarks = ("YOUR PASSWORD IS OK, BUT IT CAN BE IMPROVED.")
    elif strenght == 4 :
        remarks = ("YOUR PASSWORD IS HARD TO GUESS, BUT YOU COULD MAKE IT EVEN MORE SECURE.")
    elif strenght == 5 : 
        remarks = (" NOW THAT IS ONE HELL OF A STRONG PASSWORD>")
        
    print("your password has : ")
    print(f'{lower} lower case letters.')
    print(f'{upper} upper case letters.')
    print(f'{num} numbers.')
    print(f'{w_space} white spaces.')
    print(f'{special} special characters.')
    print(f'passowrd score is :{strenght / 5}')
    print(f"Remarks : {remarks}")
    
def check_pwd(another_pw = False):
    valid = False
    if another_pw:
        choise = input("DO YOU WANT TO CHECK YOUR PASSWORDS STRENGHT (y/n):")
        
    while not valid:
        if choise.lower() == "y":
            return True
        elif choise.lower() == "n":
            print("EXITING.....")
            return False 
        else: 
            print("INVALID INPUT........ PLEASE TRY AGAIN. \n")
            
if __name__ == "__main__":
    print("-_-_-_-_-_-_-_ WELCOM TO PASSWORD STRENGTH CHECKER -_-_-_-_-_-_-_")
    check_pwd = check_pwd()
    while check_pwd:
        c_p_strenght()
        check_pwd = check_pwd(True)
    