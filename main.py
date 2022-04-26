'''
Python Skills Directions:

1. Write a conditional that is based on user input. (at least two questions)
2. Write a function that is called within a loop (could be for loop or while loop). 
3. Create a list and print something from the list with user input.
4. Use try and except to test user input
5. Make a table with tabulate library
6. Format money 
'''

'''
def survey():
    print('1) M&Ms')
    print('2) Skittles')
    print('3) Nerds')
    print('4) Twix')
  
    while True:
        try:
            question = int(input('Out of these options (1,2,3,4), which one is your favorite candy? '))
            break
        except: 
            print("That's not valid option!")
          
    if question == 1:
        print('I like that candy!')
    elif question == 2:
        print('Taste the Rainbow!')
    elif question == 3:
        print('You are a nerd!')
    elif question == 4:
        print('Thats a good choice!')
    else:
        print('That option is not on the list!')
survey()
''' 
from tabulate import tabulate 
print (tabulate([["1. Chocalate", " $5.99", "4. Oatmeal raisin cookies", " $2.99", "7. Milk", " $1.75"], ["2. Vanilla", " $5.99", "5. Chocalate Chip cookies", " $2.99", "8. Chocalate Milk", " $2.25"], ["3. Pistachio", " $4.99", "6. Sugar Cookies", " $2.99", "9. Black Tea", " $2.99"]], ["IceCream", " $", " Cookies", " $", "Drinks", " $" ], "fancy_grid"))

total = 0
order = []
#waiter is taking the costumers order
#waiter asks what type of icecream they want
icecream = input("Pick a type of icecream: Chocalate, Vanilla, or Pistachio? " )

print(icecream)
if icecream.lower()== "chocalate":
    order.append("chocalate")
    total = 5.99
elif icecream.lower()== "vanilla":
    order.append("vanilla")
    total = 5.99
elif icecream.lower()== "pistachio":
    order.append("pistachio")
    total = 4.99
print("Thats is a good choice! The total will be $", total, ".")

#waiter asks what type of cookies they want

cookie = input("Pick a type of cookies: oatmeal, chocalate, or sugar cookies? ")

print(cookie)
if cookie.lower()== "oatmeal rasin cookies":
    order.append("oatmeal rasin cookies")
    total = 2.99
elif cookie.lower()== "chocalate chip cookies":
    order.append("chocalate chip cookies")
    total = 2.99
elif cookie.lower()== "sugar cookies":
    order.append("sugar cookies")
    total = 2.99
print("The total will be $", total, ".")