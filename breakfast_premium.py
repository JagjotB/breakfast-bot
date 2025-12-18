print("Hello! I am Bob, the Breakfast Bot. \n"
      "Today we have two breakfast options available. \n"
      "The firt is waffles with strawberries and whipped cream. \n" 
      "The second is pancakes with butter and syrup. \n")
while True:
    response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
    if "waffles" in response:
        print("Waffles it is!")
        break
    elif "pancakes" in response:
        print("Pancakes it is! \n Your order will  be ready shortly")
        break
    else:
        print("Sorry, that's not on our menu.")

print("Your order will be ready shortly.")