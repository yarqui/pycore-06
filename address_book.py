from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        value = str(value)

        if len(value) != 10:
            raise ValueError("Phone number should be 10 digits")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def delete_phone(self, number):
        number = str(number)
        existing_number = self.find_phone(number)

        if existing_number == None:
            raise ValueError("Phone number was not found")

        self.phones = [p for p in self.phones if p.value != number]

    def update_phone(self, old_number, new_number):
        old_number = str(old_number)

        for i, phone in enumerate(self.phones):
            if phone.value == old_number:
                self.phones[i] = Phone(new_number)
                return

        raise ValueError("Old number was not found")

    def find_phone(self, number):
        number = str(number)
        for phone in self.phones:
            if phone.value == number:
                return phone

        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # def __init__(self):
    #     self.data = []

    def add_record(self, rec):
        self.data[rec.name.value] = rec

    def find_record(self, name):
        return self.data.get(name, "No record was found with such name")
        # for rec in self.data:
        #     if rec.name == name:
        #         return rec

        # raise ValueError("No record with such name")

    def delete_record(self, name):
        # self.data = [rec for rec in self.data if rec.name != name]
        if name in self.data:
            del self.data[name]
