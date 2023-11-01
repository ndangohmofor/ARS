def find_season(seasons, month):
    for season, months in seasons.items():
        if month in months:
            return season
