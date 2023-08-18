class Register():

    def __init__(self, id, name, cpf, tel, city) -> None:
       self.name = name
       self.id = id
       self.tel = tel
       self.cpf = cpf
       self.city = city

    def __str__(self):
        return f"Register: id={self.id}, name={self.name}, cpf={self.cpf}, city={self.city}"

    def getId(self) -> int:
        return self.id
    
    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getCpf(self):
        return self.cpf

    def setCpf(self, cpf):
        self.cpf = cpf

    def getTel(self):
        return self.tel

    def setTel(self, tel):
        self.tel = tel

    def getCity(self):
        return self.city

    def setCity(self, city):
        self.city = city        

