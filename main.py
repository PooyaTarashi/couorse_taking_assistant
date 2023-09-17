from typing import Any
import pyperclip as ppc
import pickle

class Item:
    def __init__(self, caption, id) -> None:
        self._caption = None
        self._id = None
        self.caption = caption
        self.id = id
    
    def save_to_pickle(self):
        with open('data.pickle', 'rb') as file:
            loaded_data = pickle.load(file)
            loaded_data[self.id] = self
            new_data = loaded_data
            file.close()
        with open('data.pickle', 'wb') as file:
            pickle.dump(new_data, file)


    def delete_from_pickle(self):
        with open('data.pickle', 'rb') as file:
            loaded_data = pickle.load(file)
            del loaded_data[self.id]   
            new_data = loaded_data
            file.close()
        with open('data.pickle', 'wb') as file:
            pickle.dump(new_data, file)     


    @property
    def caption(self):
        return self._caption
    @caption.setter
    def caption(self, caption):
        self._caption = caption

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id


class System:
    def __init__(self) -> None:
        pass

    def load_data(self) -> dict:
        with open('data.pickle', 'rb') as file:
            loaded_data = pickle.load(file)    # Returns a dictionary. Keys are IDs and Values are course obj.
            return loaded_data
        
    def add_item(self, caption, id):
        itm = Item(caption, id)
        itm.save_to_pickle()

if __name__ == '__main__':
    s = System()

    
# rizmo = Item('Rizmo Taheri', '123')
# rizmo.save_to_pickle()
# rizmo.delete_from_pickle()

# mizro = Item('Mizro Bagheri', '321')
# mizro.save_to_pickle()
# mizro.delete_from_pickle()

