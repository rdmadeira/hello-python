# Variables & Funciones Intrínsecas: 

first_name = 'Rodrigo'
last_name = 'Nascimento'
isStudent = True
age = 43
print(first_name, last_name, isStudent, age)

# Transformar Int a String, llamamos a la funcion builted-in: 
age_to_str = str(age)
print(type(age_to_str), age_to_str )

# Un Prompt:
first_name = input('Enter your nombre: ')

print(first_name)

# Transformar En entero: ll
print(int(2.8))   # 2
# print(int('2.8'))   # ValueError: invalid literal for int() with base 10: '2.8'

# Round - arredondear: 
print(round(2.51)) # 3

# Length:
print(len(first_name), len(age_to_str))
# print(len(3.5)) TypeError: object of type 'float' has no len()

# Variables en una sola linea de codigo: 

first_name, last_name, age, isStudent = "Rodrigo_de_vuelta", "Madeira", str(42), True # Las variables pueden cambiar de valor
age = int(input('Cual la edad que queris tener? '))
my_first_list = [first_name, last_name, age, isStudent]

print(my_first_list, last_name)

"""
Python no tiene un tipado FUERTE, o sea, podes pisar el valor de las variables y el tipo también!! 
Para aclarar eso, tenemos que incluir el tipado, como en Typescript. Pero eso no impide tampoco de 
cambiar el tipo de valor de la variable. Es un tipado Debil:
"""

age: str = str(35)
print(type(age)) # 'str'
age = 35 
print(type(age)) # 'int'


# 1h35min53seg