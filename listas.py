### Listas: ###

my_first_list = list("23fds")  # ['2', '3', 'f', 'd', 's']

print(my_first_list)

my_list: list = [3, "45", "Rodrigo"]  # Es parecido con un array, pero tiene funciones mas inteligentes y tiene mas cosas

print(my_list)

# Las listas, como los array en JS, tiene un length de 0 o sea [], y un indice empezando de 0
# Que es el primer elemento.
print("len(my_list): ", len(my_list))

print("my_list[2]: ", my_list[2])  # Rodrigo -> Acceder a un elemento de la lista por el indice
print("my_list[-2]: ", my_list[-2])  # "45" -> Acceder a un elemento de la lista por el indice negativo, del final al comienzo

leng = len(my_list)
my_last_element = my_list[leng - 1]  # Es lo mismo de:
my_last_element = my_list[-1]

print(my_last_element)  # Rodrigo

# Count:
print("my_list.count('45'): ", my_list.count("45"))  # 1 - numero de ocurrencias de un valor

street, number, location, city = ["Jose c Paz", 1870, "San Andres", "San Martin"]
street, number, location, city = "Jose c Paz", 1870, "San Andres", "San Martin"

print(number)  # 1870

# Concatenar listas con operador +
print(my_first_list + my_list)  # ['2', '3', 'f', 'd', 's', 3, '45', 'Rodrigo']
# print(my_first_list + "35")  # TypeError: can only concatenate list (not "int") to list

# Agregar elementos con append:
my_first_list.append("Rodrigo Madeira!")
print(my_first_list)  # ['2', '3', 'f', 'd', 's', 'Rodrigo Madeira!']

# insert:
my_first_list.insert(3, "Rodrigo Madeira!")
print(my_first_list)  # ['2', '3','f', 'Rodrigo Madeira!', 'd', 's', 'Rodrigo Madeira!']

# remove:
my_first_list.remove("Rodrigo Madeira!")
print(my_first_list)  # ['2', '3','f', 'd', 's', 'Rodrigo Madeira!'] -> Sol oremueve el primer valor igual

# pop:
print(my_first_list.pop())  # 'Rodrigo Madeira!'-> Remueve el ultimo elemento por defecto. Devuelve el elemento eliminado
print(my_first_list)  # ['2', '3','f', 'd', 's' ] -> Remueve el ultimo elemento por defecto.

# del:
del my_first_list[2]
print(my_first_list)  # ['2', '3', 'd', 's'] -> Elimina de la lista sin retornar nada

# clear:
my_first_list.clear()
print(my_first_list)  # []

# clear:
my_new_list = my_list.copy()
my_list.clear()
print(my_list)  # []
print(my_new_list)  # [3, '45', 'Rodrigo'] -> Crea una nueva referencia

# Sublistas:

print(my_new_list[1:3])  # ['45', 'Rodrigo']

# reverse:
# le da vuelta a una lista
