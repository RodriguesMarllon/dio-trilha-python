class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# p = Pessoa("Guilherme", 28)
# print(p.nome, p.idade)

p = Pessoa.criar_de_nascimento(1994, 3, 21, "Guilherme")
print(p.idade, p.nome)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))