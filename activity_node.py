class Node:
    def __init__(self, activity, location, seasons, min_persons, max_persons, period, next_node=None):
        self.activity = activity
        self.location = location
        self.seasons = seasons
        self.min_persons = min_persons
        self.max_persons = max_persons
        self.period = period
        self.next_node = next_node

    def set_next_node(self, new_node):
        self.next_node = new_node

    def get_next_node(self):
        return self.next_node

    def get_activity(self):
        return self.activity

    def get_lcation(self):
        return self.location

    def get_seasons(self):
        return self.seasons

    def get_min_persons(self):
        return self.min_persons

    def get_max_persons(self):
        return self.max_persons

    def get_period(self):
        return self.period
