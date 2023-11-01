from activities import activities
from activity_list import LinkedList


def insert_activities(activity_types):
    activities_list = LinkedList()
    for activity in activity_types:
        activities_list.insert_beginning(activity[0], activity[1], activity[3], activity[4], activity[5])
    return activities_list
