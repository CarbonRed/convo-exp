bill = 0
temp = 0
cart = []
price = {"chicken": 200, "biscuit": 50, "shrimp": 75, 'juice': 150, 'wings': 125}
bot_greeting = "Welcome to AutoDyne chicken, how may i assist you today?"

print(bot_greeting)

while True:
    request = input("Your request:").lower().strip()

    if "wings" in request:
        bill += price["wings"]
        cart.append("wings")
        temp = price["wings"]
        print('Bot: wings has been added to your order, anything else')

    if "shrimp" in request:
        bill += price["shrimp"]
        cart.append("shrimp")
        temp = price["shrimp"]
        print('Bot: shrimp has been added to your order, anything else')

    if "chicken" in request:
        bill += price["chicken"]
        cart.append("chicken")
        temp = price["chicken"]
        print('Bot: Chicken has been added to your order, anything else')

    if "biscuit" in request:
        bill += price["biscuit"]
        cart.append("biscuit")
        temp = price["biscuit"]
        print('Bot: biscuit has been added to your order, anything else')

    if "juice" in request:
        bill += price["juice"]
        cart.append("juice")
        temp = price["juice"]
        print('Bot: juice has been added to your order, anything else')

    if "remove last" in request:
        cart.pop()
        bill -= temp
        print("order:")
        for x in cart:
            print(x)
        print(f"Your bill: {bill}")
        print("bot: ok, your last request has been canceled, is that ok ")

    if "checkout" in request:
        print("order:")
        for x in cart:
            print(x)
        print(f"Your bill: {bill}")

    if "description c" in request:
        print("chicken price: 200")

    if "description w" in request:
        print("wings price: 125")

    if "description b" in request:
        print("biscuit price: 50")

    if "description j" in request:
        print("juice price : 150 ")

    if "description s" in request:
        print("shrimp price: 75")

    if "menu" in request:
        print(""""
Item            Price       
Chicken         200
Biscuit         100
Juice           150
       """)
