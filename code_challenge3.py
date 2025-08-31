#code challenge 3: Fare discount Calculator
#DES: ask user to input his/her name, after doing so, ask user as well his/her fare fee and if she/he is currently a studet. If user is a student apply 20% discount on fare. Promptly display the discounted price and calculated discount. If user is not  student, promptly display a message indicating that she/he is not eligible for a discount.



name = input("Input your name: ")
passenger = input("Are you a student (Yes or No): ")
fare = eval(input("Fare: "))

if passenger == 'Yes':
	discount = fare * .2
	newfare = fare - discount
	print("Congrats,",name,"discount has been approved! \nYour discount is", discount,"\nYour discounted fare is ",newfare,  "\nEnjoy your ride with us ^_^ ")

else:
	print("Sorry,",name,"your request to have a discount is not approved :( ")