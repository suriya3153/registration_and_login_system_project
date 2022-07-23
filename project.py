import re
from csv import writer 
import pandas as pd
way=input("register or login")
mailpattern="[a-z]+[a-z0-9]+@[a-z]+\.[a-z]+"
password_p="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$"

csvfile=pd.read_csv("iddata.csv")
if way=="register":
    
    while 1:
        
        mailid=input("enter your mail id")
        if mailid in csvfile["id"].tolist():
            print("this id was already taken enter new id")
            print("invalid mail id enter valid mail")
            
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
                repass=input("re-enter password")
                if repass==password:
                    print("your account created successfuly")
                    data=[mailid,password]
                    with open("iddata.csv","a") as wr:
                        hwr=writer(wr)
                        hwr.writerow(data)
                    way="login"
                    break
                
                else:
                    print("password missmatch re enter your password")
            break
        else:
            
            print("password most 8-16 uppercase,lowercase,numbers and spicial charecter requied")
elif way=="login":
    id=input("enter your email : ")
    if id in csvfile["id"].tolist():
        for i in range(2,-1,-1):
            pas=input("enter your password")
            f=sum(csvfile[csvfile["id"]==id].index.values)
            if pas==csvfile["password"][f]:
                print("you are logined")
                break
            else:
                print(i,"attempt left")
                if i==0:
                    print("id temperly blocked")
                continue
        
    else:
        print("wroug id or ivalid id")
        
else:
    print("enter valid input")
