from activity_filter import find_matches
from activities import activities
from seasons import months, days, locations
from welcome import welcome


finish_activity_search = False

welcome()

while not finish_activity_search:
    user_month = None
    while not user_month or user_month not in months:
        user_month = str(input(
            "\nWhich month of the year are you looking for engage in an activity? (Type the full month. Example, "
            "March/ April/ May/ etc.\n"
        )).lower()

    user_day = None
    while not user_day or user_day not in days:
        user_day = str(input(
            "\nWhat day of the week are you looking to engage in an activity (Type the full day. Example, "
            "Monday / Tuesday / etc)?\n"
    )).lower()

    activity_location = None
    while not activity_location or activity_location not in locations:
        activity_location = str(input(
            "\nWould you like an 'indoor' or 'outdoor' activity? (Type the word 'Outdoor', or 'Indoor', or 'Both').\n"
    )).lower()

    num_of_participants = input(
        "\nHow may people are going to be involved in the activity? (Type a digit and press enter Example 1/ 2/ 3/ 4/ "
        "etc).  If it's only you, you can just press enter\n"
    )

    if num_of_participants:
        num_of_participants = int(num_of_participants)
    else:
        num_of_participants = None

    activity_match_list = find_matches(activities, user_month, user_day, num_of_participants, activity_location)

    if activity_match_list.head_node.activity is not None:
        print(activity_match_list.stringify_list())

        cont_search = str(input(
            "\nDo you want to change the search criteria? Enter 'y' for yes or 'n' for no\n"
        )).lower()

        if cont_search == 'n':
            finish_activity_search = True

    else:
        cont_search = str(input(
            "\nNo activities matched your selected criteria. Do you want to try another search?\n"
        )).lower()
        if cont_search == 'n':
            finish_activity_search = True
