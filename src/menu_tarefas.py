tarefas = []

def mostrar_menu():
    print("\n=== Menu ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")

def ver_tarefas():
    if not tarefas:
        print("Nenhuma tarefa.")
    else:
        for i, tarefa in enumerate(tarefas):
            status = "✔" if tarefa["feito"] else " "
            print(f"{i + 1}. [{status}] {tarefa['texto']}")

while True:
    mostrar_menu()
    opcao = input("Escolha (1-5): ")

    if opcao == "1":
        texto = input("Tarefa: ")
        tarefas.append({"texto": texto, "feito": False})

    elif opcao == "2":
        ver_tarefas()

    elif opcao == "3":
        ver_tarefas()
        try:
            num = int(input("Número da tarefa concluída: "))
            tarefas[num - 1]["feito"] = True
        except:
            print("Número inválido.")

    elif opcao == "4":
        ver_tarefas()
        try:
            num = int(input("Número da tarefa a remover: "))
            tarefas.pop(num - 1)
        except:
            print("Número inválido.")

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
