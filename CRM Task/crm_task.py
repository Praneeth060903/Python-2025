customerId = input("Enter Customer ID: ")
customerName = input("Enter Customer Name: ")

isPremium_input = input("Premium Customer ? (yes/no)")
isPremium = True if isPremium_input == "yes" else False

yearsPartnership = int(input("Enter yearsPartnership:"))
dealStage = input("proposal/negotiation/closed :")
dealValue = int(input("Original Value of Deal :"))
discount=0.0

if isPremium == "yes":
    base_discount = 0.10
    
elif yearsPartnership >= 3:
    base_discount = 0.05
    
else:
    base_discount = 0.0
    
match dealStage:
    case "proposal":
        extra_discount = 0.02
    case "negotitaion":
        extra_discount = 0.03
    case "closed":
        extra_discount = 0.05

final_discount = base_discount * extra_discount
deal_value = dealValue * (1-final_discount)

print(f"customerId: {customerId}")
print(f"customerName: {customerName}")
print(f"Premium Customer: {'Yes' if isPremium else 'No'}")
print(f"Years of Partnership:{yearsPartnership}")
print(f"Deal Stage: {dealStage}")
print(f"Original Deal value: {dealValue}")
print(f"final discount:{final_discount}")
print(f"Deal Value : {deal_value}")