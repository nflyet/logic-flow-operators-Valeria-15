#Do not edit any of the starte code. Use the comments as a guide to complete the assignment.

print ("Welcome to the rollercoaster")

#Step 1:Ask the user about their height. 
height = int(input("What is your height in inches? "))

#Step 2: Create an if statement that matches for their response. You may need multiple if/elif statements. 
if height >= 60:
  age = int(input("What is your age? "))
  if age <=12:
    bill = 5
    print ("Your ticket is $5.")
  elif age <=18: 
    bill = 7
    print ("Your ticket is $7.")
  elif age >= 45 and age <= 85:
    bill = 0
    print ("Your ticket is free.")
  else: 
    bill = 12
    print ("Your bill is $12.")

  #Step 3: Ask the user if they want a photo.
  photo = input("Do you want a photo? ")
  if photo =="Y" or photo == "y":
    bill = bill + 3
    print(f"Your total bill is ${bill}")
  else:
    print(f"Your total bill is ${bill}")

else:
  print("You are not tall enough to ride the coaster.")

#Run your code to verify that it works. 