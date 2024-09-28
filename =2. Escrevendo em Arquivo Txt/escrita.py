""" 
    - Arquivos
    
    1 - Opção w - write
    2 - opção a - append
    3 - opção r - read
"""
name = input("Digite o seu nome: ")

# Alternativa 1
# file = open("names.txt", "a")
# file.write(f'{name}\n')
# file.close()

# Alternativa 2
with open("names.txt", "a", encoding="utf-8") as file:
    file.write(f'{name}\n')