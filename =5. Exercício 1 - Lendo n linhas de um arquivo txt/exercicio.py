""" 
    Lendo números linhas de um arquivo
    
    - Escreva um programa para ler as primeiras numeros de linhas de um arquivo.
    
    1 - O nome do arquivo e a quantidade de linhas devem ser passadas via parâmetro na função. 
"""

def file_read_from_line(fname, nlines):
    from itertools import islice
    with open(fname, encoding="utf-8") as file:
        for line in islice(file, nlines):
            print(line)
            
file_read_from_line("texto.txt", 2)