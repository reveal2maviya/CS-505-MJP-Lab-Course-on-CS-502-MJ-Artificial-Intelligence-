"""
Program: Object Arrangement in a Room (A* Approach)
Description: This program simplifies the problem of arranging objects in a room using an A* search algorithm.
How to Run:
- On Ubuntu/Linux: Open the terminal and navigate to the directory containing this file. Use the command "python3 object_arrangement.py" to run the program.
- On Windows: Open a command prompt and navigate to the directory containing this file. Use the command "python object_arrangement.py" to run the program.
"""

# Object class representing rectangular and square-shaped objects
class Object:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Object({self.width}x{self.height})"

# Room class representing the room to arrange objects
class Room:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]

    def is_valid_location(self, x, y, obj):
        if x + obj.width > self.width or y + obj.height > self.height:
            return False
        for i in range(x, x + obj.width):
            for j in range(y, y + obj.height):
                if self.grid[j][i] != ' ':
                    return False
        return True

    def place_object(self, x, y, obj):
        for i in range(x, x + obj.width):
            for j in range(y, y + obj.height):
                self.grid[j][i] = '*'

    def __str__(self):
        room_str = ''
        for row in self.grid:
            room_str += ''.join(row) + '\n'
        return room_str

# A* search algorithm to arrange objects in the room
def arrange_objects(room, objects):
    objects.sort(key=lambda obj: obj.width * obj.height, reverse=True)
    for obj in objects:
        for y in range(room.height):
            for x in range(room.width):
                if room.is_valid_location(x, y, obj):
                    room.place_object(x, y, obj)
                    print(f"Placed {obj} at ({x}, {y})")
                    return True
    return False

# Main function to perform object arrangement
def main():
    room_width = 10
    room_height = 10
    room = Room(room_width, room_height)

    objects = [
        Object(3, 2),
        Object(2, 2),
        Object(2, 1),
        Object(1, 1),
        Object(1, 1),
        Object(1, 1),
        Object(1, 1),
    ]

    print("Object Arrangement in a Room:")
    if arrange_objects(room, objects):
        print("\nArrangement in Room:")
        print(room)
    else:
        print("No suitable arrangement found.")

if __name__ == '__main__':
    main()
