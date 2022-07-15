import json
import os
info={}
while True:
    print("press \n 1.for log_in \n 2.for sign_in \n 3.for update  \n 4.for exist")
    n=int(input("enter what do you want to do:"))
    def sign_up():
        try:
            with open("pra.json","r") as p:
                d=json.load(p)
            n=input("enter your email:")
            if "@" in n:
                j={"name":input("enter your name:"),"surname":input("enter your surname:"),"password":input("create your password:")}
                with open("pra.json","w") as p2:
                    d[n]=j
                    json.dump(d,p2,indent=4)
                    c
            else:
                print("please enter correct Email:")
        except:
            n=input("enter your Email:")
            if "@" in n:
                j={"name":input("enter your name:"),"surname":input("enter your surname:"),"password":input("create your password:")}
                with open("pra.json","w") as p3:
                    info[n]=j
                    json.dump(info,p3,indent=4)
                    print("your account sign up successful.")
            else:
                print("please enter correct Email:")
    def sign_in():
        if os.path.exists("pra.json"):

            n=input("enter your Email:")
            password=input("enter your password:")
            with open("pra.json","r") as p4:
                d=json.load(p4)
            if n in d:
                if d[n]["password"]==password:
                    print("your account log_in successful.")
                    print(d[n])
                else:
                    print("your password is wrong.")
            else:
                print("this Email does not exist.")
        else:
            print("please create an account before sign_in.")
    def update():
        try:
            with open("pra.json","r") as p5:
                d=json.load(p5)
            n=input("enter your Email:")
            p=input("enter your password")
            if n in d:
                if d[n]["password"]==p:
                    with open("pra.json","w") as p6:
                        j={"name":input("enter your name:"),"surname":input("enter your surname:"),"password":input("change your password:")}
                        d[n]=j
                        json.dump(d,p6,indent=4)
                    print("your acount updating successful.")
                else:
                    print("your password is wrong.")
            else:
                print("please enter correct Email.")
        except:
            print("please create an account before updating.")
    if n==1:
        sign_up()
    if n==2:
        sign_in()
    if n==3:
        update()
    if n==4:
        break
