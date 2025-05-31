import os

# Función para limpiar la pantalla (multiplataforma)
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Preguntas con sus respuestas correctas (True o False)
preguntas = [
    ("0", False),
    ("1", True),
    ("\"\"", False),
    ("\"hola\"", True),
    ("[]", False),
    ("[1, 2, 3]", True),
    ("None", False),
    ("{}", False),
    ("{\"a\": 1}", True)
]

def juego_verdadero_falso():
    clear()
    print("¡Bienvenido al juego de Verdadero o Falso en Python!")
    print("Debes adivinar si la siguiente expresión es True o False según bool().\n")
    
    puntaje = 0
    
    for expr, respuesta in preguntas:
        print(f"¿La expresión {expr} es True o False?")
        user_input = input("Escribe 'V' para Verdadero o 'F' para Falso: ").strip().upper()
        
        # Validar entrada del usuario
        if user_input not in ('V', 'F'):
            print("¡Entrada inválida! Usa 'V' o 'F'.\n")
            continue
        
        user_respuesta = (user_input == 'V')
        
        if user_respuesta == respuesta:
            print("✅ ¡Correcto!\n")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta era {'Verdadero' if respuesta else 'Falso'}.\n")
    
    print(f"¡Juego terminado! Puntaje final: {puntaje}/{len(preguntas)}")

# Iniciar el juego
juego_verdadero_falso()