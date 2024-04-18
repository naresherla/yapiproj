import sys
class DepositError(Exception):pass
class WithDrawError(BaseException):pass
class InsuffFundsError(Exception):pass
import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='tiger',
                             database='bank_management',
                             )
def menu():
    print("*"*50)
    print('''
        1.Open New tables 
        2.Deposit Amount
        3.Withdraw Amount
        4.Balance Enquiry
        5.Show customer details
        6.Close an account
        7.exit
        ''')
    print("*" * 50)

def openacc():
    n=input("Enter the name:")
    ac=int(input("Enter the Account number:"))
    db=input("Enter the Date of Birth:")
    add=input("Enter the Address:")
    ch=int(input("Enter ur contact number:"))
    ob=int(input("Enter the opening balance:"))
    if ob >=500:
        x=mydb.cursor()
        x.execute("insert into account values('%s',%d,'%s','%s',%d,%f)" %(n,ac,db,add,ch,ob))
        x.execute("insert into amount values('%s',%d,%f)" %(n,ac,ob))
        mydb.commit()
        print("Data Entered Successfully.........")
    else:
        print("opening balance should be greater than or equal to 500")
def despamo():
    global ob
    amount=int(input("enter the amount you want to deposit:"))
    if(amount<=0):
        raise DepositError
    else:
        global ob
        ac=int(input("enter the account no:"))
        a="select Baccountalance from amount where Accno=%d"
        x=mydb.cursor()
        x.execute(a %(ac))
        result=x.fetchone()
        t=result[0]+amount+ob
        s=('update amount set Baccountalance=%d where Accno=%d')
        x.execute(s %(t,ac))
        mydb.commit()
        print("your Account {} is credited with INR:{}".format(ac,amount))
        print("Now ur Account {} bal after deposit INR:{}".format(ac,t))
def withdrawamount():
    global ob,t
    ac = int(input("enter the account no:"))
    a = 'select Baccountalance from amount where Accno=%d'
    x = mydb.cursor()
    x.execute(a % (ac))
    result = x.fetchone()
    t = result[0]
    amount =int(input("enter the amount you want to withdraw:"))
    if(amount<=0):
        raise WithDrawError
    elif (amount+500)>t:
        raise InsuffFundsError
    else:
        wd = t - amount
        sq = ('update amount set Baccountalance=%d where Accno=%d')
        x.execute(sq % (wd, ac))
        mydb.commit()
        print("ur Account {} Debited with INR:{}".format(ac,amount))
        print("now ur Account {}  balance after Withdraw INR:{}".format(ac,wd))
def balenq():
    global min_bal
    ac=int(input("Enter the account no:"))
    a='select * from amount where Accno=%d'
    x=mydb.cursor()
    x.execute(a %(ac))
    result=x.fetchone()
    print("Balance for account ",ac,"is",result[-1])
def displaydetails():
    ac = int(input("Enter the account no:"))
    a = 'select * from account where Accno=%d'
    x = mydb.cursor()
    x.execute(a %(ac))
    result = x.fetchone()
    print(result)
    print("*"*20)
    print("Name:",result[0])
    print("Account number:",result[1])
    print("Date of birth:",result[2])
    print("Address:",result[3])
    print("Contact number:",result[4])
def closeaccount():
    ac = int(input("Enter the account no:"))
    sql1='delete from account where Accno=%d'
    sql2 = 'delete from amount where Accno=%d'
    x = mydb.cursor()
    x.execute(sql1 %(ac))
    x.execute(sql2 %(ac))
    mydb.commit()
def wish():
    print("Thanks for using our services please visit again!!!!")


while(True):
    menu()
    try:
        ch=int(input("Enter ur choice:"))
        match(ch):
            case 1:
                openacc()
            case 2:
                try:
                    despamo()
                except DepositError:
                    print("Don't enter -ve or zero for deposit amount")
                except ValueError:
                    print("Dont try to withdraw alnums,strs and special symbols from account")
            case 3:
                try:
                    withdrawamount()
                except WithDrawError:
                    print("Dont enter -ve or Zero for withdrawing amount")
                except InsuffFundsError:
                    print("Ur account does not have sufficient funds ---please try again later")
                except ValueError:
                    print("Dont try to withdraw alnums,strs and special symbols from account")
            case 4:
                balenq()
            case 5:
                displaydetails()
            case 6:
                closeaccount()
            case 7:
                wish()
                sys.exit()
            case _:
                print("Ur selection of operation wrong---try again ")
    except ValueError:
        print("ur choice of operation should not be alnums,strs,symbols")