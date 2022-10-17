#creating a function that asks the user how much the food cost, and converting it to a float: adding a try expect statemt to check and make sure the user enters a a number as an input,  if there is a Value error,  it asks them to enter a valid number, and then we call the function again to ask them how much the food costs.
def get_food_cost():
    try:
        food_cost = float(input("How much does the food cost?"))
        return food_cost
    except ValueError:
        print("You did not enter a valid number")
        get_food_cost()
#creating a function that asks the user how many people are splitting the bill, and converting it to a float: adding a try expect statemt to check and make sure the user enters a a number as an input,  if there is a Value error,  it asks them to enter a valid number, and then we call the function again to ask them again.
def get_num_of_people():
    try:
        people = float(input("HOw many people are splitting the bill?"))
        return people
    except ValueError:
        print("You did not enter a valid number")  
        get_num_of_people() 
#creating a function that asks the user what is the tip percentl, and converting it to a float and dividing that number by 100 to get the decimal for later math: adding a try expect statemt to check and make sure the user enters a a number as an input,  if there is a Value error,  it asks them to enter a valid number, and then we call the function again to ask them again.
def get_tip_percent():
    try:
        tip = int(input("What is the tip percentage?")) / 100
        return tip
    except ValueError:
        print("You did not enter a valid number") 
        get_tip_percent() 
#creating a function to ask the user if they would like to run the function again
def run_again():
    run = input("Do you want to calculate another bill, yes or no? ")
    while run == "yes":
        get_total()
#creating a function that will take all the information and calculate the bill total and how it should be split
def get_total():
    #creating variables that will call the functions for each of the elements that we needed ffrom the user to do the calculations, the varibale will store the return number so that we can use it in later calculations
    food = get_food_cost() 
    people = get_num_of_people()
    tip = get_tip_percent() * food
    #making sure that the 10% sales tax is a decimal and multiplied by the cost of the food.
    tax = food * .10
    #creating two totals for different use cases, one variable to store a total bill that has tip and one that will total without a tip being added
    total_with_tip = round((food + tax + tip), 2)
    total_no_tip = round((food + tax), 2)
    # creeating condition statements for if there is only 1 person and a tip included in the bill, there will only be one print statement in the case of only oner person paying the bill
    if people == 1 and tip > 0:
        print(f'The total bill: ${total_with_tip:.2f}')
       
    #conditional for if there is multiple people and a tip included in the bill there will be two print statements in the case of a split , the total will be divided by the number of people.  
    elif people > 1 and tip > 0: 
        print(f'The total bill: ${total_with_tip:.2f}')
        print(f'Each person should pay ${total_with_tip/people:.2f}')
        
    #the next two statements are if there is no tip included in the bill and only one person paying:
    elif people == 1 and tip == 0:
        print(f'The total bill: {total_no_tip:.2f}')
        
    #this conditional is if there is more than oneperson splitting the bill and there is no tip included in the bill the total will be divided by the number of people
    elif people > 1 and tip == 0:
        print(f'The total bill: {total_no_tip:.2f}')
        print(f'Each person should pay ${total_no_tip/people:.2f}')  
         
get_total()
run_again()