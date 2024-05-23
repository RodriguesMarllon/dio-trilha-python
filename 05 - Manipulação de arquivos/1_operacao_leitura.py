arquivo = open(r"C:\projetos\dio-trilha-python\05 - Manipulação de arquivos\lorem.txt", "r")


print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

# for linha in arquivo.readlines():
#     print(linha)
# while len(linha := arquivo.readline()):
#     print(linha)

arquivo.close()


