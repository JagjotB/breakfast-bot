import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfast options available.")
print_pause("The first is waffles with strawberries and whipped cream.") 
print_pause("The second is pancakes with butter and syrup.")

while True:
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
    time.sleep(1)
    while True:
        order_again = input("Would you like to place another order? (yes/no)\n").lower()
        if 'no' in order_again:
            print ("Ok, goodbye!")
            time.sleep(1)
            break
        
        elif 'yes' in order_again:
            print("Very good, I'm happy to take another order.")
            time.sleep(1)
            break
        
        else:
            print("Sorry, I didn't understand that.")
            time.sleep(1)
    if 'no' in order_again:
        break