import re
from csv import writer 
import pandas as pd
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# only one time use this 3 line code for make a file 
#data={}
#ft=pd.DataFrame(data,columns=["id","password"])
#ft.to_csv('iddata.csv',index=False)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
csvfile=pd.read_csv("iddata.csv")
way=input("register or login :")
mailpattern="[a-z]+[a-z0-9]+@[a-z]+\.[a-z]+"
password_p="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{5,16}$"
#funtions
def registeration():
    while 1:
        mailid=input("enter your mail id :")
        if mailid in csvfile["id"].tolist():
            print("this id was already taken enter new id")
        else:
            if re.match(mailpattern,mailid):
                print("stpe 2")
                break
            else:
                print("invalid mail id enter valid mail")
                continue
    while 1:
        password=input("set your password : ")
        if re.match(password_p,password):
            while 1:
                repass=input("re-enter password :")
                if repass==password:
                    print("your account created successfuly")
                    data=[mailid,password]
                    with open("iddata.csv","a") as wr:
                        hwr=writer(wr)
                        hwr.writerow(data)
                    nextd=input("press (1) to login or press (2) back :")
                    if nextd=="1":
                        logins()
                    else:
                        pass
                    break
                
                else:
                    print("password missmatch re enter your password")
                    
            break
        else:
            
            print("password most 5-16 minimum one uppercase, one lowercase,numbers and one spicial charecter requied")
def logins():            
    id=input("enter your email : ")
    if id in csvfile["id"].tolist():
        for i in range(2,-1,-1):
            pas=input("enter your password :")
            f=sum(csvfile[csvfile["id"]==id].index.values)
            if pas==csvfile["password"][f]:
                print("you are logined")
                break
            else:
                print(i,"attempt left")
                sur=input("try again enter your password press (1),forget your password (2),go back press(3) :")
                if i==0:
                    print("id temperly blocked")
                else:
                    if sur=="1":
                        pass
                    elif sur=="2":
                        forgotp()
                        break
                    else:
                        break             
                continue  
    else:
        print("wroug id or regisert ypur accont")
        ne=input("try again enter your id press (1),register your account press (2),go back press (3) :")
        if ne=="1":
            logins()
        elif ne=="2":
            registeration()
        else:
            pass
def forgotp():
    id=input("enter your email : ")
    if id in csvfile["id"].tolist():
        logr=input("do you want your old password press (1) or create new password press (2) :")
        if logr=="1":
            f=sum(csvfile[csvfile["id"]==id].index.values)
            print("your old password is",csvfile["password"][f])
            ing=input("you want to login press (1) or go back press (2) :")
            if ing=="1":
                logins()
            else:
                pass
        elif logr =="2":
            f=sum(csvfile[csvfile["id"]==id].index.values)
            while 1:
                password1=input("set your password : ")
                if re.match(password_p,password1):
                    while 1:
                        repass=input("re-enter password :")
                        if repass==password1:
                            print("your password as been changed successfuly")
                            csvfile["password"][f]=repass
                            csvfile.to_csv("iddata.csv",index=False)
                            ing=input("you want to login press (1) or go back press (2) :")
                            if ing=="1":
                                logins()
                            else:
                                pass
                            break
                    break
                else:
                    print("password most 5-16 minimum one uppercase, one lowercase,numbers and one spicial charecter requied")
        else:
            print("invalid input try again")
    else:
        print("wrong id or you not register your accont")
        inp=input("try again enter your id press (1),register your account press (2),go back press (3) :")
        if inp=="1":
            logins()
        elif inp=="2":
            registeration()
        else:
            pass                
if way=="register":
    registeration()
elif way=="login":
    f=input("login or forgot Password :")
    if f=="login":
        logins()
    elif f=="forgot":
        forgotp()
    else:
        pass     
else:
    print("enter valid input")
