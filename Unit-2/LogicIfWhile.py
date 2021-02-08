# Ria T., Honors Geometry, 9/26/20
# Logic If While
# Exploring Boolean variables and logical operators


#tired = True
#caffeinated = True
#healthy = False

#ready_to_learn = caffeinated or (not tired)
#excited_to_learn = caffeinated and (not tired)
#go_home = tired and (not healthy)

#print("Are you ready to learn? ", ready_to_learn)
#print("Are you EXCITED to learn!!? ", excited_to_learn)
#print("Should you go home? ", go_home)



# Uses an if-statement to control execution of two print commands

#number_donuts = int(input("How many donuts do you want? "))
#less_than_half_dozen = number_donuts < 6

#print("Mmmmm...eating " + str(number_donuts) + " donut(s) sounds yummy!")
#if less_than_half_dozen:
#    print("You know you are not getting the best value.")
#    print("If you get a half-dozen or more, you get a discount.")
#print("You know what sounds even better? " + str(number_donuts*2) +
#    " donuts.")



# Uses if-else to run one group of statements or another

#number = int(input("Enter an integer: "));
#even_number = number%2==0;
#if even_number:
#    print(str(number) + " is even.");
#    print("Is " + str(number) + " also divisible by 4? " + str(number%4==0));
#else:
#    print(str(number) + " is odd.");
#    print("Is " + str(number) + " also divisible by 3? " + str(number%3==0));
#print("What a great number.");



# Uses if-elif to sort through coffee possibilities

cream = True;
sugar = False;
if ((not cream) and (not sugar)):
    preference = "black";
elif ((not cream) and sugar):
    preference = "sweet";
elif (cream and (not sugar)):
    preference = "white";
else:
    preference = "regular";
print("You like your coffee " + preference);
