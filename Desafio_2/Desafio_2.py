# Nilo Rodrigues Alves Filho

TextoInicial = "\nOpções: \n1. Criar nova To-Do \n2. Criar nova categoria \n3. Exibir todas as To-Do \n4. Marcar To-Do como concluida \n5. Excluir To-Do \n6. Excluir Categoria \n7. Editar titulo da To-Do \n8. Editar categoria \n9. Sair \n"
ToDo = {
    'Casa': [],
    'Trabalho': [],
    'Escola': []
}

# Formato da Lista
# ToDo = {
#          'Categoria1': [ {'Titulo': Titulo1, 'Status': Status1}, {'Titulo': Titulo2, 'Status': Status2} ],
#          'Categoria2': [ {'Titulo': Titulo1, 'Status': Status1}, {'Titulo': Titulo2, 'Status': Status2} ],
#          'Categoria3': [ {'Titulo': Titulo1, 'Status': Status1}, {'Titulo': Titulo2, 'Status': Status2} ]
#        }


# Função principal


def main():
    while (True):
        print(TextoInicial)
        Opcao = int(input("Digite a opção escolhida: "))
        if Opcao == 1:
            CriarToDo()
        elif Opcao == 2:
            CriarCategoria()
        elif Opcao == 3:
            ListarToDo()
        elif Opcao == 4:
            ConcluirToDo()
        elif Opcao == 5:
            ExcluirToDo()
        elif Opcao == 6:
            ExcluirCategoria()
        elif Opcao == 7:
            EditarToDo()
        elif Opcao == 8:
            EditarCategoria()
        elif Opcao == 9:
            break


# Funções Auxiliares


def CriarToDo():
    Categoria = input("\nDigite a categoria da nova To-Do: ")
    NovoTitulo = input("\nDigite o título da nova To-Do: ")
    NovaToDo = {"Titulo": NovoTitulo, "Status": False}
    ToDo[Categoria].append(NovaToDo)
    print("To-Do cadastrada com sucesso!\n")


def CriarCategoria():
    NovaCategoria = input("\nDigite a nova Categoria: ")
    ToDo.update({NovaCategoria: []})
    print("Categoria cadastrada com sucesso!\n")


def ListarToDo():
    Categorias = list(ToDo.keys())
    print("\nTo-Do's:")
    for a in range(len(Categorias)):
        print(" » " + Categorias[a])
        for b in range(len(ToDo[Categorias[a]])):
            Marcador = ' '
            if ToDo[Categorias[a]][b]["Status"]:
                Marcador = 'X'
            print("   {0}. [{1}]{2}".format(
                b + 1, Marcador, ToDo[Categorias[a]][b]["Titulo"]))


def ConcluirToDo():
    ListarToDo()
    Categoria = input("\nDigite a categoria da nova To-Do: ")
    Indice = int(input("\nDigite o índice da To-Do a ser concluída: ")) - 1
    ToDo[Categoria][Indice]["Status"] = True
    print("\nTo-Do concluída com sucesso!")


def ExcluirToDo():
    ListarToDo()
    Categoria = input("\nDigite a categoria da nova To-Do: ")
    Indice = int(input("\nDigite o índice da To-Do a ser excluída: ")) - 1
    ToDo[Categoria].remove(Indice)
    print("\nTo-Do excluída com sucesso!")


def ExcluirCategoria():
    Categorias = list(ToDo.keys())
    for a in range(len(Categorias)):
        print("[{0}] {1}".format(a + 1, Categorias[a]))
    Categoria = input("\nDigite a categoria a ser excluída: ")
    del ToDo[Categoria]
    print("\nCategoria excluída com sucesso!")


def EditarToDo():
    Categoria = input("\nDigite a categoria To-Do a ser editada: ")
    Indice = int(input("Digite o índice da To-Do a ser editada: ")) - 1
    NovoTitulo = input("Digite o novo título: ")
    ToDo[Categoria][Indice]['Titulo'] = NovoTitulo
    print("\nTítulo alterado com sucesso!")


def EditarCategoria():
    Categoria = input("Digite a categoria a ser editada: ")
    NovaCategoria = input("\nDigite a nova categoria: ")
    ToDo[NovaCategoria] = ToDo[Categoria]
    del ToDo[Categoria]
    print("\nCategoria editada com sucesso!")


main()
