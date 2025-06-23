#Validador de contraseñas

def valida(contrasena):
    tiene_numero = any(char.isdigit() 
                       for char in contrasena)
    return len(contrasena) >= 8 and tiene_numero

password = input("Introduce tu contraseña: ")

if valida(password):
    print("Tu contraseña es valida.")
else:
    print("Contraseña invalida.")