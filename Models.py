class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone


    def exibir(self):
        print(f"Nome: {self.nome}| Email: {self.email}| Telefone: {self.telefone}")

    def converte_tupla(self):
        return (self.nome, self.email, self.telefone)

    @staticmethod
    def reverte_tupla(tupla):
        c=Cliente(tupla[1], tupla[2], tupla[3])
        c.id = tupla[0]
        return c


c1= Cliente("Ray", "rayaryel@gamil.com", "123456789")
c1.exibir()

c2 = Cliente.reverte_tupla((5, "Ana Souza", "ana@email.com", "47999990000"))
c2.exibir()