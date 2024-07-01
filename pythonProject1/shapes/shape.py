import json

class Shape:
    def show(self):
        info = vars(self)
        for m in info.keys():
            print(f"{m}: {info[m]}")
    def save(self):
        file = open(f'shapes/saves/{self.__class__.__name__}.json', 'w')
        json.dump(vars(self), file)
        file.close()

    def load(self):
        try:
            with open(f'shapes/saves/{self.__class__.__name__}.json', 'r') as file:
                atributes = json.load(file)
                for k in atributes.keys():
                    setattr(self, k, atributes[k])

        except FileNotFoundError:
            print('no save found')