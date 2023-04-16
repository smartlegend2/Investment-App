# This is an Investment build with python 
# it collects user data like name  and pin for its operations
# It give access to user for Transactions with realirebility of it's services
# >> Let's Write the Code <<

#This is the Homepage of this App displaying grreetings to the User

print(">>> YOU ARE WELCOME TO COHORT5 INVWSTMENT APP <<<") 

                  # Here creatings values to different variables
Trials = 3        # Total Attempts for Pin number input tto access th eApp
Userpin = 4321    # keypin to gain access to the app
BalanceIwallet = 5000    # Account Opens with #5000 im balance
rate = 0.5        # for every depsit you have 50% (Percentage) increament
vat = 0.07        # for every W ithdrawal There is Charges of 7% VAT Deduction

choice = " "      # Assigned an empty string value to choice for operations of this App
   # Here colects user assigned pin number

while Trials != 0:
    pin = int(input("Please Enter Your 4 digit pin Number: ")) 
    if pin != Userpin:
       Trials-= 1
       print("Wrong pin Number", Trials, "Trials Left")
    else:                                                     
       while choice != "4":
          print("1.Deposit amount")
          print("2.Withdraw amount")
          print("3.Display the current balance")
          print("4.Exit")
  # Here prompt the user for choice of transaction        
          choice = input("Please Enter your choice: ") 

  # Prompt User for data colection for deposit Transaction
          if (choice == "1"):                                                             
             WAllet_name = input(" Please Enter Your Name: ")
             amount_deposited = float (input("Please Enter How Much You Want to Deposit:# "))
             percentage_increase = amount_deposited*rate
           
  # Here The percentage Increase Takes effect and added to the user balance          
             if amount_deposited > 0:
                BalanceIwallet = amount_deposited + percentage_increase + BalanceIwallet          
                print(WAllet_name,"Your Deposit Is Successful! Your Now Have Total balance Of #", BalanceIwallet,"In Your Wallet" )
             else:
                print('Sorry Yur Entered non Positive Number')

  # Here Prompts User for Data colection for withdrawal Transaction           
          elif(choice == "2"):                                                             
             Wallet_Name = input("please Enter Your Account Name: ")
             Amount_to_withdraw = float(input( "How Much Amount Are You Willing To Withdraw From Your Account:# "))
             vat = 0.07
             vat_per_calc = Amount_to_withdraw * vat 

  # Here the VAt takes effect and be Deducted from the Wallet         
             if Amount_to_withdraw > 0:
                if(BalanceIwallet - Amount_to_withdraw)>= 0:
                    BalanceIwallet = BalanceIwallet - vat_per_calc - Amount_to_withdraw    
                    print("Thanks!After VAT Deduction Your Balance Is #",BalanceIwallet)
                else:
                   print("There Is Not Enough Money In Your Wallet, Please! Fund you Wallet")

  # Here Shows That -ve values  inputed                
             else:
                print("The Amount Entered Is Not a positive Value")                          

  # Equiry For Blalance
          elif(choice == "3"):
            Wallet_Name = input("Please Enter Your Wallet Name: ")                          

            print( "Thanks For Your Enquiry! Your Current Balance Is:#", BalanceIwallet)

  # Here Log You Out Of The System           
          elif(choice == "4"):
             print("Thank you for using our app, Bye!" )
          else:
             print(">>> Wrong Selection.. Please! Select Correct Option From >>> THE CHOICE MENU. THANK YOU!!! <<<")
