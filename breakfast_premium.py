import time

print("Hello! I am Bob, the Breakfast Bot.")
time.sleep(1)
print("Today we have two breakfast options available.")
time.sleep(1)
print("The firt is waffles with strawberries and whipped cream.") 
time.sleep(1)
print("The second is pancakes with butter and syrup.")
time.sleep(1)
while True:
    response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
    if "waffles" in response:
        print("Waffles it is!")
        time.sleep(1)
        break
    elif "pancakes" in response:
        print("Pancakes it is!")
        time.sleep(1)
        break
    else:
        print("Sorry, that's not on our menu.")
        time.sleep(1)

print("Your order will be ready shortly.")