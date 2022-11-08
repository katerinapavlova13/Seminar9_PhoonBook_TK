class Contact:
    id: str
    name: str
    surname: str
    phone: str
    comment: str

    def __init__(self, id: str, name: str, surname: str, phone: str, comment: str):
        self.id = id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.comment = comment

    def items(self):
        return (self.id, self.name, self.surname, self.phone, self.comment)

    def show(self):
        print(f'{self.id} {self.name} {self.surname} {self.phone} {self.comment}')