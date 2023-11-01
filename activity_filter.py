from check_day import check_for_weekend
from find_season import find_season
from insert_activities import insert_activities
from seasons import seasons


def find_matches(activities, month=None, day=None, participants=1, location="Outdoor"):
    activities_linkedlist = insert_activities(activities)
    current_matches = [activity for activity in activities_linkedlist if activity.get_location == location and (
            activity.get_min_persons <= participants <= activity.get_max_persons
    )]

    if month:
        current_season = find_season(seasons, month)
        current_matches = [activity for activity in current_matches if current_season in activity.get_seasons]

    if day:
        current_matches = [activity for activity in current_matches if activity.get_period == check_for_weekend(day)]

    return current_matches
