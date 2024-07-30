task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += " that should be completed as soon as possible."
    
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that should be done today."
        else:
            reminder += " that should be completed soon."

    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " that should be addressed today."
        else:
            reminder += " to consider completing when you have free time."

    case _:
        reminder = "Invalid priority entered. Please enter 'high', 'medium', or 'low'."

print("Reminder:", reminder)
