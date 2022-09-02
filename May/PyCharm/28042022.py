origin=input("Enter your country : ")
if "india" in origin.casefold():
    print("You are {}n National".format(origin.capitalize()))
else:
    print("You are not Indian National")
