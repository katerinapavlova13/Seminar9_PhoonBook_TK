import Model

path = 'PhoneBook.txt'
contacts = []

last_id: str = '0'

def read_file():
    global contacts, last_id
    with open(path, 'r', encoding='utf_8') as f:
        contacts = [i.strip().split(';') for i in f.readlines()]
    last_id = '0' if len(contacts) == 0 else contacts[len(contacts) - 1][0]
    Model.refresh_table()



