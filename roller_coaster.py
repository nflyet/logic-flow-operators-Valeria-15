# Do not edit any of the starte code. Use the comments as a guide to complete the assignment.

print ("Welcome to the rollercoaster")

# Step 1:Ask the user about their height. 
height = int(input("What is your height in inches? "))

# Step 2: Ask for their age.
age = int(input("What is your age? "))


#Step 3: Create an if statement that matches for their responses. You may need multiple if/elif statements. 
    # Use the logic flow diagram to help you
if height >60:
    print("You can ride the rollercoaster.")
    if age<12:
        print("please pay $5.")
        bill = 5
    elif age <<18:
        print("please pay $7 .")
        bill = 7
    else:
        print("please pay $12 .")
        bill = 12
    photo=input("Do you want a photo? Yes o No :")
    if photo=="yes":
        print("photos are $3 extra. ")
        bill = bill+3
        bill=str(bill)
        print("Your final bill is $"+bill+".")
    else:
        bill=str(bill)
        print("Your final bill is $"+bill+".")
else:
    print("You cannot ride.")
# Step 4: Ask the user if they want a photo.

# Step 5: Tell them what their final bill is.

# Run your code to verify that it works. 