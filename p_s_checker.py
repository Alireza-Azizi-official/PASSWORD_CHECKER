import string 
import getpass
import time

def p_s_checker():
    password = getpass.getpass("ENTER YOUR PASSWORD: ")
    strenght = 0
    remarks = ""
    lower = upper = num = wspace = special = 0
    
    for i in list(password):
        if i in string.ascii_lowercase:
            lower += 1 
        elif i in string.ascii_uppercase:
            upper += 1
        elif i in string.digits:
            num += 1
        elif i == " ":
            wspace += 1
        else:
            special += 1
            
    if lower >= 1 :
        strenght += 1
    if upper >= 1 : 
        strenght += 1
    if num >= 1 :
        strenght +=1 
    if wspace >= 1:
        strenght += 1
    if special >= 1:
        strenght +=1
    
    if strenght == 1:
        remarks = ("That's a terrible password even a dog can guess it! change it right now.")
    elif strenght == 2:
        remarks = ("That's a weak passsword you should consider using a tougher password.")
    elif strenght == 3:
        remarks ("your password is hard to guess,but it could be better.")
    elif strenght == 4:
        remarks = ("your password is hard enought")
    elif strenght == 5:
        remarks = ("it is a hell hard password which you can not guess it even.")
        
    print("YOUR PASSWORD HAS:")
    print(f"<<{lower}>> lowercase letters.")
    print(f"<<{upper}>> lowercase letters.")
    print(f"<<{num}>> lowercase letters.")
    print(f"<<{wspace}>> lowercase letters.")
    print(f"<<{special}>> lowercase letters.")
    
    print(f"password score : {strenght / 5}")
    print(f"Remarks: {remarks}")
    
def check_pass(another_pw = False):
    valid = False
    
    if another_pw:
        choice = input("Do you want to check another password? (y/n):")
    else:
        choice = input("Do you want to check your password? (y/n):")
    while not valid :
        if choice.lower() == "y":
            return True
        if choice.lower() == "n":
            print("exiting....\n")
            time.sleep(2)
            print("Take care.")
            return False
        else:
            print("invalid input ..... please try again. \n")

if __name__ == "__main__":
    print("_________ PASSWORD STRENGHT CHECKER __________")
    check_pwd = check_pass()
    while check_pwd:
        p_s_checker()
        check_pwd = check_pass(True)
    