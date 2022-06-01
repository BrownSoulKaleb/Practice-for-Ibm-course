#Second assignment Part 1
print ("Jerry Momus Cst 1101")
print("Second assignment part 1")
print("What is your first name?")
firstname =input()
print("What is your last name?")
lastname = input()
print("What is your age?")
age = int(input())
print ("Alright, so your name is " + firstname + " " + lastname + ", and your age is " + str(age) + ". ") #Had to convert integer of age = input to a string, because python cannbot concatenate this


#Second Assignment Part 2
print("Second Assignment")
print("Give your first number.")
num1 = int(input())
print("Give your second number.")
num2 = int(input())
sum = num1 + num2
prod = num1 * num2
div = num2 / num1
div2 = num1 / num2
avg = (num1 + num2) / 2
print("Addition of the two numbers is " + str(sum) + ".")
print("The product of these two numbers is " + str(prod) + ". Now the first number divided by the second number is " + str(div2) + ". The second number divided by the first number is " + str(div) + ".")
print("The average of these two numbers is " + str(avg) + ".")        


print("Final part of assignment")

print("How much do you make per hour?")
pph = float(input())
print("How much hours did you work this week?")
htw = float(input())
print("So your name is " + firstname + " " + lastname + ", you make " + str(pph) + " per hour, and made " + str(pph *htw) + " this week before taxes.")
