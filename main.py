from collections import UserDict
from classes import Record 


class AddressBook(UserDict):
    def add_record(self, record: Record):
        '''
        Метод додавання запису до книги
        '''
        # ключ - значення імені запису; значення - сам запис як об'єкт Record
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        '''
        Пошук запису за ім'ям
        '''
        name = name.lower().capitalize()
        if name in self.data.keys():
            return self.data.get(name)
        return f"There is no contact {name} in our AddressBook!"

    def delete(self, name: str):
        '''
        Видалення запису за ім'ям (з поверненням видаленого запису)
        '''
        name = name.lower().capitalize()
        if name in self.data.keys():
            return self.data.pop(name)
        return f"There is no contact {name} in our AddressBook!"


def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_phone("6666666666")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)
    print("-----------------------------------")

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
    print("-----------------------------------")

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
    print("-----------------------------------")

    # Видалення запису Jane
    book.delete("Jane")
    john_record.remove_phone("6666666666")

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)
    print("-----------------------------------")

    john_record.add_phone("+389876543210")  # Виконається
    john_record.add_phone("389876543210")   # Видасть повідомлення про вже наявність номеру
    john_record.add_phone("89876543210")    # Видасть повідомлення про вже наявність номеру
    
    for record in book.data.values():
        print(record)


if __name__ == "__main__":
    main()