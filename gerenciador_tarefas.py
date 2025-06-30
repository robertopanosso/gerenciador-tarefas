import sys 
sys.stdout.reconfigure(encoding='utf-8')
# Listas de tarefas
tarefas_pendentes = []
tarefas_concluidas = []

# Função para exibir o menu
def exibir_menu():
    print("\n===== MENU =====")
    print("1 - Adicionar nova tarefa")
    print("2 - Ver tarefas pendentes")
    print("3 - Marcar tarefa como concluída")
    print("4 - Ver tarefas concluídas")
    print("5 - Sair")

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ").strip()
    data = input("Digite a data de vencimento (AAAA-MM-DD): ").strip()
    prioridade = input("Digite a prioridade (Baixa, Média ou Alta): ").strip().capitalize()

    tarefa = {
        "descricao": descricao,
        "data": data,
        "prioridade": prioridade
    }

    tarefas_pendentes.append(tarefa)
    print("Tarefa adicionada com sucesso.")

# Função para listar tarefas (pendentes ou concluídas)
def listar_tarefas(lista):
    if lista:
        tarefas_ordenadas = sorted(lista, key=lambda x: x["descricao"].lower())
        for i, tarefa in enumerate(tarefas_ordenadas):
            print(f"[{i}] {tarefa['descricao'].title()} | Data: {tarefa['data']} | Prioridade: {tarefa['prioridade']}")
    else:
        print("Nenhuma tarefa para exibir.")

# Função para concluir uma tarefa
def concluir_tarefa():
    if tarefas_pendentes:
        tarefas_ordenadas = sorted(tarefas_pendentes, key=lambda x: x["descricao"].lower())
        print("\nTarefas pendentes:")
        for i, tarefa in enumerate(tarefas_ordenadas):
            print(f"[{i}] {tarefa['descricao'].title()} | Data: {tarefa['data']} | Prioridade: {tarefa['prioridade']}")

        escolha = input("Digite o número da tarefa que deseja marcar como concluída: ")

        if escolha.isdigit():
            indice = int(escolha)
            if 0 <= indice < len(tarefas_ordenadas):
                tarefa_concluida = tarefas_ordenadas[indice]
                tarefas_pendentes.remove(tarefa_concluida)
                tarefas_concluidas.append(tarefa_concluida)
                print(f"Tarefa '{tarefa_concluida['descricao'].title()}' marcada como concluída.")
            else:
                print("Índice inválido.")
        else:
            print("Entrada inválida. Digite um número.")
    else:
        print("Nenhuma tarefa para concluir.")

# Laço principal do programa
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        print("\nTarefas pendentes:")
        listar_tarefas(tarefas_pendentes)
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        print("\nTarefas concluídas:")
        listar_tarefas(tarefas_concluidas)
    elif opcao == "5":
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")