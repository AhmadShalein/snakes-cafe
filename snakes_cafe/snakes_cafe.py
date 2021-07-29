print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************""")

menu = [{'type':'Appetizers','foods':['Wings','Cookies','Spring Rolls',]},{'type':'Entrees','foods':['Salmon','Steak','Meat Tornado','A Literal Garden',]},{'type':'Desserts','foods':['Ice Cream','Cake','Pie',]},{'type':'Drinks','foods':['Coffee','Tea','Unicorn Tears',]},]

print("""Appetizers
----------
Wings
Cookies
Spring Rolls
""")

print("""Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
""")

print("""Desserts
--------
Ice Cream
Cake
Pie
""")

print("""Drinks
------
Coffee
Tea
Unicorn Tears
""")

orderlist = []
counter = 0
flag = 1
while flag == 1:
    order = input("""***********************************
    ** What would you like to order? **
    ***********************************
    >""")

    if order == "quit":
        flag = 0
        break
    else:
        for foodtype in menu:
            for kind in foodtype["foods"]:
                if order.lower() == kind.lower():
                    orderlist.append(order)
                    if order in orderlist:
                        counter = orderlist.count(order)
                        print(f"** {counter} orders of {order} has\have been added to your meal **")
                        break
                    else:
                        print(f"** {counter} orders of {order} has\have been added to your meal **")
