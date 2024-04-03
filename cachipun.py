import random
import sys

usuario = sys.argv[1]

opciones = ["piedra", "papel", "tijeras"]

npc = random.choice(opciones)

if usuario not in opciones:
    print(f'{usuario.upper()} no es una opción válida. Debe escoger entre: {opciones}')
else:
    if usuario == npc:
        print("Empate")
    elif ((usuario == "piedra" and npc == "tijeras") or
            (usuario == "papel" and npc == "piedra") or
            (usuario == "tijeras" and npc == "papel")):
        print("GANASTE!!!")
    else:
        print("Perdiste tonto :(", npc)
