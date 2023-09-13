class Manager:
    def __init__(self):

        self.actions = {}
        self.items = {}
        self.logs = []
        self.balance = 0.0
        self.amount = 0.0
        self.quantity = 0
        self.price = 0.0

    def menu(self, file_path):
        self.load(file_path)
        while True:
            for action in self.actions:
                print(f'- {action}')
            print("- end")
            user_input = input("Enter one of the commands: ").lower().strip()
            if user_input == "end":
                self.save(file_path)
                break
            self.action(user_input)

    def action(self, name, *args, **kwargs):

        if name not in self.actions:
            print('invalid command')
            return
        return self.actions[name](self,*args, **kwargs)

    def assign_old(self, name, action):
        self.actions[name] = action

    def assign(self, name):

        def inner(callback):
            self.actions[name] = callback
        return inner

    def save(self, file_path):
        with open(file_path, 'w') as file:
            file.write(f'{self.balance}\n{self.amount}\n')
            for name, qty in self.items.items():
                file.write(f'{name}\n{qty}\n')
            file.write('\n')
            for log in self.logs:
                log.save(file, self)
            file.write('end\n')

    def load(self, file_path):
        with open(file_path) as file:
            self.balance = float(file.readline())
            self.amount = float(file.readline())
            while True:
                name = file.readline().strip()
                if not name:
                    break
                qty = int(file.readline())
                self.items[name] = qty