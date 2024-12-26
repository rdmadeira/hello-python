# Operadores aritmetricos:
a = 10
b = 5

print(a + b)

print(a - b)
print(a * b)
print(a / b)
print(
    "El resultado de una división es un float: ",
    type(a / b),
)
print(a % b)  # Modulus - sería el resto de una división
# Floordivision - es el resultado aproximado, o el numero intero del resultado de la división
print(a // b)
print(a**b)  # Exponencial

c = "Hola"
d = "Python"

print(c + " " + d)  # Operador + para strings ----> OK

# print("Hola" + 5) # ------> TypeError: can only concatenate str (not "int") to str
print("Hola " + str(5))  # Hola 5 ----------> OK
print(
    "Hola " * 10
)  # Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola   ---> OK
# Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola  ----> OK <------ Hay que convertir el resultado en int, porque era float
print("Hola " * int(10 * 5 / 10 + 20 - 10))

# Operadores comparativos:
print(3 > 4)  # False (bool)  - Mayor o menor
print(3 >= 4)  # False (bool) - Mayor igual o menor igual
print(3 + 1 == 4)  # True (bool) - es igual
print(
    3 + 1 != 4
)  # False - es distinto  # Las lugaturas arriba es porque instalé "Fire Code" y en Settings, agregué esta fuente con editor.fontLigatures: true

print(3 < 4 < 5)  # True
print(3 < 8 <= 5)  # False

f = bool(0)
print(
    f,
    type(f),
)

# Comparativos con Strings:
print("Hola" <= "Python")  # True
print("Hola" > "Python")  # False - compara los ordenes alfabeticos por ASCII:
print(
    "aaaa >= aaba: ",
    "aaaa" >= "aaba",
)  # False
print(
    "abaa >= aaba: ",
    "abaa" >= "aaba",
)  # True
print(
    "aAaa >= aaba: ",
    "aAaa" >= "aaba",
)  # False - con mayuscula no
print(
    "AAAA >= aaba: ",
    "AAAA" >= "aaba",
)  # False
print(
    "AAAA >= aaaa: ",
    "AAAA" >= "aaaa",
)  # False
# True - minuscula viene primero!!!! por ASCII
print(
    "AAAA <= aaaa: ",
    "AAAA" <= "aaaa",
)
print(
    "aaaa >= aaaa: ",
    "aaaa" >= "aaaa",
)  # True


print("Hola" == "Python")  # False
print("Hola" == "Hola")  # True
print("Hola" == "Pyth")  # True - compara sos strings

# Operadores Lógicos:
print(
    "aaaa >= aaba and abaa <= aaba: ",
    "aaaa" >= "aaba" and "abaa" <= "aaba",
)  # False && True = False
print(
    "aaaa >= aaba or abaa <= aaba: ",
    "aaba" >= "aaba" or "abaa" <= "aaba",
)  # False || True = True

# Se puede agrupar para hacer un orden lógico, con uso de parenthesis:
print(3 < 4 and (4 > 3 or 0.5 > 2))  # True

# Not:
print(not (3 < 4 and (4 > 3 or 0.5 > 2)))  # False
print(3 < 4 and (not (4 > 3) or 0.5 > 2))  # False - not es como ! en JS

print(2 * 4)
