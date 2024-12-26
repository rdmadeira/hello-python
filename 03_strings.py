# Strings
# Todo lo de Strin vimos en el curso 02, ahora vemos algunas caracteristicas más:

string_con_saltodelinea = "Este es un strin con\nsalto de linea"
string_con_tabulacion = "\tEste es un strin con tabulación"

print(string_con_saltodelinea)
print(string_con_tabulacion)

# Formateo:
apodo = "Rod"
mi_nombre = "Rodrigo"
mi_apodo = "%sri" % (apodo)
mi_surname = "Nascimento"
mi_age = 43

# 1 - Con el metodo "format" de un string
print(
    "Con las strings puedo incluir las variables de acuerdo con el format: ",
    "Mi nombre es {}, de apellido {} y tengo {} años.\nPero me dicen {}".format(
        mi_nombre, mi_surname, mi_age, mi_apodo
    ),
)

# 2 - Con el operador %: en el caso ya digo si un integer se convierte a string con %s mas alla que sea Integer
print(
    "Con las strings puedo incluir las variables con el operador %: ",
    "Mi nombre es %s, de apellido %s y tengo %d años.\nPero me dicen %s"
    % (mi_nombre, mi_surname, mi_age, mi_apodo),
)

# 3 - Por inferencia de datos, operador f:
print(
    "Con las strings puedo incluir las variables con la f: ",
    f"Mi nombre es {mi_nombre}, de apellido {mi_surname} y tengo {mi_age} años.\nPero me dicen {mi_apodo}",
)

# Desenpaquetados de caracteres:

a, b, c, d, e, f = "Python"

language = "Python"

print(a, c, f)
print(
    language[1:4]
)  # yth - toma los valores del 1 al 3 (no cuenta el 4) - es un slice
print(
    language[1:]
)  # ython - toma los valores del 1 al final - es un slice
print(language[-3])  # h - toma los valores del final -3 - es un slice
print(language[::-1])  # nohtyP - Hace al reves
print(language[0:6:2])  # No entendi

# Funciones - Metodos:
print(language.capitalize())  # Python
print(language.upper())  # PYTHON
print(language.lower())  # python
print(language.count("o"))  # 1
print("1".isnumeric())  # True
print(language.isnumeric())  # False
