class DataBase:
    def __init__(self,):
        self.data = {}


    def insert_customer(self, id, name):
        if 'customers' not in self.data:
            self.data['customers'] = {id: name}
        else:
            self.data['customers'].update({id: name})

    def display_customers(self):
        for id, name in self.data['customers'].items():
            print(id, name)

    def delete_customer(self, id):
        del self.data['customers'][id]



bd = DataBase()
bd.insert_customer(1, 'Mano Brown')
bd.insert_customer(2, 'Han Solo')
bd.insert_customer(3, 'Darth Vader')
bd.delete_customer(2)
bd.display_customers()

print(bd.data)