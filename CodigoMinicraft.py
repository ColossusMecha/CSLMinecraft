# CSLMinecraft
CSL Minecraft V.1 

import time

inventory = {
    "madera": 0,
    "piedra": 0,
    "pico": 0
}

def show_inventory():
    print("\n🧺 Inventario:")
    for item, qty in inventory.items():
        print(f"- {item.capitalize()}: {qty}")
    print()

def chop_tree():
    print("🌲 Has cortado un arbol...")
    inventory["madera"] += 1
    time.sleep(1)

def mine_stone():
    if inventory["pico"] > 0:
        print("⛏️ Has minado piedra...")
        inventory["piedra"] += 1
        time.sleep(1)
    else:
        print("❌ Necesitas un pico para minar piedra ")

def craft_pickaxe():
    if inventory["madera"] >= 3:
        print("🛠️Fabricando un pico...¡ Ahora tienes un pico!.")
        inventory["madera"] -= 3
        inventory["pico"] += 1
        time.sleep(1)
    else:
        print("❌ No tienes suficiente madera. Recolecta 3 ")

def game_loop():
    print("🔹 Bienvenido a Minicraft 🔹")
    while True:
        print("\n Escoge una acción:")
        print("1. Talar un arbol 🌲")
        print("2. Minar piedra ⛏️")
        print("3. Fabricar un pico 🛠️")
        print("4. Mostrar el inventario 🧺")
        print("5. Salir ❌")

        choice = input(">> ")

        if choice == "1":
            chop_tree()
        elif choice == "2":
            mine_stone()
        elif choice == "3":
            craft_pickaxe()
        elif choice == "4":
            show_inventory()
        elif choice == "5":
            print("Hasta pronto, explorador.")
            break
        else:
            print("❓ Opción no válida...Intenta nuevamente")

game_loop()
