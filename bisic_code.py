#temperature converter
temp_input = float(input("please enter the temperature in celsius: "))
temp_converted = temp_input * 9/5 +32
print(f"The temperature in fahrenheit is: {temp_converted:.1f}")

#calculate average of 3 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
aver_num = (num1 + num2 + num3) / 3
print("The average of the 3 number is: {0:.2f}".format(aver_num))

#gender test
gen_input = int(input("Please enter your last ID number: "))
if gen_input % 2 == 0 :
    print("You are a lady.")
else:
    print("You are a man.")



#grade calculator
grade_input = int(input("Please enter your grade: "))
if grade_input >= 85:
  degree = "HD"
elif grade_input >= 65:
  degree = "D"
elif grade_input >= 50:
  degree = "P"
else:
  degree = "F"
print("Your score is {0}, grade degree is {1}.".format(grade_input,degree))


#number guessing game
random_num = 27
while True:
    try:
        num_input = int(input("Guess a random number between 0 and 100: "))
    except:
        print("Oops! Try again!")
        continue
    if num_input == random_num:
      break
    elif num_input > random_num:
      print(f"My number is less than {num_input}!")
    elif num_input < random_num:
      print("My number is great than {0}!".format(num_input))

print("Awesome! You are right!")


#even or odd
num_input = int(input("Please input an integer: "))
if num_input % 2 == 0:
  print(f"The number {num_input} is an even number!")
elif num_input % 2 == 1:
  print("The number {0} is an odd number!".format(num_input))


#multiplication table
for i in range(1,10):
  for j in range(1,10):
    print(f"{i * j:5}", end = "")
  print()


#sum of numbers
num_input = int(input("Please input an integer: "))
sum_num = 0
for i in range(1, num_input + 1):
    sum_num += i
print(f"The sum of numbers from 1 to {num_input} is: {sum_num}")



#password retry system
password = "123456"
n = 0
while n < 5:
  pass_input = input("Please enter 6-digit password: ")
  n = n + 1
  if password == pass_input:
    print("Password is right!")
    break
  else:
    if 5 - n > 0:
      print(f"Oops! Please try again! You still have {5 - n} chances!")
    else:
      print("Sorry! The password is wrong, you failed!")
      continue


#contact list
contacts = dict()
name = input("Please enter your first name: ")
number = input("Please enter your phone number: ")
contacts[name] = number
print(contacts)


#student grade tracker
student_grade = {}
name = input("Enter your full name: ")
mark = int(input("Enter your grade: "))
if mark > 85:
  grade = "HD"
elif mark > 65:
  grade = "D"
else:
  grade = "F"
student_grade[name] = {
    "mark": mark,
    "grade": grade
}
print(student_grade)



#shopping list
shopping_list = list()
while True:
  items = input("Enter what you're gonna buy: ")
  if items == "done":
    break
  shopping_list.append(items) 
print(shopping_list)