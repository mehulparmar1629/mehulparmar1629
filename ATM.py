list = [1234,2345,4567,7890]
user = int(input("Enter your Pin: "))
if user in list:
    amount = int(input("Enter your Amount: "))
    print("1.Withdraw 2.Deposite")
    choice = int(input("Enter your Choice: "))
    if choice==1:
        change_amount = int(input("Enter Your WithDraw amount: "))
        if amount<change_amount:
            print("The amount is larger than total amount")
        else:
            withdraw = amount-change_amount
            print("After WithDraw Amount",withdraw)
    elif choice==2:
        Deposite_amount = int(input("Enter Your Deposite Amount: "))
        deposite = amount + Deposite_amount
        print("After Deposite Amount",deposite)
    else:
        print("Please Enter the valid choice!!")
else:
    print("Your Pin is Invalid")    
