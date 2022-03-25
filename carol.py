database={
    "zeddy":"2019",
    "carol":"2020",
    "palmer":"2323",
    "sylvia":"2212"

}
username=input("Enter your username: ")
for key, value in database.items():
    if username==key:
        password=input("Enter your password: ")
        if password==value:
            print ("Granted")
        else:
            print("Denied")
if username not in database:
    print("invalid username")