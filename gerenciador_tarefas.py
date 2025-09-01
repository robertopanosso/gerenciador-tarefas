import json
from datetime import datetime
import sys 
sys.stdout.reconfigure(encoding="utf-8")

ARQUIVO_DADOS = "tarefas.json"

# ------------------ utilidades ------------------ #
def carregar_dados():
    """Carrega tarefas do arquivo JSON, se existir."""
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf - 8") as f:
            dados = json.load(f)
            return dados.get ("pendentes", []),dados.get ("concluidas",[])
    except FileNotFoundError:
        return [], []

def salvar_dados():
    """Salva as listas em JSON para manter o histórico."""                
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump({"pendentes": tarefas_pendentes,
                   "concluidas": tarefas_concluidas}, f,  indent=2, ensure_ascii=False)

def str_para_data(txt):
    """ Converte DD-MM-AAAA para datetime.date (ou None se erro)"""
    try:
        return datetime.strptime(txt, "%d-%m-%Y").date()
    except ValueError:
        return None
    
    # ------------------ funções de menu ------------------ #

def exibir_menu():
    print("\n===== MENU =====")
    print("1 - Adicionar nova tarefa")
    print("2 - Ver tarefas pendentes")
    print("3 - Marcar tarefa como concluída")
    print("4 - Editar tarefas pendentes")
    print("5 - Ver tarefas concluídas")
    print("6 - Filtrar tarefas por período")
    print("7 - Sair")


# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    desc = input("Descrição: ").strip()
    data_txt = input("Data (DD-MM-AAAA): ").strip()
    data = str_para_data(data_txt)
    if not data:
        print("Data inválida.")
        return
    prioridade = input("Prioridade (Baixa, Média ou Alta): ").strip().capitalize()
    tarefa = {"descricao": desc, "data": data_txt, "prioridade": prioridade}
    tarefas_pendentes.append(tarefa)
    salvar_dados()
    print("Tarefa adicionada.")

def listar (lista):
    if not lista:
        print("Nenhuma tarefa na lista.")
        return
    lista_ordenada = sorted(lista, key=lambda x: x["descricao"].lower())
    for i, t in enumerate(lista_ordenada):
        print(f"[{i}] {t['descricao'].title()} | {t['data']} | {t['prioridade']}")
def concluir_tarefa():
    if not tarefas_pendentes:
        print("Sem tarefas pendentes.")
        return
    listar(tarefas_pendentes)
    idx = input("Número da tarefa a concluir:")
    if idx.isdigit():
        idx = int(idx)
        if 0 <= idx < len(tarefas_pendentes):
            t = tarefas_pendentes.pop(idx)
            tarefas_concluidas.append(t)
            salvar_dados()
            print("Concluída.")
        else:
            print("Índice inválido.")

def editar_tarefa():
    if not tarefas_pendentes:
        print("Sem tarefas pendentes.")
        return
    listar(tarefas_pendentes)
    idx = input("Número da tarefa a editar: ")
    if not idx.isdigit():
        print("Entrada inválida. ")
        return
    idx = int(idx)
    if not (0 <= idx < len(tarefas_pendentes)):
        print("Índice fora do alcance.")
        return
    
    tarefa = tarefas_pendentes[idx]
    print("Deixe em branco para não alterar. ")
    nova_desc = input(f"Nova descrição [{tarefa['descricao']}]: ").strip()
    nova_data = input(f"Nova data (AAAA-MM-DD) [{tarefa['data']}]: ").strip()
    nova_prio = input(f"Nova prioridade [{tarefa['prioridade']}]: ").strip().capitalize()

    if nova_desc:
        tarefa["descricao"] = nova_desc
    if nova_data:
        if str_para_data(nova_data):
            tarefa["data"] = nova_data
        else:
            print("Data inválida - mantida original ")
    if nova_prio:
        tarefa["prioridade"] = nova_prio
    salvar_dados()
    print("Tarefa atualizada. ")
    
def filtrar_por_periodo():
    inicio_txt = input("Data inicial (AAAA-MM-DD): ").strip()
    fim_txt = input("Data final (AAAA-MM-DD): ").strip()
    ini = str_para_data(inicio_txt)
    fim = str_para_data(fim_txt)
    if not ini or not fim or ini > fim:
        print("Período inválido. ")
        return
    print("\nPendentes no período:")
    pend = [t for t in tarefas_pendentes if ini <= str_para_data(t["data"]) <= fim]
    listar(pend)
    print("\nConcluídas no período: ")
    conc = [t for t in tarefas_concluidas if ini <= str_para_data(t["data"]) <= fim]
    listar(conc)
    
# ------------------ programa principal ------------------ #

tarefas_pendentes, tarefas_concluidas = carregar_dados()

while True:
    exibir_menu()
    op = input("Opção: ").strip()
    if op == "1":
        adicionar_tarefa()
    elif op == "2":
        listar(tarefas_pendentes)
    elif op == "3":
        concluir_tarefa()
    elif op == "4":
        editar_tarefa()
    elif op == "5":
        listar(tarefas_concluidas)
    elif op == "6":
        filtrar_por_periodo()
    elif op == "7":
        print("Até logo!")
        break
    else:
        print("Opção inválida.")