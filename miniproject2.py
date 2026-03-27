name = ["sett", "Heimerdinger", "sion", "ornn", "vi"]
role = ["manager", "kitchen", "server", "bar", "washer"]
wage = [25.50, 20.50, 13.50, 18.50, 11.50]

while True:
    print("\n---Restaurant management---") #shows system options
    print("1.view staff")
    print("2.Add staff")
    print("3.remove staff")
    print("4.payroll")
    print("5.search staff")
    print("6.exit")

    opt = input ("\nselect your option: ")
    
    if opt == "1":
        print("\n---staff list---") #gives name of all staff and their roles and wages
        for i in range(len(name)):
            print(str(i+1) + ". " + name[i] + " - " + role[i] + " (£"+ str(wage[i]) + "/hr)")

    elif opt == "2":
        new_name = input("staff name: ") #adds a new staff to the system
        new_role = input("staff role: ")
        new_wage = float(input("hourly wage: "))

        name.append(new_name)
        role.append(new_role)
        wage.append(new_wage)
        print("added " + new_name + " to the system.")

    elif opt == "3":
        rem = input("Enter name to remove: ")#removes a staff member from the system
        if rem in name:
            idx = name.index(rem)
            name.pop(idx)
            role.pop(idx)
            wage.pop(idx)
            print("removed " + rem + " from the system. ")
        else:
            print("staff member not found.")

    elif opt == "4":
        total = sum(wage)
        print("The total cost per hour for all staff is: £" + str(total))#adds up all the sums of the workers and then displays to show total wage/hr

    elif opt == "5":
        search_name = input("enter the name of the staff: ")

        if search_name in name:
            idx = name.index(search_name)
            print("\n---staff member found---") #searches the name of the staff member and displays only their details
            print("name: " +name[idx])
            print("role: " + role[idx])
            print("hourly wage: £" + str(wage[idx]))
        else:
            print("error: '" + search_name + "' is not in the system.")

    elif opt == "6":
        print("exiting...")#it does what it says.. it exits
        break

    else:
        print("invalid option. choose from options 1, 2, 3, 4, 5, 6")