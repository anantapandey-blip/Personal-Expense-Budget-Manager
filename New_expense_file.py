print("******** PERSONAL EXPENSE MANAGER ********")

monthly_budget= 89000
class expense:
    
    def __init__(self,amount,category,description):
      self.amount = amount
      self.category= category
      self.description= description
    def display(self):
        return f"Amount: {self.amount} \n Category: {self.category} \n Description: {self.description}"

facewash = expense(200, "Skincare", "Facewash")

groceries = expense(1400, "Food", "Essentials")

ration = expense(9800, "Ration", "Monthly groceries")

lunch = expense(346, "Food", "Lunch")

personal_care = expense(4500, "Essentials", "Personal care products")

monthly_essentials = expense(5680, "Essentials", "Household essentials")

clothes = expense(1400, "Monthly Shopping", "Clothes")

metro = expense(250, "Transport", "Metro fare")

python_course = expense(1200, "Education", "Python course")

movie = expense(800, "Entertainment", "Movie and snacks")

medicines = expense(600, "Healthcare", "Medicines")

shoes = expense(1500, "Shopping", "Shoes")

electricity_bill = expense(2000, "Bills", "Electricity bill")

shampoo = expense(500, "Personal Care", "Shampoo")

cab = expense(750, "Transport", "Cab fare")

breakfast = expense(300, "Food", "Breakfast")

books = expense(2500, "Education", "Books")

mobile_recharge = expense(900, "Bills", "Mobile recharge")

coffee = expense(400, "Entertainment", "Coffee with friends")

haircut = expense(650, "Personal Care", "Haircut")

investments= expense(36000, "Essentials", "Investments")

savings= expense(12000, "Essentials", "Savings")
expenses=[
        facewash,
        mobile_recharge,
        coffee,
        movie,
        medicines,
        metro,
        monthly_essentials,
        haircut,
        breakfast,
        cab,
        shampoo,
        shoes,
        python_course,
        books,
        electricity_bill,
        groceries,
        ration,
        lunch,
        personal_care,
        investments,
        savings
       ]


while True:

    menu=input("1. Add Expense\n 2. View All Expenses \n 3. Search Expenses \n 4. Show Total Spending \n 5. Show Category-wise Spending \n 6. Set Monthly Budget \n 7. Check Remaining Budget \n 8. Save Data in different file \n 9. Delete Expense \n 10. Clear History \n 11. Exit \n ")

    if menu=="1":
       amount_of_expense= input("Enter the amount of your expense:-  ")
       category_of_expense= input("Enter the category of your expense:-  ")
       description_of_expense= input("Enter the description of your expense:-  ")

       new_expense= expense(amount_of_expense,category_of_expense,description_of_expense)
       expenses.append(new_expense)
       print("New expense added")

    elif menu=="2":
        print("*************Your all expenses***************")
        for e in expenses:
           print(e.display())
           print(facewash.display())
           print("-"*30)
           print(groceries.display())
           print("-"*30)
           print(ration.display())
           print("-"*30)
           print(lunch.display())
           print("-"*30)
           print(personal_care.display())
           print("-"*30)
           print(monthly_essentials.display())
           print("-"*30)
           print(clothes.display())
           print("-"*30)
           print(haircut.display())
           print("-"*30) 
           print(coffee.display())
           print("-"*30)
           print(mobile_recharge.display())
           print("-"*30)
           print(movie.display())
           print("-"*30)
           print(python_course.display())
           print("-"*30)
           print(metro.display())
           print("-"*30)
           print(books.display())
           print("-"*30)
           print(medicines.display())
           print("-"*30)
           print(shampoo.display())
           print("-"*30)
           print(shoes.display())
           print("-"*30)
           print(cab.display())
           print("-"*30)
           print(breakfast.display())
           print("-"*30)
           print(electricity_bill.display())
    
   
    elif menu=="3":
       search= input("Enter the amount,category or discription of the expense you want to search:- ").strip().lower()
       found= False
       for e in expenses:
         if  (
           search == str(e.amount).lower() 
           or search ==(e.category).lower()
           or search== (e.description).lower()

           ):
           print(e.display())
           found = True
       if not found:
           print("Expense not found!")
    elif menu=="4":
       total_spending=0
       for items in expenses:
        total_spending += items.amount
       print(f"Your total spending of this month is ₹{total_spending}")

    elif menu=="5":
        category_total={}
        for e in expenses:
          if e.category in category_total:
             category_total[e.category]+= e.amount
          else:
             category_total[e.category] = e.amount

        for category, total in category_total.items():
           print(f"{category}: ₹{total}")

        
    elif menu=="6":
      change_budget=input("Enter the Updated budget- ")
      print(f"Your monthly budget is updated from ₹{monthly_budget} to ₹{change_budget} ")
    elif menu=="7":
     total_spending=0
     for items in expenses:
         total_spending = total_spending + items.amount
         Remaining_budget = monthly_budget - total_spending
     print(f"Your remaining budget is ₹{Remaining_budget}")
    elif menu=="8":
      with open("expenses.txt", "w") as f:
         f.write("\n*************Your all expenses***************\n")
         f.write(facewash.display())
         f.write("-"*30 + "\n")
         f.write(groceries.display())
         f.write("-"*30 + "\n")
         f.write(ration.display())
         f.write("-"*30 + "\n")
         f.write(lunch.display())
         f.write("-"*30 + "\n")
         f.write(personal_care.display())
         f.write("-"*30 + "\n")
         f.write(monthly_essentials.display())
         f.write("-"*30 + "\n")
         f.write(clothes.display())
         f.write("-"*30 + "\n")
         f.write(haircut.display())
         f.write("-"*30 + "\n")
         f.write(coffee.display())
         f.write("-"*30 + "\n")
         f.write(mobile_recharge.display())
         f.write("-"*30 + "\n")
         f.write(movie.display())
         f.write("-"*30 + "\n")
         f.write(python_course.display())
         f.write("-"*30 + "\n")
         f.write(metro.display())
         f.write("-"*30 + "\n")
         f.write(books.display())
         f.write("-"*30 + "\n")
         f.write(medicines.display())
         f.write("-"*30 + "\n")
         f.write(shampoo.display())
         f.write("-"*30 + "\n")
         f.write(shoes.display())
         f.write("-"*30 + "\n")
         f.write(cab.display())
         f.write(("-"*30 + "\n"))
         f.write(breakfast.display())
         f.write("-"*30 + "\n")
         f.write(electricity_bill.display())
         
         print("File saved successfully!")
             
        
    elif menu=="9":
         delete_expense = input("Enter the expense you want to delete-").strip().lower()
         found=False

         for e in expenses:
        
             if delete_expense == e.category.lower():
                expenses.remove(e)
                print("Expense deleted")
                found = True
                break
          
         if not found:
           print("Expense not found")

    elif menu=="10":
      with open("expenses.txt", "w") as f:
        print("history cleared")
    elif menu=="11":
      end=input("Do you really want to end this?(yes/no)")
      if end=="yes":
        print("Session closed")   