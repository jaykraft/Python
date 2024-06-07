class Game:
    def __init__(self):
        self.locations = {
            'forest': 'You are in a dark forest. Paths lead north and east.',
            'cave': 'You are in a damp cave. Paths lead south and west.',
            'lake': 'You are at the edge of a serene lake. Paths lead west and north.',
            'village': 'You are in a small village. Paths lead east and west.'
        }
        self.current_location = 'forest'
        self.inventory = []

    def show_location(self):
        print(self.locations[self.current_location])

    def move(self, direction):
        if self.current_location == 'forest':
            if direction == 'north':
                self.current_location = 'lake'
            elif direction == 'east':
                self.current_location = 'village'
            else:
                print("You can't go that way.")
        elif self.current_location == 'cave':
            if direction == 'south':
                self.current_location = 'village'
            elif direction == 'west':
                self.current_location = 'forest'
            else:
                print("You can't go that way.")
        elif self.current_location == 'lake':
            if direction == 'west':
                self.current_location = 'forest'
            elif direction == 'north':
                self.current_location = 'cave'
            else:
                print("You can't go that way.")
        elif self.current_location == 'village':
            if direction == 'east':
                self.current_location = 'lake'
            elif direction == 'south':
                self.current_location = 'forest'
            else:
                print("You can't go that way.")
        else:
            print("Invalid location.")

    def start(self):
        print("Welcome to the Adventure Game!")
        while True:
            self.show_location()
            command = input("What do you want to do? ").strip().lower()
            if command in ['north', 'south', 'east', 'west']:
                self.move(command)
            elif command == 'quit':
                print("Thanks for playing!")
                break
            else:
                print("Invalid command.")

if __name__ == "__main__":
    game = Game()
    game.start()
                