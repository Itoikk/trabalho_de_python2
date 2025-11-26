import os
def menu_inicio():
    print("================================")
    print("    Gerenciador de Projetos     ")
    print("================================")
    print("                                ")
    print("Opções:")
    print("1 - Usuários")
    print("2 - Projetos")
    print("3 - Tarefas")
def menu_usuarios():
    os.system("cls")
    print("Você escolheu Usuários!")
    print("Opções:")
    print("0 - Voltar")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar usuário")
    print("4 - Atualizar")
    print("5 - Remover")
def mostrar_usuarios(indices, usuarios):
    if indices == []:
        return
    for indice in indices:
        print()
        print("="*20)
        print(f"nome: {usuarios[indice]["nome"]}\nemail: {usuarios[indice]["email"]}\nperfil: {usuarios[indice]["perfil"]}")
        print("="*20)
def listar_usuarios(usuarios):
    for usuario in usuarios:
        print("="*20)
        print(f"nome: {usuario["nome"]}")
        print(f"email: {usuario["email"]}")
        print(f"perfil: {usuario["perfil"]}")
        print("="*20)


def menu_projetos():
    os.system("cls")
    print("Você escolheu Projetos!")
    print("Opções:")
    print("0 - Voltar")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar projeto")
    print("4 - Atualizar")
    print("5 - Remover")

def mostrar_projetos(indices, projetos):
    if indices == []:
        return
    for indice in indices:
        print()
        print("="*20)
        print(f"nome: {projetos[indice]["nome"]}\ninicio {projetos[indice]["inicio"]}\nfim: {projetos[indice]["fim"]}\ndescricao: {projetos[indice]["descricao"]}")
        print("="*20)

def menu_tarefas():
    os.system("cls")
    print("Você escolheu Tarefas!")
    print("Opções:")
    print("0 - Voltar")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Remover")

def menu_listar_tarefas():
    os.system("cls")
    print("Como você quer listar?")
    print("Opções:")
    print("0 - Voltar")
    print("1 - Todas")
    print("2 - Por Projetos")
    print("3 - Por Responsável")
    print("4 - Por Status")


def menu_atualizar_tarefa():
    os.system("cls")
    print("O que você quer atualizar?")
    print("Opções:")
    print("0 - Voltar")
    print("1 - Título")
    print("2 - Projeto")
    print("3 - Responsável")
    print("4 - Status")
    print("5 - Prazo")
    print("6 - concluir tarefa")
    print("7 - reabrir tarefa")


def interface():
    print("")
    print("="*20)
    print("RESUMO POR PROJETO")
    print("="*20)
    print("")