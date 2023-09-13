

def storage_actions(manager):

    @manager.assign('balance')
    def balance(manager):
        mode = int(input("Would you like to deposit(1), withdraw(2) or look at balance(3)"))
        if mode != 3:
            manager.amount = float(input('Please enter the amount you would like to deposit or withdraw'))
        if manager.amount < 0:
            print('Invalid amount')
            return
        if mode == 2:
            if manager.amount > manager.balance:
                print("Not enough funds.")
                return
            manager.balance -= manager.amount
        if mode == 1:
            manager.balance += manager.amount
        if mode == 3:
            print(f'Your current balance is {manager.balance}')
            return
        manager.logs.append(manager)


    @manager.assign('purchase')
    def purchase(manager):
        manager.item = input("Enter item name: ")
        manager.price = float(input("Enter item price: "))
        manager.quantity = int(input("Enter item quantity: "))
        if manager.balance < manager.price * manager.quantity:
            print("not enough funds")
            return
        manager.balance -= manager.price * manager.quantity
        if manager.item not in manager.items:
            manager.items[manager.item] = 0
        manager.items[manager.item] += manager.quantity
        manager.logs.append(manager)


    @manager.assign('sale')
    def sale(manager):
        manager.item = input("Enter item name: ")
        if manager.item not in manager.items:
            print(f"Item({manager.item}) not in warehouse")
            return
        manager.quantity = int(input("Enter item amount: "))
        if manager.items[manager.item] < manager.quantity:
            print("Insufficient quantity")
            return
        manager.price = float(input("Enter item price: "))
        manager.balance += manager.price * manager.quantity
        manager.items[manager.item] -= manager.quantity
        manager.logs.append(manager)


    @manager.assign('list')
    def list_items(manager):
        print('Total Warehouse inventory: ')
        for name, value in manager.items.items():
            print(name, value)


    @manager.assign('review')
    def review(manager):
        index_from = int(input("Please enter starting point of log: "))
        index_to = int(input("Please enter ending point of log: "))
        for log in manager.logs[index_from:index_to]:
            log.print()


    @manager.assign('search')
    def search(manager):
        name = input("Enter item name in warehouse: ")
        if name in manager.items:
            quantity = manager.items[name]
            print(f"Quantity: {quantity}")
        else:
            print("Item not in warehouse")

