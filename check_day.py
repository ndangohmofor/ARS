days = {
    "weekend": ["saturday", "sunday"],
    "weekday": ["monday", "tuesday", "wednesday", "thursday", "friday"]
}


def check_for_weekend(day):
    for week, days_list in days.items():
        if day in days_list:
            return week
