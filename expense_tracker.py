#expenses tracker 
expenses = list()

#add expense
def add_expense(expenses):
  items = input("Enter the goods name: ")
  prices = float(input("Enter the goods price: "))
  expense = {"item": items, "price": prices}
  expenses.append(expense)

#show expense
def show_expense(expenses):
  for expense in expenses:
    print(expense["item"], "-", "$", expense["price"])

#total expense
def total_expense(expenses):
  total_cost = 0
  for expense in expenses:
    total_cost += expense["price"]
  print("The total cost is ${0:.2f}.".format(total_cost))

#choose what to show

while True:
  print("\n1. Add expense")
  print("2. Show expense")
  print("3. Total expense")
  print("4. Exit")

  choice = input("Which one would you like to choose?")

  if choice == "1":
    add_expense(expenses)
  
  elif choice == "2":
      show_expense(expenses)

  elif choice == "3":
      total_expense(expenses)

  elif choice == "4":
      break

  else:
      print("Invalid option")