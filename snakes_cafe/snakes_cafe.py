print('\n \n ************************************** \n **    Welcome to the Snakes Cafe!   ** \n **    Please see our menu below.    ** \n ** \n ** To quit at any time, type "quit" ** \n **************************************\n')

menu = {
  'Appetizers': {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0},
  'Entrees': {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A Literal Garden': 0},
  'Desserts': {'Ice Cream': 0, 'Cake': 0, 'Pie': 0},
  'Drinks': {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}
}

for element in menu:
    print(element)
    print("-" * len(element))
    for item in menu[element]:
        print(item)

print('\n \n *********************************** \n ** What would you like to order? ** \n ***********************************\n')

response = input(">").lower()

while response != 'quit':

  for key in menu.keys():

    if response in menu[key].keys():

      menu[key][response]+= 1

      if menu[key][response] == 1:
        print(f'** {menu[key][response]} order of {response} has been added to your meal **')
        break

      else:
        print(f'** {menu[key][response]} orders of {response} have been added to your meal **')
        break
  
  else:
    print('** Sorry this item is unavailable, please order item from our menu **')
    response = input(">").lower()
