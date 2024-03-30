from collections import UserDict
from errors import RecordFindError

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


    def delete(self, name):
        if not name in self.data:
            raise RecordFindError(f"User {name} can not be found.")        
        self.data.pop(name)


    def find(self, name):
        user = self.data.get(name)
        if user:
            return user
        else:
            raise RecordFindError(f"User {name} has not been found.") 
