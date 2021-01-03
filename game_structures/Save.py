import pickle
import os
from components.Counter import Counter


class Save:
    def __init__(self, file_url):
        self.money = 0
        self.wood = 0
        self.objects = {}
        self.file_url = file_url

    def set_file_name(self, filename):
        self.file_url = 'save/'+filename

    def each_second(self, resources):
        pass

    def get_object(self, name):
        return self.objects.get(name)

    def add_object(self, name, obj):
        self.objects[name] = obj

    def serialize(self):
        with open(self.file_url, 'wb') as save_file:
            pickle.dump(self.objects, save_file)

    def deserialize(self):
        if not os.path.exists(self.file_url):
            self.serialize()
        else:
            with open(self.file_url, 'rb') as save_file:
                self.objects = pickle.load(save_file)
