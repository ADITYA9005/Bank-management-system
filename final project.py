import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as pyql
import seaborn as sns
import matplotlib.style as style
conn=pyql.connect(host='localhost', port='3306', password='9005', database='Bank', user='root')
from datetime import date
from playsound import playsound
#------------------------------------------------#
def login_manager():
    id=input("Enter staff id:")
    pwd=int(input("Enter password:"))
    df=pd.read_csv(r"C:\project\stafffile.csv")
    df=df.loc[df["staffid"]== id]
    if df.empty:
        print("Invalid Username given:")
        playsound(r"C:\\project\\error.wav")
        return False
    else:
        df=df.loc[df["password"]== pwd]
        if df.empty:
            print("Invalid Password given:")
            playsound(r"C:\\project\\error.wav")
            return False
        else:
            df=df.loc[df["position"]== 'manager']
            if df.empty:
                print("You are not authorize to login as manager ")
                playsound(r"C:\\project\\error.wav")
                return False
            else:
                print("User name and password  Matchsuccessfully")
                return True
#----------------------------------------------------#
def login_staff():
    id=input("Enter staff id:")
    pwd=int(input("Enter password:"))
    df=pd.read_csv(r"C:\project\stafffile.csv")
    df=df.loc[df["staffid"]== id]
    if df.empty:
        print("Invalid Username given:")
        playsound(r"C:\\project\\error.wav")
        return False
    else:
        df=df.loc[df["password"]== pwd]
        if df.empty:
            print("Invalid Password given:")
            playsound(r"C:\\project\\error.wav")
            return False
        else:
            df=df.loc[df["position"]== 'staff']
            if df.empty:
                print("You are not authorize to login as staff ")
                playsound(r"C:\\project\\error.wav")
                return False
            else:
                print("User name and password  Matchsuccessfully")
                return True
#-------------------------------------------------------------#
def login_user():
    acc=input("Enter account no. :")
    pwd=int(input("Enter password:"))
    df=pd.read_csv(r"C:\project\bankfile.csv")
    df=df.loc[df["accno"]== acc]
    if df.empty:
        print("Invalid account no. given:")
        playsound(r"C:\\project\\error.wav")
        return False
    else:
        df=df.loc[df["password"]== pwd]
        if df.empty:
            print("Invalid Password given:")
            playsound(r"C:\\project\\error.wav")
            return False
        else:
            print("User name and password  Matchsuccessfully")
            playsound(r"C:\\project\\welcome.mpeg")
            return True
#-----------------------------------------------------------#
def show_option():
    print("What is your designation")
    print("Ex- PRESS 1.Manager, \n    PRESS 2.Staff,\n    PRESS 3.Account_holder ")
    choice=int(input("Enter designation:"))
    return choice
#--------------------------------------------#
def showMenu_manager():
    print("************")
    print("       BANK MANAGEMENT SYSTEM        ")
    print(" Press:1 - To Show Bank file      ")
    print(" Press:2 - Add a new Account Holder   ")
    print(" Press:3 - Delete a Bank Account   ")
    print(" Press:4 - Show Bank Staffmember    ")
    print(" Press:5 - Add a new staff   ")
    print(" Press:6 - Delete staff     ")
    print(" Press:7 - Graphical represtation of accountholders     ")
    print(" Press:8 - Graphical represtation of staff     ")
    print(" Press:9 - To exit   ")
    print("***********")
    choice=int(input("Enter your choice:"))
    return choice
#------------------------------------------------------------#
def showMenu_staff():
    print("************")
    print("       BANK MANAGEMENT SYSTEM        ")
    print(" Press:1 - To Show Bank file      ")
    print(" Press:2 -  Sort account according to name  ")
    print(" Press:3 - Add a new Account Holder   ")
    print(" Press:4 - Delete a Bank Account   ")
    print(" Press:5 -  show graph   ")
    print(" Press:6 - Graphical represtation     ")
    print(" Press:7 - To exit   ")
    print("***********")
    choice=int(input("Enter your choice:"))
    return choice
#-----------------------------------------#
def showMenu_user():
    print("************")
    print("       BANK MANAGEMENT SYSTEM        ")
    print(" Press:1 - To Show account details      ")
    print(" Press:2 -  Deposite money  ")
    print(" Press:3 - Withdrawl money   ")
    print(" Press:4 - To exit   ")
    print("***********")
    choice=int(input("Enter your choice:"))
    return choice
#-------------------------------------------------------#
def about():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("In this project you know anout BANK MANAGEMENT using ")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#---------------------------------------------------------#
def bankcsv():
    print("Reading files")
    print()
    df=pd.read_csv(r"C:\project\bankfile.csv",index_col=0)
    print(df.iloc[:,0:5])
#-------------------------------------------------------#
def new_acholder():
    accno=input("Enter account no :")
    name=input("Enter account holder name:")
    phno=int(input("Enter mobile no. :"))
    mail=input("Enter email id:")
    addres=input("Enter address:")
    city=input("Enter city:")
    balance=int(input("Enter balance amount:"))
    password=input("Enter password:")
    df=pd.read_csv(r"C:\project\bankfile.csv")
    n=df["accno"].count()
    df.at[n]=[accno,name,phno,mail,addres,city,balance,password]
    df.to_csv(r"C:\project\bankfile.csv",index=False)
    sql="CREATE TABLE if not exists {}(User_name varchar(100),deposite int(10),withdrawl int(10),date DATE)".format(accno)
    mys=conn.cursor()
    mys.execute(sql)
#-------------------------------------------------#
def removeaccount():
    df=pd.read_csv(r"C:\project\bankfile.csv",index_col='accno')
    accno=input("Enter account no :")
    df.drop(accno,axis=0,inplace=True)
    df.to_csv(r"C:\project\bankfile.csv")
    print("account deleted successfullly")
    sql="drop table {}".format(accno)
    mys=conn.cursor()
    mys.execute(sql)
    conn.commit()
#--------------------------------------------------------#
def sort_name():
    df=pd.read_csv(r"C:\project\bankfile.csv",index_col=0)
    df=df.sort_values('name')
    print(df)
#--------------------------------------------------------#
def deposit():
    df=pd.read_csv(r"C:\project\Bankfile.csv",index_col=False)
    a=input("Enter account no :")
    b=int(input("Enter amount deposite :"))
    df.loc[df['accno']==a,['bal']]=df['bal']+b
    df.to_csv(r"C:\project\Bankfile.csv",index=False)
    df1=pd.read_csv(r"C:\project\Bankfile.csv",index_col='accno')
    c=df1.name[a]
    d=date.today()
    sql="INSERT INTO {}( User_name, deposite, withdrawl, date) VALUES('{}',{},{},'{}')".format(a,c,b,0,d)
    mys=conn.cursor(prepared=True)
    mys.execute(sql)
    conn.commit()   
    playsound(r"C:\\project\\thank-you.wav")
#------------------------------------------------------------#
def withdraw():
    df=pd.read_csv(r"C:\project\Bankfile.csv",index_col=False)
    a=input("Enter account no :")
    b=int(input("Enter amount withdrawl : "))
    df.loc[df['accno']==a,['bal']]=df['bal']-b
    df.to_csv(r"C:\project\Bankfile.csv",index=False)
    df1=pd.read_csv(r"C:\project\Bankfile.csv",index_col='accno')
    c=df1.name[a]
    d=date.today()
    sql="INSERT INTO {}( User_name, deposite, withdrawl, date) VALUES('{}',{},{},'{}')".format(a,c,0,b,d)
    mys=conn.cursor(prepared=True)
    mys.execute(sql)
    conn.commit()
    playsound(r"C:\\project\\thank-you.wav") 
#----------------------------------------------------------#
def showstaff():
    df=pd.read_csv(r"C:\project\stafffile.csv",index_col=0)
    print(df.iloc[:,0:5])
#---------------------------------------#
def new_staff():
    staffid=input("Enter staff id :")
    name=input("Enter staff name:")
    age=int(input("Enter staff age no. :"))
    phoneno=int(input("Enter phone no:"))
    salary=int(input("Enter salary:"))
    position=input("Enter designation:")
    password=input("Enter password:")
    df=pd.read_csv(r"C:\project\stafffile.csv")
    n=df["staffid"].count()
    df.at[n]=[staffid,name,age,phoneno,salary,position,password]
    df.to_csv(r"C:\project\stafffile.csv",index=False)
    print("staff added")
#--------------------------------------------------$
def removestaff():
    df=pd.read_csv(r"C:\project\stafffile.csv",index_col='staffid')
    staffid=input("Enter staffid :")
    df.drop(staffid,axis=0,inplace=True)
    df.to_csv(r"C:\project\stafffile.csv")
    print("account deleted successfullly")
#---------------------------------------------------------#
def show_account():
    import pandas as pd
    from pandas.core.indexes.base import Index
    a=input("Enter account no")
    df=pd.read_csv(r"C:\project\bankfile.csv")
    c=df[df['accno']==a]
    print(c)
    sql="select * from {}".format(a)
    mys=conn.cursor()
    mys.execute(sql)
    r=mys.fetchall()
    i=0
    for i in r:
        print(i)
#----------------------------------------------------------#
def all_graph():
    df=pd.read_csv(r"C:\project\bankfile.csv")
    plt.figure(figsize=(35,10))
    plt.subplot(2,2,1)
    sns.lineplot(x="name",y="bal",data=df,color="yellow")
    plt.subplot(2,2,2)
    sns.distplot(df["bal"],color="red")
    plt.subplot(2,2,3)
    plt.scatter(df['name'],df['bal'],marker='*',color='blue')
    plt.xlabel('name')
    plt.ylabel('balance')
    plt.subplot(2,2,4)
    plt.pie(df['bal'],labels=df['name'])
    plt.show()
#------------------------------------------------------#
def graph_account():
    df=pd.read_csv(r"C:\project\bankfile.csv")
    plt.figure(figsize=(10,5))
    sns.scatterplot(x="name",y="bal",data=df,markers='*',color='black')
    sns.lineplot(x="name",y="bal",data=df)
    sns.barplot(x="name",y="bal",data=df)
    plt.show()
#----------------------------------------------------------------#
def graph_staff():
    df=pd.read_csv(r"C:\project\stafffile.csv")
    plt.figure(figsize=(10,5))
    sns.scatterplot(x="name",y="salary",data=df,markers='*',color='black')
    sns.lineplot(x="name",y="salary",data=df)
    sns.barplot(x="name",y="salary",data=df)
    plt.show()
#---------------------------------------------------------#
while True:
    a=show_option()
    if a==1:
        if login_manager():
            while True:
                ch=showMenu_manager() 
                if ch==1:
                    bankcsv()
                elif ch==2:
                    new_acholder()
                elif ch==3:
                    removeaccount()
                elif ch==4:
                    showstaff()
                elif ch==5:
                    new_staff()
                elif ch==6:
                    removestaff()
                elif ch==7:
                    graph_account()
                elif ch==8:
                    graph_staff()
                elif ch==9:
                    break
                else:
                    print("Invalid option")
                
        break
    elif a==2:
        if login_staff():
            while True:
                ch=showMenu_staff()
                if ch==1:
                    bankcsv()  
                elif ch==2:
                    sort_name()
                elif ch==3:
                    new_acholder()
                elif ch==4:
                    removeaccount()
                elif ch==5:
                    all_graph()
                elif ch==6:
                    graph_account()
                elif ch==7:
                    break
                else:
                    print("Invalid option")
        break
    elif a==3:
        if login_user():
            while True:
                ch=showMenu_user()
                if ch==1:
                    show_account()
                elif ch==2:
                    withdraw() 
                elif ch==3:
                    deposit()
                elif ch==4:
                    break
                else:
                    print("Invalid option")
        break
    else:
        print("invalid option")
