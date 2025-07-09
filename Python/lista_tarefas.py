tarefas = []
def mostrar_menu():
    print("""Lista de Tarefas
          1. Ver tarefas
          2. Adicionar uma tarefa
          3. Remover uma tarefa
          4. Sair""")

def ver_tarefas():
    if tarefas == []:
        print("Nenhuma tarefa adicionada.")
    else:
        print("Tarefas registradas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. (tarefa)")
                
mostrar_menu()
