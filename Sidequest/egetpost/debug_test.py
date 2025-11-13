global_validcreds = {'adam':'adam', 'bison':'unsung', 'admin':'admin'}
#print("Pass of Bison", global_validcreds["bison"])
user = "bison"
possi = global_validcreds[user]
#print("User Bison with pass : ", possi)


inpuser = input("Enter username : ")
inppass = input("Enter Password : ")


def upcheck():
    if inpuser in global_validcreds:
        if global_validcreds[inpuser] == inppass:
            print("Password Good ")
        else:
            print("Wrong Password ")
    else:
        print("Wrong Username")

upcheck()
