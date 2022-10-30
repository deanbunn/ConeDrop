import sys

def drop_cone(cone_numb):
    x = 0
    while x < cone_numb:
       print('\u0394')
       x += 1

       
    drop_msg = "You dropped " + str(cone_numb)

    if(cone_numb > 1):
       drop_msg += " cones"
    else:
       drop_msg += " cone"
    
    
    print("\n" + drop_msg + "\n")



#Var for User Input
usr_choice = ""

#Var for Checking to Continue
b_cont = True

while b_cont == True:   
   usr_choice = input("Would you like to drop some cones? Y=Yes,N=No: ")
   
   if(usr_choice.lower() == "y"):
      usr_cone_numb = input("\nHow many cones would you like to drop? ")
      
      if(usr_cone_numb.isdigit()):
          drop_cone(int(usr_cone_numb))
      else:
          print("You didn't enter a number")
 
      
   else:
      b_cont = False










