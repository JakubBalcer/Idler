import json


class Resource:
    def __init__(self, dict):
        self.name = dict['name']
        self.amount = dict['amount']
        self.value = dict['value']
        self.price = dict['price']
        self.description = dict['description']
        self.tab = dict['tab']

    @staticmethod
    def load_resources_from_file(filename):
        resources = []
        with open(filename) as file:
            data = json.load(file)
            for res in data['resources']:
                resources.append(Resource(res))
        return resources

    def __str__(self):
        return self.name

    def get_save_data(self):
        return {'value': self.value, 'amount': self.amount, 'price': self.price}

    def load_from_save(self, dict):
        if not dict is None:
            self.amount = dict['amount']
            self.price = dict['price']
            self.value = dict['value']
