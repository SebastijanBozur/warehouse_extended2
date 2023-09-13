from main import Manager
from actions import storage_actions


manager = Manager()
storage_actions(manager)
manager.menu('warehouse.txt')