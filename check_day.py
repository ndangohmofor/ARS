days = {
    "weekend": ["Saturday", "Sunday"],
    "weekday": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
}


def check_for_weekend(day):
    for week, days_list in days.items():
        if day in days_list:
            return week
