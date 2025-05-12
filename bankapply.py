# Balance=0
# def generate_userid():
#   UserIds=[]
#   #get alluserid from user.txt and store it in userIds
#   while True:
#     userid= f"U{random.randint(1,100)}"

#     if userid not in UserIds:
#         return userid

###########################cereate the account to customers########################
Balance=0
def Customer_Create():
      global Balance
      first_Name=input('enter Your first name:-')
      last_Name=input('enter the your last name:-')
      Address=input('enter your Address:-')
      Password=int(input('enter your password:-'))
      Initial_Balance=int(input('enetr the  amount:-'))
      Balance+=Initial_Balance
  ####################################save the customers deatils on File##########################  
   
      with open('userspersonal','a')as users_personal:
          users_personal.write(f',{first_Name},{last_Name},{Address}\n')

      with open('userssecure.txt','a')as Users_secure:
          Users_secure.write(f' ,{Password},{Balance}\n')
     
      with open('save the Balance.txt','a')as balancefile:
            balancefile.write(f' initial_balance:{Balance}')
      print(f" Helloo {first_Name} sucessfully created your account  ") 
      Customer_Option()
     

##########################################Deposite#########################################
def Deposite():
  global Balance
  while True:
      
      password=int(input('enter the your Password number'))
      if password==Customer_Create
        try:
            amount=int(input('enter the amount') )      
            if amount>0:
                  Balance+=amount
                  print(f'sucessfully deposited :{amount}')
                  break
            else:
                    print(f"invalid deposite try again")
                    
        except ValueError:
                  print('enter the number only')     
        else:
          print(f"check your id number")
          
        with open('save the balance.txt','a')as balancefile:
              balancefile.write(f"{Balance},deposited:-{amount}")    
        return Balance




# #########################withdrawal########################################### 
# def Withdraw():  
#    global balance
#    while True:
#       newuser_id=generate_userid()
#       usersid=input('enter the yourid')
#       if newuser_id==usersid:
#         try:
#             cash=int(input('enter the cash') )      
#             if cash>0:
#                   Balance+=cash
#                   print(f'sucessfully withdrawal:{cash}')
#                   break
#             else:
#                     print(f" cheack the Balance ")
                    
#         except ValueError:
#                   print('enter the number only')     
#         else:
#           print(f"check your id number")
          
#         with open('save the balance.txt','a')as balancefile:
#                 balancefile.write(f"{newuser_id},{Balance}withdrawal amount:-{cash}") 


# ###########################################################################################################333333
# ################################################################################################################
#choose the option for admin#
def Choose_Admin():
        while True:
            print(f'\n====choose the option=====\n')
            print('1.Create the account')
            print('2.tarnscations history')
            print('3.Exit')

            try:
                choice=int(input('enter the user choice 1 to 3 '))
            
                if choice==1:
                    Customer_Create()
                # elif choice==2:
                #     Transactions_History()
                elif choice==3:
                    print("Thanks For Using  our bank")  
                    break
                else:
                    print('invalid number enter number 1 to 3')
            except ValueError:
                        print("enter the numbers only")
def Admin_Login():
    Username='Kanna'
    Userid=3102
    while True:
        name=input('enter the name:-')
        user_id=int(input('enter your id:-'))
        if name==Username and user_id==Userid:
            print("sucessfully created ")
            Choose_Admin()
            break
        else:
         print('please check your ID,Name')
      



#########choose the option for customer##########################################
def Customer_Option():
    while True:
        print(f'\n===choose Your  option===\n')
        print('1.Deposite Money')
        print('2.withdrawal')
        print('3.check the Balance')
        print('4.Exit')

        try:
            choose=int(input('enetr the option 1 to 3:-'))

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
            print("only enter the numbers only ")

# ###########################Signup For Signup###########################

# def Customers_Signup():
#     # userid=input('enter the  your id')
#     # User_id=generate_userid()
#     if userid==User_id:
#         print('choose your options')
#         Customer_Option()
#     else:
#         print('Not Found your account firstly create the account')
#         Customer_Create()
# ###########################Banking Menu####################################################################
# def Front_Menu():
#     while True:
#             print(f'\n====== Welcome=====\n')
#             print('1.Admin signup')
#             print('2.Customer signup')
#             print('3.Exit')

#             try:
#                 choose=int(input("enter your options:-"))

#                 if choose==1:
#                      Admin_Login()
#                 elif choose==2:
#                     Customers_Signup()
#                 elif choose==3:
#                     print('Thanks for using our bank')
#                     break
#                 else:
#                     print('invalid number enter the number 1 to 3')
#             except ValueError:
#                   print('only enter the numbers 1 to 3')
# Front_Menu()

Customer_Create()