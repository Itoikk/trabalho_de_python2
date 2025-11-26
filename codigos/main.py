from ui import *
from storage import *
from models import *
from services import *
from utils import *
from datetime import datetime

import os, sys, json, time
while True:
    usuarios = carregar_usuarios()
    tarefas = carregar_tarefas()
    projetos = carregar_projetos()
    os.system("cls")
    menu_inicio()
    opcao_menu = input("")
    if opcao_menu not in ["1", "2", "3"]:
        sys.exit("Opção inválida!")
        time.sleep(1)
        continue
    elif opcao_menu == "1":
        #Usuario
        while True:
            usuarios = carregar_usuarios()
            menu_usuarios()
            opcao_usuario = input("")
            if opcao_usuario not in ["0", "1", "2", "3", "4", "5"]:
                continue
            if opcao_usuario == "0":
                break
            elif opcao_usuario == "1":
                #CADASTRAR
                nome = input("nome: ")
                if nome == "":
                        print("nome não pode ser vazio!")
                        time.sleep(1)
                        continue
                email = input("email: ")
                for usuario in usuarios:
                    if usuario["email"] == email:
                        print("email já cadastrado!")
                        time.sleep(1)
                        break
                else:
                    perfil = input("perfil: ")
                    if perfil == "":
                        adicionar_usuario(nome, email)
                    else:
                        adicionar_usuario(nome, email, perfil)
                    print("Usuario Adicionado!")
                    time.sleep(1)
                    break
            elif opcao_usuario == "2":
                #listar
                listar_usuarios(usuarios)
                input()
                break
            elif opcao_usuario == "3":
                indices = []
                email = input("email: ")
                if email != "":
                    for indice, usuario in enumerate(usuarios):
                        if email == usuario["email"]:
                            indices.append(indice)
                            mostrar_usuarios(indices, usuarios)
                            input()
                            break
                    else:
                        print("usuário não encontrado!")
                        time.sleep(1)
                        break
                    break
                nome = input("nome: ")
                if nome != "":
                    condicao = True
                    for indice, usuario in enumerate(usuarios):
                        if nome == usuario["nome"]:
                            indices.append(indice)
                            condicao = False
                    if condicao:
                        print("usuário não encontrado!")
                        time.sleep(1)
                        break
                    mostrar_usuarios(indices, usuarios)
                    input()
                    break
                else:
                    print("usuário não encontrado!")
                    time.sleep(1)
                    break
            elif opcao_usuario == "4":
                #atualizar
                email = input("email: ")
                for index, usuario in enumerate(usuarios):
                    if usuario["email"] == email:
                        indice = index
                        break
                else:
                    print("email não encontrado")
                    time.sleep(1)
                    break
                nome = input("novo nome: ")
                if nome == "":
                    nome = usuarios[indice]["nome"]
                email = input("novo email: ")
                email_ja_cadastrado=False
                for usuario in usuarios:
                    if email == usuario["email"]:
                        print("email já cadastrado!")
                        email_ja_cadastrado=True
                if email_ja_cadastrado:
                    time.sleep(1)
                    break
                if email == "":
                    email = usuarios[indice]["email"]
                perfil = input("novo perfil: ")
                if perfil == "":
                    perfil = usuarios[indice]["perfil"]
                atualizar_usuario(indice, nome, email, perfil)
                print("atualizado!")
                time.sleep(1)
            elif opcao_usuario == "5":
                email = input("email: ")
                for indice, usuario in enumerate(usuarios):
                    if usuario["email"] == email:
                        remover_usuario(indice)
                        print("usuário removido!")
                        time.sleep(1)
                        break
                else:
                    print("email não cadastrado!")
                    time.sleep(1)
                break              
    elif opcao_menu == "2":
        print("Você escolheu Projetos!")
        while True:
            #Projetos
            projetos = carregar_projetos()
            menu_projetos()
            opcao_projetos = input("")
            if opcao_projetos not in ["0", "1", "2", "3", "4", "5"]:
                continue
            if opcao_projetos == "0":
                break
            elif opcao_projetos == "1":
                #Cadastrar projeto
                nome_projeto = input("nome do projeto: ")
                if nome_projeto == "":
                    print("nome do projeto não pode ser vazio!")
                    time.sleep(1)
                    continue
                for projeto in projetos:
                    if nome_projeto == projeto["nome"]:
                        print("Já existe um projeto com este nome!")
                        time.sleep(1)
                        break
                descricao = input("descrição: ")
                inicio = input("Digite a data de início(YYYY/MM/DD):")
                if not data_valida(inicio):
                    print("data inválida")
                    time.sleep(1)
                    break
                fim = input("Digite a data de encerramento(YYYY/MM/DD):")
                if not data_valida(fim):
                    print("data inválida")
                    time.sleep(1)
                    break
                adicionar_projeto(nome_projeto, inicio, fim, descricao)
                break
            
            elif opcao_projetos == "2":
                #listar projetos
                listar_projetos(projetos)
                input()
                break

            elif opcao_projetos == "3":
                #buscar projeto
                indices = []
                nome_projeto = input("nome do projeto: ")
                if nome_projeto != "":
                    for indice, projeto in enumerate(projetos):
                        if nome_projeto == projeto["nome"]:
                            indices.append(indice)
                            mostrar_projetos(indices, projetos)
                            input()
                            break
                    else:
                        print("projeto não encontrado!")
                        time.sleep(1)
                        break
                    break
                





            elif opcao_projetos == "4":
                #atualizar projeto
                nome_projeto1 = input("nome: ")
                for index, projeto in enumerate(projetos):
                    if projeto["nome"] == nome_projeto1:
                        indice = index
                        break
                else:
                    print("nome do projeto não encontrado")
                    time.sleep(1)
                    break
                nome_projeto1 = input("novo nome do projeto: ")
                if nome_projeto1 == "":
                    nome_projeto1 = projetos[indice]["nome"]
                inicio_projeto1 = input("nova data de inicio(YYYY/MM/DD): ")
                if not data_valida(inicio_projeto1):
                    print("data inválida")
                    time.sleep(1)
                    break
                if inicio_projeto1 == "":
                    inicio_projeto1 = projetos[indice]["inicio"]
                fim_projeto1 = input("nova data de encerramento(YYYY/MM/DD): ")
                if not data_valida(fim_projeto1):
                    print("data inválida")
                    time.sleep(1)
                    break
                if fim_projeto1 == "":
                    fim_projeto1 = projetos[indice]["fim"]
                descricao_projeto1 = input("nova descricao: ")
                if descricao_projeto1 == "":
                    descricao_projeto1 = projetos[indice]["descricao"]
                atualizar_projeto(indice, nome_projeto1, inicio_projeto1, fim_projeto1, descricao_projeto1)
                print("atualizado!")
                time.sleep(1)






            elif opcao_projetos == "5":
                #remover projetos
                nome_projeto = input("nome: ")
                for indice, projeto in enumerate(projetos):
                    if projeto["nome"] == nome_projeto:
                        remover_projeto(indice)
                        print("projeto removido!")
                        time.sleep(1)
                        break
                else:
                    print("projeto não cadastrado!")
                    time.sleep(1)
                break         
            









    elif opcao_menu == "3":
        print("Você escolheu Tarefas!")
        while True:
            tarefas = carregar_tarefas()
            menu_tarefas()
            opcao_tarefas = input()
            if opcao_tarefas not in ["0", "1", "2", "3", "4"]:
                print("Opção inválida!")
                time.sleep(1)
                continue
            if opcao_tarefas == "0":
                break
            if  opcao_tarefas == "1":
                titulo_tarefa = input("nome: ")
                if titulo_tarefa == "":
                    print("o título não deve ser vazio!")
                    time.sleep(1)
                    break
                projeto_tarefa = input("projeto: ")
                for projeto in projetos:
                    if projeto_tarefa == projeto["nome"]:
                        break
                else:
                    print("Projeto não existe!")
                    time.sleep(1)
                    break
                responsavel_tarefa = input("responsável: ")
                if responsavel_tarefa == "":
                    print("a tarefa deve ter um responsável!")
                    time.sleep(1)
                    break
                status_tarefa=""
                while status_tarefa not in ["pendente", "em andamento", "concluida", "cancelar"]:
                    status_tarefa = padronizar_texto(input("status: "))
                    if status_tarefa == "cancelar":
                        break
                    if status_tarefa in ["pendente", "em andamento", "concluida"]:
                        break
                    print("status inválido!")
                    time.sleep(1)
                print("ex: YYYY/MM/DD")
                prazo_tarefa = input("prazo: ")
                if not data_valida(prazo_tarefa):
                    print("data inválida")
                    time.sleep(1)
                    break
                adicionar_tarefa(titulo_tarefa, projeto_tarefa, responsavel_tarefa, status_tarefa, prazo_tarefa)
                print("Tarefa adicionada!")
                time.sleep(1)
                break
            if opcao_tarefas == "2":
                while True:
                    menu_listar_tarefas()
                    opcao_listar_tarefas = input()
                    if opcao_listar_tarefas not in ["0", "1", "2", "3", "4"]:
                        print("Opcão inválida")
                        time.sleep(1)
                        continue
                    if opcao_listar_tarefas == "0":
                        break
                    if opcao_listar_tarefas == "1":
                        listar_tarefas(tarefas)
                        input()
                        break
                    if opcao_listar_tarefas == "2":
                        projeto_tarefa=input("projeto: ")
                        listar_tarefas_por_projetos(tarefas, projeto_tarefa)
                        input()
                        break
                    if opcao_listar_tarefas == "3":
                        responsavel_tarefa=input("responsável: ")
                        listar_tarefas_responsavel(tarefas, responsavel_tarefa)
                        input()
                        break
                    if opcao_listar_tarefas == "4":
                        status_tarefa=padronizar_texto(input("status: "))
                        print()

                        if status_tarefa not in ["pendente", "em andamento", "concluida"]:
                            print("status inválido!")
                            time.sleep(1)
                            break
                        listar_tarefas_por_status(tarefas, status_tarefa)
                        input()
                        break  


            if opcao_tarefas == "3":
                #atualizar tarefas
                menu_atualizar_tarefa()
                opcao_atualizar_tarefa = input()
                if opcao_atualizar_tarefa not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
                    print("Opção inválida!")
                    time.sleep(1)
                    continue
                if opcao_atualizar_tarefa == "0":
                    break


                if opcao_atualizar_tarefa == "1":
                    #atualizar título
                    titulo_tarefa = input("título da tarefa: ")
                    for index, tarefa in enumerate(tarefas):
                        if tarefa["titulo"] == titulo_tarefa:
                            indice = index
                    if tarefa["status"] == "concluida":
                            print("não é possível atualizar uma tarefa concluída!")
                            time.sleep(1)
                            break
                    elif tarefa["titulo"] != titulo_tarefa:
                        print("tarefa não encontrada!")
                        time.sleep(1)
                        break
                    novo_titulo = input("novo título: ")
                    if novo_titulo == "":
                        novo_titulo = tarefas[indice]["titulo"]
                    atualizar_tarefa_titulo(indice, novo_titulo)
                    print("título atualizado!")
                    time.sleep(1)


                elif opcao_atualizar_tarefa == "2":
                    #atualizar projeto
                    titulo_tarefa = input("título da tarefa: ")
                    for index, tarefa in enumerate(tarefas):
                        if tarefa["titulo"] == titulo_tarefa:
                            indice = index
                            break
                    if tarefa["status"] == "concluida":
                            print("não é possível atualizar uma tarefa concluída!")
                            time.sleep(1)
                            break
                    elif tarefa["titulo"] != titulo_tarefa:
                        print("tarefa não encontrada!")
                        time.sleep(1)
                        break
                    novo_projeto = input("novo projeto: ")
                    if novo_projeto == "":
                        novo_projeto = tarefas[indice]["projeto"]
                    atualizar_tarefa_projeto(indice, novo_projeto)
                    print("projeto atualizado!")
                    time.sleep(1)


                elif opcao_atualizar_tarefa == "3":
                    #atualizar responsavel
                    titulo_tarefa = input("título da tarefa: ")
                    for index, tarefa in enumerate(tarefas):
                        if tarefa["titulo"] == titulo_tarefa:
                            indice = index
                            break
                    if tarefa["status"] == "concluida":
                            print("não é possível atualizar uma tarefa concluída!")
                            time.sleep(1)
                            break
                    elif tarefa["titulo"] != titulo_tarefa:
                        print("tarefa não encontrada!")
                        time.sleep(1)
                        break
                    novo_responsavel = input("novo responsável: ")
                    if novo_responsavel == "":
                        novo_responsavel = tarefas[indice]["responsavel"]
                    atualizar_tarefa_responsavel(indice, novo_responsavel)
                    print("responsável atualizado!")
                    time.sleep(1)


                elif opcao_atualizar_tarefa == "4":
                    #atualizar status
                    titulo_tarefa = input("título da tarefa: ")
                    for index, tarefa in enumerate(tarefas):
                        if tarefa["titulo"] == titulo_tarefa:
                            indice = index
                            break
                    if tarefa["status"] == "concluida":
                            print("não é possível atualizar uma tarefa concluída!")
                            time.sleep(1)
                            break
                    elif tarefa["titulo"] != titulo_tarefa:
                        print("tarefa não encontrada!")
                        time.sleep(1)
                        break
                    novo_status = padronizar_texto(input("novo status: "))
                    if novo_status == "":
                        novo_status = tarefas[indice]["status"]
                    if novo_status not in ["pendente", "em andamento", "concluida"]:
                        print("status inválido!")
                        time.sleep(1)
                        break
                    atualizar_tarefa_status(indice, novo_status)
                    print("status atualizado!")
                    time.sleep(1)


                elif opcao_atualizar_tarefa == "5":
                    #atualizar prazo
                    titulo_tarefa = input("título da tarefa: ")
                    for index, tarefa in enumerate(tarefas):
                        if tarefa["titulo"] == titulo_tarefa:
                            indice = index
                            break
                    if tarefa["status"] == "concluida":
                            print("não é possível atualizar uma tarefa concluída!")
                            time.sleep(1)
                            break
                    elif tarefa["titulo"] != titulo_tarefa:
                        print("tarefa não encontrada!")
                        time.sleep(1)
                        break
                    print("ex: YYYY-MM-DD")
                    novo_prazo = input("novo prazo: ")
                    if novo_prazo == "":
                        novo_prazo = tarefas[indice]["prazo"]
                    if not data_valida(novo_prazo):
                        print("data inválida")
                        time.sleep(1)
                        break
                    atualizar_tarefa_prazo(indice, novo_prazo)
                    print("prazo atualizado!")
                    time.sleep(1)
                

                elif opcao_atualizar_tarefa == "6":
                    #concluir tarefa
                    titulo_tarefa = input("título da tarefa: ")
                    for index, tarefa in enumerate(tarefas):
                        if tarefa["titulo"] == titulo_tarefa:
                            indice = index
                            break
                    if tarefa["status"] == "concluida":
                            print("não é possível atualizar uma tarefa concluída!")
                            time.sleep(1)
                            break
                    elif tarefa["titulo"] != titulo_tarefa:
                        print("tarefa não encontrada!")
                        time.sleep(1)
                        break
                    atualizar_tarefa_status(indice, "concluida")
                    print("tarefa concluída!")
                    time.sleep(1)
                

                elif opcao_atualizar_tarefa == "7":
                    #reabrir tarefa
                    titulo_tarefa = input("título da tarefa: ")
                    for index, tarefa in enumerate(tarefas):
                        if tarefa["titulo"] == titulo_tarefa:
                            indice = index
                            break
                    else:
                        print("tarefa não encontrada!")
                        time.sleep(1)
                        break
                    atualizar_tarefa_status(indice, "em andamento")
                    print("tarefa reaberta!")
                    time.sleep(1)


                
            if opcao_tarefas == "4":
                #remover tarefas
                nome_tarefa = input("título da tarefa: ")
                for indice, tarefa in enumerate(tarefas):
                    if tarefa["titulo"] == nome_tarefa:
                        remover_tarefa(indice)
                        print("tarefa removida!")
                        time.sleep(1)
                        break
                else:
                    print("tarefa não encontrada!")
                    time.sleep(1)
                break
            