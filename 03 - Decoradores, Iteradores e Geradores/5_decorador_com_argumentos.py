def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar')
        funcao(*args, **kwargs)
        print('Faz algo depois de executar')

    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f'Olá Mundo {nome}!')

ola_mundo('João', 1000)