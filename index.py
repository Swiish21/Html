# a program that receives funds(via integer input) then divides it into different accounts depending on user instructions, returning balances

customer_deposit = int(input("Enter amount deposited in dollars:\n"))
print(f"Dear customer we have received a deposit of {customer_deposit} dollars, please proceed in diving the funds.")
print("select 1 for savings, 2 for mortgage, 3 for fixed, 4 for all accounts")
print("select 12 for savings & mortgage, 13 for savings & fixed, 23 for mortgage & fixed")
which_acc_to_depo = int(input("Which account(s) would you like to deposit to(mortgage,savings,fixed):\n"))

if which_acc_to_depo == 3:
    print(f"A total of {customer_deposit} dollars has been deposited to your fixed account.")
elif which_acc_to_depo == 2:
    print(f"A total of {customer_deposit} dollars has been deposited to your mortgage account.")
elif which_acc_to_depo == 1:
    print(f"A total of {customer_deposit} dollars has been deposited to your savings account.")
elif which_acc_to_depo == 12:
    print("Please select what percent to deposited to each account!")
    mortgage_acc = int(input("What percent would you like to deduct from funds to mortgage(5,10,15,20...):\n"))
    mortgage_amount = (mortgage_acc/100)*customer_deposit
    print(f"{mortgage_acc} percent was deposited to your mortgage account which is a total of {mortgage_amount} dollars.")
    rem_amount1 = customer_deposit - mortgage_amount
    print(f"Dear customer, you have a balance of {rem_amount1} dollars after the above deposit,")
    quest1 = input("Would you like to deposit the rest to your savings account(yes/no):\n")
    if quest1 == "yes":
        print(f"{rem_amount1} dollars has been transferred to your savings")
    elif quest1 == "no":
        savings_acc = int(input("What percent to deduct from remaining funds to savings,remaining funds are automatically sent to fixed account(5,10,15,20...):\n"))
        savings_amount = (savings_acc/100)*rem_amount1
        rem_amount2 = rem_amount1-savings_amount
        print(f"{savings_acc} percent was deposited to savings account which is a total of {savings_amount} dollars.")
        print(f"Remaining balance of {rem_amount2} dollars was automatically deposited to your fixed account")
elif which_acc_to_depo == 13:
    print("Please select what percent to deposited to each account!")
    savings_acc = int(input("What percent would you like to deduct from funds to savings(5,10,15,20...):\n"))
    savings_amount = (savings_acc/100)*customer_deposit
    print(f"{savings_acc} percent was deposited to your savings account which is a total of {savings_amount} dollars.")
    rem_amount1 = customer_deposit - savings_amount
    print(f"Dear customer, you have a balance of {rem_amount1} dollars after the above deposit,")
    print(f"{rem_amount1} dollars has been automatically transferred to your fixed account")
elif which_acc_to_depo == 23:
    print("Please select what percent to deposited to each account!")
    mortgage_acc = int(input("What percent would you like to deduct from funds to mortgage(5,10,15,20...):\n"))
    mortgage_amount = (mortgage_acc/100)*customer_deposit
    print(f"{mortgage_acc} percent was deposited to your mortgage account which is a total of {mortgage_amount} dollars.")
    rem_amount1 = customer_deposit - mortgage_amount
    print(f"Dear customer, you have a balance of {rem_amount1} dollars after the above deposit,")
    print(f"Remaining balance of {rem_amount1} dollars was automatically deposited to your fixed account")
elif which_acc_to_depo == 4:
    print("Please select what percent to deposited to each account!")
    mortgage_acc = int(input("What percent would you like to deduct from funds to mortgage(5,10,15,20...):\n"))
    mortgage_amount = (mortgage_acc/100)*customer_deposit
    print(f"{mortgage_acc} percent was deposited to your mortgage account which is a total of {mortgage_amount} dollars.")
    rem1 = customer_deposit-mortgage_amount
    print(f"Your account balance is now {rem1} dollars")
    fixed_acc = int(input(f"What percent would you like to deduct from balance ${rem1} to fixed acc(5,10,15,20...):\n"))
    fixed_amount = (fixed_acc/100)*rem1
    print(f"{fixed_acc} percent was deposited to your fixed account which is a total of {fixed_amount} dollars.")
    rem2 = rem1-fixed_amount
    savings_acc = int(input(f"What percent would you like to deduct from balance ${rem2} to savings(5,10,15,20...):\n"))
    savings_amount = (savings_acc/100)*rem2
    print(f"{savings_acc} percent was deposited to your savings which is a total of {savings_amount} dollars.")
    rem3 = rem2 - savings_amount
    if rem3 <= 0:
        print("All funds have been successfully divided, thank you for banking with us!")
    elif rem3 > 0:
        fixed_amount = fixed_amount + rem3
        print(f"Your balance of {rem3} dollars has been automatically transferred to your fixed account.")
        print(f"Your new account balances are: Fixed - ${fixed_amount}, Savings - ${savings_amount}, Mortgage - ${mortgage_amount}")
else:
    print("Wrong Input, Please try again!")