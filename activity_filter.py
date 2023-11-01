def find_matches(activities, month=None, day=None, participants=1, indoors=False):
    current_matches = [activity for activity in activities if not indoors]