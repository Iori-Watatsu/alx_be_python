task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): ")).lower()
time_bound = str(input("Is it time-bound? (yes/no): ")).lower()

match priority :
    case "high":
        priority == "high"
        print(f"{task} is a high priority task that requires immediate attention today!")
    #case "medium":
        #if priority == "medium":
            #print(f"{task} is a medium priority task that requires attention soon.")
    case "medium" | "low":
        priority == "medium" or "low"
        if time_bound == "no":
            print(f"{task} is a low priority task. Consider completing it when you have free time.")
        else:
            print(priority)
