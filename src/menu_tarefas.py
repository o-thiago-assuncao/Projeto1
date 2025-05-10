tarefas = []

def mostrar_menu():
    print("\n=== Menu de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, tarefa in enumerate(tarefas):
            status = "[✔]" if tarefa["concluida"] else "[ ]"
            print(f"{i + 1}. {status} {tarefa['descricao']}")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "1":
        desc = input("Digite a nova tarefa: ")
        tarefas.append({"descricao": desc, "concluida": False})
        print("Tarefa adicionada com sucesso.")

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        listar_tarefas()
        num = int(input("Digite o número da tarefa concluída: "))
        if 0 < num <= len(tarefas):
            tarefas[num - 1]["concluida"] = True
            print("Tarefa marcada como concluída.")
        else:
            print("Número inválido.")

    elif opcao == "4":
        listar_tarefas()
        num = int(input("Digite o número da tarefa a remover: "))
        if 0 < num <= len(tarefas):
            tarefas.pop(num - 1)
            print("Tarefa removida.")
        else:
            print("Número inválido.")

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
