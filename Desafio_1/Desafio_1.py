# Nilo Rodrigues Alves Filho

TextoInicial = "\nOpções: \n1. Criar nova To-Do \n2. Exibir todas as To-Do \n3. Marcar To-Do como concluida \n4. Excluir To-Do \n5. Editar titulo da To-Do \n6. Sair \n"
ToDo = list()
# Formato da Lista
# [{'Titulo': %Titulo% , 'Status': %Status%}, {'Titulo': %Titulo% , 'Status': %Status%}]


# Função principal


def main():
    while (True):
        print(TextoInicial)
        Opcao = int(input("Digite a opção escolhida: "))
        if Opcao == 1:
            CriarToDo()
        elif Opcao == 2:
            ListarToDo()
        elif Opcao == 3:
            ConcluirToDo()
        elif Opcao == 4:
            ExcluirToDo()
        elif Opcao == 5:
            EditarToDo()
        elif Opcao == 6:
            break


# Funções Auxiliares


def CriarToDo():
    Novotitulo = input("\nDigite o título da nova To-Do: ")
    NovaToDo = {"Titulo": Novotitulo, "Status": False}
    ToDo.append(NovaToDo)
    print("To-Do cadastrada com sucesso!\n")


def ListarToDo():
    print("\nTo-Do:")
    for a in range(len(ToDo)):
        Marcador = ' '
        if ToDo[a]["Status"]:
            Marcador = 'X'
        print("{0}. [{1}]{2}".format(a + 1, Marcador, ToDo[a]["Titulo"]))


def ConcluirToDo():
    ListarToDo()
    Indice = int(input("\nDigite o índice da To-Do a ser concluída: ")) - 1
    ToDo[Indice]["Status"] = True
    print("\nTo-Do concluída com sucesso!")


def ExcluirToDo():
    ListarToDo()
    Indice = int(input("\nDigite o índice da To-Do a ser excluída: ")) - 1
    ToDo.remove(Indice)
    print("\nTo-Do excluída com sucesso!")


def EditarToDo():
    Indice = int(input("Digite o índice da To-Do a ser editada:")) - 1
    NovoTitulo = input("Digite o novo título: ")
    ToDo[Indice]['Titulo'] = NovoTitulo
    print("\nTítulo alterado com sucesso!")


main()
