import json
import os
from datetime import datetime
ARQUIVO = "trabalho_de_python2/codigos/data/usuarios.json"
ARQUIVO3 = "trabalho_de_python2/codigos/data/tarefas.json"
ARQUIVO2= "trabalho_de_python2/codigos/data/projetos.json"
usuarios = []
projeto = []
tarefas = []

def carregar_usuarios():
    if not os.path.exists(ARQUIVO):
        return []
    try:
        with open(ARQUIVO, "r", encoding = "utf-8") as f:
            usuarios = json.load(f)
            return usuarios
    except json.JSONDecodeError:
        return []
def atualizar_usuarios(usuarios):
    with open(ARQUIVO, "w", encoding = "utf-8") as f:
        json.dump(usuarios, f, indent = 4, ensure_ascii = False)

def carregar_tarefas():
    if not os.path.exists(ARQUIVO3):
        return []
    try:
        with open(ARQUIVO3, "r", encoding = "utf-8") as f:
            usuarios = json.load(f)
            return usuarios
    except json.JSONDecodeError:
        return []
def atualizar_tarefas(tarefas):
    with open(ARQUIVO3, "w", encoding = "utf-8") as f:
        json.dump(tarefas, f, indent = 4, ensure_ascii = False)
carregar_usuarios()



def carregar_projetos():
    if not os.path.exists(ARQUIVO2):
        return []
    try:
        with open(ARQUIVO2, "r", encoding = "utf-8") as f:
            projetos = json.load(f)
            return projetos
    except json.JSONDecodeError:
        return []


def atualizar_projetos(projetos):
    with open(ARQUIVO2, "w", encoding = "utf-8") as f:
        json.dump(projetos, f, indent = 4, ensure_ascii = False)


carregar_projetos()
