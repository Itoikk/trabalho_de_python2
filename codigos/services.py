from models import *
from storage import *
from utils import *
from datetime import datetime
def listar_usuarios(lista):
    for indice, usuario in enumerate(lista):
        print(f"nome: {lista[indice]["nome"]}")
        print(f"email: {lista[indice]["email"]}")
        print(f"função: {lista[indice]["perfil"]}")
        print()
        print()
def adicionar_usuario(nome, email, perfil = "user"):
    usuarios = carregar_usuarios()
    usuario = {
        "nome": nome,
        "email": email,
        "perfil": perfil
    }
    usuarios.append(usuario)
    atualizar_usuarios(usuarios)
def atualizar_usuario(indice, nome, email, perfil = "user"):
    usuarios = carregar_usuarios()
    usuario = {
        "nome": nome,
        "email": email,
        "perfil": perfil
    }
    usuarios[indice] = usuario
    atualizar_usuarios(usuarios)    
def remover_usuario(indice):
    usuarios = carregar_usuarios()
    usuarios.pop(indice)
    atualizar_usuarios(usuarios)



def adicionar_tarefa(titulo, projeto, responsavel, status, prazo):
    tarefas = carregar_tarefas()
    tarefa = {
        "titulo": titulo,
        "projeto": projeto,
        "responsavel": responsavel,
        "status": status,
        "prazo": prazo
        }
    tarefas.append(tarefa)
    atualizar_tarefas(tarefas)
def listar_tarefas(lista):
    for tarefa in lista:
        print(f"Título: {tarefa["titulo"]}")
        print(f"Projeto: {tarefa["projeto"]}")
        print(f"Responsavel: {tarefa["responsavel"]}")
        print(f"Status: {tarefa["status"]}")
        print(f"Prazo: {tarefa["prazo"]}")
        print()
        print()
def atualizar_tarefa(indice, titulo, projeto, responsavel, status, prazo):
    tarefas = carregar_tarefas()
    tarefa = {
        "titulo": titulo,
        "projeto": projeto,
        "responsavel": responsavel,
        "status": status,
        "prazo": prazo
    }
    tarefas[indice] = tarefa
    atualizar_tarefas(tarefas)
def remover_tarefa(indice):
    tarefas = carregar_tarefas()
    tarefas.pop(indice)
    atualizar_tarefas(tarefas)
def atualizar_tarefa_titulo(indice, titulo):
    tarefas = carregar_tarefas()
    tarefas[indice]["titulo"] = titulo
    atualizar_tarefas(tarefas)
def atualizar_tarefa_projeto(indice, projeto):
    tarefas = carregar_tarefas()
    tarefas[indice]["projeto"] = projeto
    atualizar_tarefas(tarefas)
def atualizar_tarefa_responsavel(indice, responsavel):
    tarefas = carregar_tarefas()
    tarefas[indice]["responsavel"] = responsavel
    atualizar_tarefas(tarefas) 
def atualizar_tarefa_status(indice, status):
    tarefas = carregar_tarefas()
    tarefas[indice]["status"] = status
    atualizar_tarefas(tarefas)
def atualizar_tarefa_prazo(indice, prazo):
    tarefas = carregar_tarefas()
    tarefas[indice]["prazo"] = prazo
    atualizar_tarefas(tarefas)
def listar_tarefas_por_projetos(lista, nome_projeto):
    for tarefa in lista:
        if tarefa["projeto"]==nome_projeto:
            print(f"Título: {tarefa["titulo"]}")
            print(f"Projeto: {tarefa["projeto"]}")
            print(f"Responsavel: {tarefa["responsavel"]}")
            print(f"Status: {tarefa["status"]}")
            print(f"Prazo: {tarefa["prazo"]}")
            print()
            print()
def listar_tarefas_responsavel(lista, nome_responsavel):
    for tarefa in lista:
        if tarefa["responsavel"]==nome_responsavel:
            print(f"Título: {tarefa["titulo"]}")
            print(f"Projeto: {tarefa["projeto"]}")
            print(f"Responsavel: {tarefa["responsavel"]}")
            print(f"Status: {tarefa["status"]}")
            print(f"Prazo: {tarefa["prazo"]}")
            print()
            print()
def listar_tarefas_por_status(lista, status):
    for tarefa in lista:
        if tarefa["status"]==status:
            print(f"Título: {tarefa["titulo"]}")
            print(f"Projeto: {tarefa["projeto"]}")
            print(f"Responsavel: {tarefa["responsavel"]}")
            print(f"Status: {tarefa["status"]}")
            print(f"Prazo: {tarefa["prazo"]}")
            print()
            print()


def adicionar_projeto(nome, inicio, fim, descricao = "Descricao vazia"):
    projetos = carregar_projetos()
    projeto = {
        "nome": nome,
        "inicio": inicio,
        "fim": fim,
        "descricao": descricao
    }
    projetos.append(projeto)
    atualizar_projetos(projetos)
def atualizar_projeto(indice, nome, inicio, fim, descricao = "Descricao vazia"):
    projetos = carregar_projetos()
    projeto = {
        "nome": nome,
        "inicio": inicio,
        "fim": fim,
        "descicao": descricao
    }
    projetos[indice] = projeto
    atualizar_projetos(projetos)
def listar_projetos(lista):
    for indice, projeto in enumerate(lista):
        print(f"nome: {lista[indice]["nome"]}")
        print(f"inicio: {lista[indice]["inicio"]}")
        print(f"fim: {lista[indice]["fim"]}")
        print(f"descricao: {lista[indice]["descricao"]}")
        print()
def remover_projeto(indice):
    projetos = carregar_projetos()
    projetos.pop(indice)
    atualizar_projetos(projetos)


