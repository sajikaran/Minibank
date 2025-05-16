Customers_data={}
Balance=0

def Front_Menu():
    while True:
            print(f'\n====== Welcome to our Banking Platform=====\n')
            print('1.Admin signup')
            print('2.Customer signin')
            print('3.Exit')

            try:
                choose=int(input("enter your options:-"))

                if choose==1:
                     Admin_Signin()
                elif choose==2:
                    Customers_Signin()
                elif choose==3:
                    print('Thanks for using our bank')
                    break
                else:
                    print('invalid number enter the number 1 to 3')
            except ValueError:
                  print('only enter the numbers 1 to 3')

def Admin_Signin():
    User_Name='Kanna'
    User_Id=3102
    while True:
        name=input('enter the name:-')
        user_id=int(input('enter your id:-'))
        if name==User_Name and user_id==User_Id:
            print("sucessfully created ")
            Admin_Choose()
            break
        else:
         print('please  Nead to check your ID,Name')

def Admin_Choose():
        while True:
            print(f'\n====choose the options=====\n')
            print('1.Create the account')
            print('2.Exit')

            try:
                choice=int(input('enter the user choice 1 0r 2:-'))
            
                if choice==1:
                    Customers_personal()
                elif choice==2:
                    print("Thanks For Using  our bank")  
                    break
                else:
                    print('invalid number enter number 1 to 3')
            except ValueError:
                        print("enter the numbers only")

def Customers_Signin():
    global Customers_data

    userid = input('Enter your personal ID:-')
    password = input('Enter your password:-')

    if userid in Customers_data and password == Customers_data[userid]['password']:
        print('You are already our customer.')
        Customer_Option()
    else:
        print('Account not found. You need to create an account first.')
        Customer_Create()


##############################Customers Choosing a Options########################################

def Customer_Option():
    while True:
        print(f'\n===choose Your  options===\n')
        print('1.Deposite Money')
        print('2.withdrawal')
        print('3.check the Balance')
        print('4.Exit')

        try:
            choose=int(input('enter  the options 1 to 4:-'))

            if choose==1:
                Deposite()
            elif choose==2:
                Withdraw()
            elif choose==3:
                Check_Balance()
            elif choose==4:
                 print('Thanks For using our bank')
                 break        
            else:
                print('Invalid number enter the number 1 to 4:-')
                
        except ValueError:
            print( 'Only  Enter The Numbers')

#########################Create the accounts For customers ########################
def Customer_Create():
    global Balance
    global Customers_data


    first_Name=input('enter Your first name:-')
    last_Name=input('enter the your last name:-')
    Address=input('enter your Address:-')
    Password=input('enter your password:-')
    NIC_Number=input('enter the NIC number:- ')
    Initial_Amount=float(input( 'Enter the amount for the Savings:-'))
    Balance+=Initial_Amount
    User_Id=(f'{int(NIC_Number)+6758}'.zfill(9))
    print(f'Sucessfully created your account This is Your Personal Id {User_Id}')
      

    return   {User_Id:{
        'first_name': first_Name,
        'last_name': last_Name,
        'address': Address,
        'password': Password,
        'Balance': Balance}}
        

def Customers_personal():
    global Customers_data
    Customers_details = Customer_Create()
    Customers_data.update(Customers_details)
    with open('customers.txt', 'a') as customers_file:
        customers_file.write(f"{Customers_data}")
        

    # with open('transactions.txt', 'a') as transactions_file:                      ####################################(i couldn't save the File in
    # transactions_file.write(f"U {Customers_data[5]}\n, Current_Amount:- {Customers_data[4]}\n"############################# Dictionaries keys and values##                                                                          
    
######################################Deposite########################################          
def Deposite(): 
    global Balance
    
    try:
        amount=float(input('enter your amount:-') )      
        if amount>0:
            Balance+=amount
            print(f'sucessfully Deposited Your {amount}...')
            with open('UsersTranscations.txt','a')as Users_transcations:
                Users_transcations.write(f"Deposited:- {amount}\n") 
        elif amount<=0:
           print('Only Enter the amount grater than 0')
    
        else:        
            print(f" you can deposite the amount grater than 0 ")
                        
    except ValueError:
                    print('enter the number only')     

##########################Withdrawal###########################################
def Withdraw(): 
    global Balance
    
    try:

        cash=float(input('enter the cash:-') )      
        if cash<=Balance:
            Balance-=cash

            print(f'sucessfully withdrawal:{cash}')
            with open('UsersTranscations.txt','a')as Users_transcations:
                Users_transcations.write(f" ,withdraw_amount:-{cash}\n") 
        elif cash<=0:
            print('cash only grater than 0')

        else:        
            print(f" Insufficiants amount check your Current Balance ")
                        
    except ValueError:
                    print('enter the number only')     

# #####################Check the Balance############################################                    
def Check_Balance():
            global Balance

            print(f' Your Current Balnce:-{Balance}')

            with open('UsersTranscations.txt','a')as Users_transcations:
                Users_transcations.write(f' Current Balance:-{Balance}\n')


# def Transcations_History():
#     with open('UsersTranscation.txt','r')as Users_transcations:
#        Money_transer=Users_transcations.readlines().split()
#        print(Money_transer)     [ i counldn't finish them ]

