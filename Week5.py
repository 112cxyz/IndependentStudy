#Hello all, this my 5th weekly indepenent study i am making a password authentication / login system
#This work is in the Apache Licence 2.0

import stdiomask
#stdiomask hides the password that the user enters so it wont be able to be seen by prying eyes.


print("Please Set A Password:")

password1 = stdiomask.getpass(">>> ")
print("Again Please:")
password2 = stdiomask.getpass(">>> ")


mixed_case = not password2.islower() and not password2.isupper()
#This stage the program is checking if its uppercase and lowercase to see if it contains either 
#if its just lowercase or just uppercase it will fail and will say that the check isnt complete 
if password1 == password2:
    print("check1")
    if mixed_case == True:
        print("check2")
        