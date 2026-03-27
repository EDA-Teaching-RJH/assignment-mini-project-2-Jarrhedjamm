name = ["sett", "Heimerdinger", "sion", "ornn"]
role = ["manager", "kitchen", "server", "bar", "washer"]
wage = ["25.50", "20.50", "13.50", "18.50", "11.50"]

while true:
    print("\n---Restaurant management---")
    print("1.view staff")
    print("2.Add staff")
    print("3.remove staff")
    print("4.payroll")
    print("5.exit")

    opt = input ("\nselect your option: ")
    
    if opt == "1":
        print("\n---staff list---")
        for i in range(len(names)):
            print(str(i+1) + ". " + name[i] + " - " + role[i] + " (£"+ str(wage[i]) + "/hr)")

    