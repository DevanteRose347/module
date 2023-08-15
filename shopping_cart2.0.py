# <!-- 1) Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list -->
def store():
    shopping_cart = {}
    
    while True:
        item = input("please enter item or Enter quit to quit! and delete to delete! : ").strip()  
        
        if item.strip().lower() != 'quit' and item.strip().lower() !='delete':
            quantity = input("please enter amount of item or Enter quit to quit! and delete to delete! : ")
            shopping_cart[item] = quantity
        
        
        elif item.strip().lower() == 'delete' or quantity.strip().lower() == 'delete':
            delete = input("please enter item you want to delete! : ")
            del(shopping_cart[delete])
        
        else:
            for item, quantity in shopping_cart.items():
                print(f"{item} {quantity} is in shopping cart")
            break
       

        print(shopping_cart)  
   
store()
