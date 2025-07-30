price_car = 2007695
down_payment = 500000
rate_of_interest = 8
no_of_months = 5
#simple = (price_car - down_payment) * (1 + (rate_of_interest * no_of_months))
#total = (price_car - down_payment) + simple
#monthly = total / (no_of_months * 12)

loan_amount = price_car - down_payment
months = no_of_months * 12
montly = rate_of_interest / (12*100)

emi = (loan_amount * montly * ((1 + montly) ** months)) / (((1 + montly) ** months) -1 )

payable_amount = emi * months
print("======================================")
print(f"Car Price : {price_car}")
print(f"Down Payment : {down_payment}")
print(f"Loan Years : {no_of_months} years")
print(f"Rate of interest : {rate_of_interest}%")
print(f"Total Amount : {payable_amount}")
print(f"EMI : {emi}")