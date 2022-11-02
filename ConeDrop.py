import sys

def drop_cone(cone_numb):
    #Var for Cone Comparison
    x = 0

    #Print Blank Line
    print(" ")

    #While Loop to Print Cones
    while x < cone_numb:
       print('\u0394')
       x += 1


    #Var for Message to User About Cones Dropped   
    drop_msg = "You dropped " + str(cone_numb)

    if(cone_numb > 1):
       drop_msg += " cones"
    else:
       drop_msg += " cone"
    
    
    #Notify User How Many Cones Dropped
    print("\n" + drop_msg + "\n")



#Var for User Input
usr_choice = ""

#Var for Checking to Continue
b_cont = True

#While Loop to Keep the Cone Drop Party Going
while b_cont == True:   
   #Ask User for Cone Action
   usr_choice = input("Would you like to drop some cones? Y=Yes,N=No: ")
   
   #Check Answer for Yes and Number of Cones
   if(usr_choice.lower() == "y"):
      usr_cone_numb = input("\nHow many cones would you like to drop? ")
      
      #Quick Number Check on Cone Number Input
      if(usr_cone_numb.isdigit()):
          drop_cone(int(usr_cone_numb))
      else:
          print("You didn't enter a number")
 
      
   else:
      #User Doesn't Want to Continue. Stop Loop
      b_cont = False










