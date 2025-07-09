import random
rooms={"Corredor": {"sul":"Cozinha", "leste":"Sala de Jantar"},
    "Cozinha": {"norte":"Corredor"}, "Sala de Jantar":{"oeste":"Corredor"}, 
    "Biblioteca":{"sul":"Corredor"}}

def main():  
    
    current_room = "Corredor"
    inventario = []
    vidas = 2
    itens = ["Espada", "Tesouro", "Monstro", "Elixir"]
    for room in rooms:
        item = random.choice(itens)
        rooms[room]["item"] = item
        itens.remove(item)
    
    while True:  
        
        #print(f"\nRoom: {current_room}, Item: {rooms[current_room]['item']}")
        #print(f"Você está noa(a) {current_room} e vê um(a) {rooms[current_room]['item']}")
        if "item" in rooms[current_room] and rooms[current_room]["item"] != "Monstro":
            print(f"Você está noa(a) {current_room} e vê um(a) {rooms[current_room]['item']}")
            comando = input("Você prefere: pegar o item, outro caminho ou desistir> ").lower()
            if comando == "pegar o item":
                inventario.append(rooms[current_room]["item"])
                print(f"Você pegou o {rooms[current_room]['item']}!")
                del rooms[current_room]["item"]
                if "Tesouro" in inventario:
                    print("Parabéns! Você achou o tesouro e ganhou o jogo!")
                    break
                elif "item" in rooms[current_room] and rooms[current_room]['item']=="Elixir":
                    vidas += 1
                    print(f"Você ganhou mais uma vida!\nVidas restantes: {vidas}")

            elif comando == "outro caminho":
                direcao = input("Escolha uma direcao: ")
                if direcao in rooms[current_room]:
                    current_room = rooms[current_room][direcao]
                else:
                    print("Você não pode ir por este caminho!")
            elif comando == "desistir":
                print("Você desistiu do jogo...")
                break
            else:
                print("Comando inválido.")

        elif "item" in rooms[current_room] and rooms[current_room]["item"]=="Monstro":
            print(f"Você está no(a) {current_room} e vê um(a) {rooms[current_room]['item']}")
            if "Espada" in inventario:
                print("Parabéns, você matou o monstro e venceu o jogo!!")
                break
            else:
                vidas -= 1
                print(f"Um monstro pegou você... Você perdeu 1 vida!\nVidas restantes: {vidas}")
                current_room=random.choice(list(rooms.keys()))
                
                if vidas <= 0:
                    print("Fim de jogo!")
                    break
        
        else:
            direcao = input(f"Você está noa(a) {current_room}, escolha uma direcao: ")
            if direcao in rooms[current_room]:
                current_room = rooms[current_room][direcao]
            else:
                print("Você não pode ir por este caminho!")


main()