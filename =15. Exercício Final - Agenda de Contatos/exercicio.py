""" 
    Agenda de Contatos
    - Desenvolva uma agenda de contatos persistindo as informações em arquivo. 
    O programa deve seguir as especificidades:
    1 - Criar o arquivo Agenda contendo tres metodos. 
     a. Um método para adicionar contato. 
     b. Um método para listar contatos.
     c. Criar um arquivo principal para a aplicação que importar o módulo de agenda e chamar cada um dos métodos desenvolvidos de acordo com a opção escolhida. 
"""

from agenda import add_contact, view_contacts, delete_contacts

def main():
    while True:
        print("\nAgenda de Contatos")
        print("1. Adiciona Contato")
        print("2. Listar Contatos")
        print("3. Remover Contatos")
        print("4. Sair")
        
        choice = input("Escolha a opção (1-4)\n")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contacts()
        elif choice == "4":
            break
        else:
            print("Informe uma opção válida")

main()