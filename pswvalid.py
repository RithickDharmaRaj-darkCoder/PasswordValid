#variables for password ckecking...
our_password = "pass123"
ur_password = " "
no_of_try = 0
max_no_try = 10
max_try_cmd = "Not reached the max try!!!"

#checks whether password matches or try reaches the maximum try...
while ur_password != our_password and max_try_cmd != "Reached the max try":
    if no_of_try < max_no_try:
        ur_password = input("Enter the password : ")     #getting password from user...
        no_of_try = no_of_try + 1               #increment the number of try...
    else:
        max_try_cmd = "Reached the max try"

#output to the user based on their input
if max_try_cmd == "Reached the max try":
    print("Account Blocked!, you have wrongly entered the password manytimes.")
else:
    print("Password matched! & Access geanted!")
