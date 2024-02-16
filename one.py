from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field): 
    pass

class Phone(Field):
    MAX_LEN = 10

    def __init__(self, phone):
        super().__init__(phone)

    def __str__(self):
        if len(self.value) == 10:
            return self.value
        else:
            return f'{self.value} is in a wrong format'

class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phones = [Phone(phone)]

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return f'{phone} is not found'

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return
        raise ValueError("Phone number not found.")

    def __str__(self):
        phones = '; '.join(str(p) for p in self.phones)
        return f"Contact name: {self.name}, phones: {phones}"

class AddressBook(UserDict):
    def add_record(self, name, record):
        self.data[name] = record

    def find_record(self, name):
        if name in self.data:
            return self.data[name]
        return f'{name} is not found'

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
            return f'{name} is removed from Addressbook'
        return f'{name} not found in Addressbook'

if __name__ == "__main__":
    # Example usage:
    address_book = AddressBook()
    record1 = Record("John", "1234567890")
    record2 = Record("Alice", "0987654321")
    address_book.add_record("John", record1)
    address_book.add_record("Alice", record2)
    print(address_book.find_record("John"))
    print(address_book.delete_record("Alice"))