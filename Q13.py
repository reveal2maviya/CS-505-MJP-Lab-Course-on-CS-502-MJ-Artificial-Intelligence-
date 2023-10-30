"""
Program: Elevator Learning Agent
Description: This program simulates a simplified elevator learning agent that makes floor stops based on individuals' requests.
How to Run:
- On Ubuntu/Linux: Open the terminal and navigate to the directory containing this file. Use the command "python3 elevator_agent.py" to run the program.
- On Windows: Open a command prompt and navigate to the directory containing this file. Use the command "python elevator_agent.py" to run the program.
"""

class Elevator:
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.current_floor = 1
        self.stops = set()

    def request_stop(self, floor):
        self.stops.add(floor)

    def go_to_floor(self, floor):
        if floor < 1 or floor > self.num_floors:
            print(f"Invalid floor request: {floor}")
        else:
            self.current_floor = floor
            print(f"Elevator is now on floor {self.current_floor}")

    def process_stops(self):
        for stop in sorted(self.stops):
            self.go_to_floor(stop)
            print(f"Stopping at floor {stop}")
        self.stops.clear()

# Main function to simulate elevator operation
def main():
    num_floors = 10
    elevator = Elevator(num_floors)

    print("Elevator Learning Agent:")
    while True:
        request = input("Enter the floor number or 'q' to quit: ")
        if request == 'q':
            break
        try:
            floor = int(request)
            elevator.request_stop(floor)
        except ValueError:
            print("Invalid input. Please enter a valid floor number.")

    elevator.process_stops()

if __name__ == '__main__':
    main()
