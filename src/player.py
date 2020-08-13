# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, room):
        self.room: Room = room
    # def __str__(self):
    #     return self.room