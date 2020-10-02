# this program helps to remind birthdays of your loved ones

dict = {}
while True:
    print("-----Birthday Reminder-----")
    print("1.Show birthday")
    print("2.Add to Birthday List")
    print("3.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        if len(dict.keys())==0:
            print("Nothing to show")
        else:
            name=input("Enter name to look for birthday:")
            birthday=dict.get(name,"No data found")
            print(birthday)
    elif choice == 2:
        name=input("Enter name of your loved one:")
        date=input("Enter birthdate:")
        dict[name]=date
        print("Birthday added")
    elif choice == 3:
        break
    else:
        print("Invalid option")
        