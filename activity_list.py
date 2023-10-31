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

    def remove_node(self, activity):
        current_node = self.head_node
        if self.head_node.get_activity() == activity:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_activity() == activity:
                    current_node.next_node = next_node.get_next_node()
                    current_node = None
                else:
                    current_node = next_node

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            string_list += str(current_node.activity + ": " + current_node.location + "Number of person: " + current_node.min_persons + " - " + current_node.max_persons + "Seasons:\n\t" + [season + "\n" for season in current_node.seasons])
            current_node = current_node.get_next_node()
        return string_list
