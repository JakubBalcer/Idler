import pickle
import os


class Save:
    def __init__(self, file_url):
        self.money = 0
        self.wood = 0
        self.file_url = file_url

    def load_from_file(self):
        if not os.path.exists(self.file_url):
            self.save_to_file()
        else:
            with open(self.file_url, 'rb') as save_file:
                return pickle.load(save_file)

    def save_to_file(self):
        with open(self.file_url, 'wb') as save_file:
            pickle.dump(self, save_file)

    def set_file_name(self, filename):
        self.file_url = 'save/'+filename
