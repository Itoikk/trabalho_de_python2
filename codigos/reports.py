import json
from datetime import datetime




arquivo1="c:\\Users\\milen\\OneDrive\\Área de Trabalho\\Trabalho de Python\\trabalho_de_python2\\codigos\\data\\projetos.json"
arquivo2="c:\\Users\\milen\\OneDrive\\Área de Trabalho\\Trabalho de Python\\trabalho_de_python2\\codigos\\data\\usuarios.json"
arquivo3="c:\\Users\\milen\\OneDrive\\Área de Trabalho\\Trabalho de Python\\trabalho_de_python2\\codigos\\data\\tarefas.json"

with open(arquivo1, 'r', encoding='utf-8') as f:
    dados1 = json.load(f)

with open(arquivo2, 'r', encoding='utf-8') as f:
    dados2 = json.load(f)

with open(arquivo3, 'r', encoding='utf-8') as f:
    dados3 = json.load(f)


#qntd_total_tarefas_projetos

print("")

for projeto in dados1:
    i=0
    for tarefa in dados3:
        if projeto['nome']==tarefa['projeto']:
            i+=1
    print(projeto['nome'] ,i)

print("")

#qntd_status_tarefas_projetos

for projetos in dados1:
    contadora_projetos_conc=0
    contadora_projeto_and=0
    contadora_projeto_pend=0
    for tarefa in dados3:
        if projeto['nome']==tarefa['projeto']:
            if tarefa['status']=='concluida':
                contadora_projetos_conc+=1
            elif tarefa['status']=='em andamento':
                contadora_projeto_and+=1
            else:
                contadora_projeto_pend+=1
    print(projetos['nome'])
    print("Quantidade de tarefas concluídos:",contadora_projetos_conc)
    print("Quantidade de tarefas em andamento:",contadora_projeto_and)
    print("Quantidade de tarefas pendentes:",contadora_projeto_pend)

print("")

#Porcentagem Concluído

for projetos in dados1:
    contadora_projetos_conc=0
    for tarefas in dados3:
        if projeto['nome']==tarefa['projeto']:
            if tarefa['status']=='concluida':
                contadora_projetos_conc+=1
        porcentagem_concluido=(contadora_projetos_conc/len(dados3))*100
        print(f"Porcentagem de tarefas concluídas no projeto {projetos['nome']}: {porcentagem_concluido:.2f}%")

print("")

#Tarefas concluidas no prazo

dia_atual=datetime.now()
for projeto in dados1:
    contadora_projetos_conc=0
    for tarefa in dados3:
        if projeto['nome']==tarefa['projeto']:
            if tarefa['status']=='concluida':
                tarefa['prazo']=datetime.strptime(tarefa['prazo'], "%Y/%m/%d")
                if tarefa['prazo']>=dia_atual:
                    contadora_projetos_conc+=1
    print(f"Número de tarefas concluídas no prazo no projeto {projeto['nome']}: {contadora_projetos_conc}")
print("")
#Tarefas atrasadas

for projeto in dados1:
    contadora_projetos_pend=0
    for tarefa in dados3:
        if projeto['nome']==tarefa['projeto']:
            if tarefa['status']=='em andamento' or tarefa['status']=='pendente':
                tarefa['prazo']=datetime.strptime(tarefa['prazo'], "%Y/%m/%d")
                if tarefa['prazo']<=dia_atual:
                    contadora_projetos_pend+=1
    print(f"Número de tarefas expiradas no projeto {projeto['nome']}: {contadora_projetos_pend}")

