fee = float(input("Enter resturant fee:"))
ampay = float(input("Enter amount you paid:"))
result = ampay - fee
if result == 0.0:
    print("You have paid the needed amount")
if result < 0.0:
    restr=str(result)
    print(f"You still need to pay {restr[1::]}")
if result > 0.0:
    print(f"You have to expect change of {result}")
