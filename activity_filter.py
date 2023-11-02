from activity_list import LinkedList
from check_day import check_for_weekend
from find_season import find_season
from insert_activities import insert_activities
from seasons import seasons


def find_matches(activities, month=None, day=None, participants=1, location="Outdoor"):
    activities_linkedlist = insert_activities(activities)

    # print(activities_linkedlist.stringify_list())
    matched_activity_nodes = LinkedList()

    current_node = activities_linkedlist.head_node

    season = find_season(seasons, month)
    week = check_for_weekend(day)

    while current_node.next_node:

        if (season in current_node.seasons) and (week == current_node.period) and (
                current_node.min_persons <= participants <= current_node.max_persons) and (
                current_node.location.lower() == location.lower() or current_node.location.lower() == 'both'):
            matched_activity_nodes.insert_beginning(current_node.activity, current_node.location, current_node.seasons,
                                                    current_node.min_persons, current_node.max_persons,
                                                    current_node.period)
        current_node = current_node.get_next_node()
    return matched_activity_nodes
