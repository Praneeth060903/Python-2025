customerId = input("Enter Customer ID: ")
customerName = input("Enter Customer Name: ")

isPremium_input = input("Premium Customer ? (yes/no)")
isPremium = isPremium_input == "yes"

yearsPartnership = int(input("Enter yearsPartnership:"))
dealStage = input("proposal/negotiation/closed :")
dealValue = int(input("Original Value of Deal :"))
discount=0.0

if isPremium == "yes":
    base_discount = 0.10
    print(f"Customer is Eligible for 10% discount")

elif isPremium == "no":
    base_discount = 0.05
    print(f"Customer is Eligible for 5% discount")

else:
    base_discount = 0.0
    print(f"Customer is not eligible for discount")

match dealStage:
    case "proposal":
        discount += 0.02
    case "negotitaion":
        discount += 0.03
    case "closed":
        discount += 0.05

final_discount = base_discount * discount
deal_value = dealValue * (1-final_discount)

print(f"customerId: {customerId}")
print(f"customerName: {customerName}")
print(f"Premium Customer: {'Yes' if isPremium else 'No'}")
print(f"Years of Partnership:{yearsPartnership}")
print(f"Deal Stage: {dealStage}")
print(f"Original Deal value: {dealValue}")
print(f"final discount:{final_discount}")
print(f"Deal Value : {deal_value}")