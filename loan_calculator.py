from math import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", help="type",)
parser.add_argument("--principal", help="principal", type=int)
parser.add_argument("--periods", help="periods", type=int)
parser.add_argument("--interest", help="interest", type=float)
parser.add_argument("--payment", help="payment", type=float)

args = parser.parse_args()
ann_or_diff = args.type
principal = args.principal
periods = args.periods
interest = args.interest
payment = args.payment
total_payment = 0

#  calculate_question = input('''What do you want to calculate?
#  type "p" - for loan principal,
#  type "a" - for annuity monthly payment amount,
#  type "n" - number of monthly payments:''')
if ann_or_diff == "annuity":
    #  number of periods calculating
    if periods == None and principal > 0 and payment > 0 and interest != None:
        loan_principal = principal
        monthly_payment = payment
        loan_interest = interest
  
        i = loan_interest / 100 / 12  # * loan_interest
        n = log(float(monthly_payment) / (float(monthly_payment) - i * float(loan_principal)), 1 + i)
    
        years = floor(n / 12)
        months = ceil(n - (years * 12))

        while months >= 12:
            years += 1
            months -=12
        
        y = years
        m = months
        years = str(years) + " year"
        months = str(months) + " month"

        if y > 1:
            years += "s"
        if m > 1:
            months += "s"
        if y >= 1 and m >= 1:
            print(f"It will take {years} and {months} to repay this loan!")
        elif y == 0 and m >= 1:
            print(f"It will take {months} to repay this loan!")
        elif y >= 1 and m == 0:
            print(f"It will take {years} to repay this loan!")
        overpayment = (ceil(monthly_payment) * ceil(n)) - loan_principal
        print(f"Overpayment = {round(overpayment)}")

    #  Principal calculation   
    elif principal == None and payment > 0 and periods > 0 and interest != None:
        annuity_payment = payment
        number_periods = periods
        loan_interest = interest
        i = loan_interest / 12 / 100
        loan_principal = floor(annuity_payment / ((i * pow(1 + i, number_periods)) / (pow(1 + i, number_periods) - 1)))
        print(f"Your loan principal is {loan_principal}!")
        overpayment = (ceil(payment) * number_periods) - loan_principal
        print(f"Overpayment = {round(overpayment)}")

    #  Monthly payment calculation
    elif payment == None and principal > 0 and periods > 0 and interest != None:
        loan_principal = principal
        number_periods = periods
        loan_interest = interest
        i = loan_interest / 12 / 100
        payment = loan_principal * (i * pow(1 + i, number_periods) / (pow(1 + i, number_periods) - 1))
        print(f"Your annuity payment is {ceil(payment)}!")
        overpayment = (ceil(payment) * number_periods) - loan_principal
        print(f"Overpayment = {round(overpayment)}")

    else:
        print("Incorrect parameters")

#   differentiate payment
if ann_or_diff == "diff" and interest != None and interest > 0 and principal > 0  and periods > 0 and payment == None:
    i = interest / 12 / 100
    month_num = 1
    for x in range(periods):
        monthly_payment = ceil((principal / periods) + (i * (principal - ((principal * (month_num - 1)) / periods))))
        print("Month", month_num, ": payment is ", monthly_payment)
        month_num += 1
        total_payment += monthly_payment
    print()
    print("Overpayment =", total_payment - principal)

else:
    print("Incorrect parameters")
