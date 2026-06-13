from g4f.client import Client

# Inicializamos un cliente libre que se conecta a modelos de lenguaje modernos
client = Client()

print("🤖 ¡Hola! Soy tu IA sin restricciones de región. Escribe 'salir' para terminar.")

while True:
    usuario = input("\nTú: ")
    
    if usuario.lower() == "salir":
        print("🤖 ¡Adiós!")
        break
        
    # Le pedimos una respuesta a un modelo de lenguaje grande
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": usuario}],
    )
    
    print(f"\nIA: {response.choices[0].message.content}")