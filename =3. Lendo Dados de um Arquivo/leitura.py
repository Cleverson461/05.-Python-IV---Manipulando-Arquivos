""" 
    - Arquivos
    
    1 - Opção w - write
    2 - opção a - append
    3 - opção r - read
"""

with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f'Olá, {line.rstrip()}.')