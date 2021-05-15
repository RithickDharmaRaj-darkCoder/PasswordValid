#variables for password ckecking...
orgin_psw = input("Create a new password (Admin!): ")
max_no_try = int(input("Maximum no.of try to enter the password correctly : "))
print("\n",f"               WARNING!, You have only {max_no_try} chance to enter the password correctly!")
ur_password = " "
no_of_try = 0
max_try_cmd = "Not reached the max try!!!"

#checks whether password matches or try reaches the maximum try...
while ur_password != orgin_psw and max_try_cmd != "Reached the max try":
    if no_of_try < max_no_try:
        ur_password = input(f"Enter the password for {no_of_try}th try : ")     #getting password from user...
        no_of_try = no_of_try + 1                        #increment the number of try...
    else:
        max_try_cmd = "Reached the max try"

#output to the user based on their input
if max_try_cmd == "Reached the max try":
    print("Account Blocked!, you have wrongly entered the password manytimes.")
else:
    print("Password matched! & Access granted!")
