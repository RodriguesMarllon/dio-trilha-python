import re

def validate_numero_telefone(phone_number):
    # Define o padrão regex para o formato esperado
    pattern = r"^\(\d{2}\) 9\d{4}-\d{4}$"
    
    # Verifica se o número de telefone corresponde ao padrão
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

# Solicita ao usuário que insira o número de telefone
phone_number = input("Insira o número de telefone: ")
# Chama a função validate_numero_telefone com o número inserido e imprime o resultado
print(validate_numero_telefone(phone_number))
