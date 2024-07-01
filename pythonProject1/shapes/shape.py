class Shape:
    def show(self):
        info = vars(self)
        for m in info.keys():
            print(f"{m}: {info[m]}")
    def save(self):
        file = open(f'shapes/saves/{self.__class__.__name__}.txt', 'w')
        file.write(str(vars(self)))
        file.close()

    def load(self):
        with open(f'shapes/saves/{self.__class__.__name__}.txt', 'r') as file:
            atributes = file.read()
            atributes = atributes.__dict__
            for k in atributes.keys():
                self.k = atributes[k]