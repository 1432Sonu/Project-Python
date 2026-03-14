print('Currency converter')

print("1. INR to USD")
print("2. USD to INR")
print("3. INR to EUR")
print("4. EUR to INR")
print("5. INR to USD")
print("6. YEN to INR")
print("7. INR to RUB")
print("8. RUB to INR")
print("9. PKR to INR")
print("10. INR to PKR")

choice = int(input("Choose coversion (1-10): "))
amount = float(input("Enter Amount : "))

# Exchange rates
inr_to_usd = 0.012
usd_to_inr = 83.0
inr_to_eur = 0.011
eur_to_inr = 90.0
inr_to_yen = 1.80
yen_to_inr = 0.58
inr_to_rub = 0.86
rub_to_inr = 1.16
pkr_to_inr = 0.33
inr_to_pkr = 3.03

if choice == 1:
    result = amount * usd_to_inr
    print("USD =", result)

elif choice == 2:
    result = amount * inr_to_usd
    print("INR =", result)

elif choice == 3:
    result = amount * inr_to_eur
    print("EUR = ", result)

elif choice == 4:
    result = amount * eur_to_inr
    print("INR = ", result)

elif choice == 5:
    result = amount * inr_to_yen
    print("YEN = ", result)

elif choice == 6:
    result = amount * yen_to_inr
    print("INR = ", result)

elif choice == 7:
    result = amount * rub_to_inr
    print("RUB = ", result)

elif choice == 8:
    result = amount * inr_to_rub
    print("INR = ", result)    

elif choice == 9:
    result = amount * pkr_to_inr
    print("INR =", result)

elif choice == 10:
    result = amount * inr_to_pkr
    print("PKR =", result)

else:
    print("Invalid choice")    