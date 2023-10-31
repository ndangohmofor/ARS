from activity_node import Node

class LinkedList:
    def __init__(self, activity=None, location=None, seasons=None, min_persons=None, max_persons=None, period=None):
        self.head_node = Node(activity, location, seasons, min_persons, max_persons, period)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_activity, new_location, new_seasons, new_min_persons, new_max_persons, new_period):
        new_node = Node(new_activity, new_location, new_seasons, new_min_persons, new_max_persons, new_period)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node