# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, items = []):
        self.location = location
        self.items = items
    def __str__(self):
        return f"{self.location}"
    def _inventory_(self):
        if len(self.items) < 1:
            print('There are no items in your inventory.')
        else:
            print('---- Your Inventory ----')
            for item in self.items:
                print(f"Name: {item.name} \n")
                print(f"Name: {item.description} \n")
