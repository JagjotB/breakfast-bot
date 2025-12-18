while True:
    response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
    if "waffles" in response:
        print("Waffles it is!")
        break
    elif "pancakes" in response:
        print("Pancakes it is!")
        break
    else:
        print("Sorry, that's not on our menu.")