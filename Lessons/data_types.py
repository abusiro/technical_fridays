'''
Esto es un comentario
de varias líneas
'''

# esto es un comentario de una línea

# ######################################
# STRINGS
simple_string = 'hola'
print('simple string:', simple_string)

multiline_string = '''
hola,
mundo'''
print('\n', 'multiline_string:', multiline_string)

string_special = '\nhola,\nmundo'
print('\nstring_special:', string_special)

raw_string_special = r'hola,\nmundo'
print('\nraw_string:', string_special)

print('es equivalente introducir un caracter especial mediante teclado o mediante un caracter escapado?:\n', multiline_string==string_special)

# strings son iterables y se puede hacer subsetting y slicing
string = 'hola'
print('subsetting de un iterable: ', string[2])

print('slicing de un iterable: ', string[1:3])


##################
# NUMBERS
entero = 1

flotante = 1.1

suma = entero + flotante
print(suma)

print('la suma de un int y un float es un :', type(suma))

# numeros admiten  todas las operaciones aritméticas básicas
suma = suma + 1
suma += 1
print(suma)

producto = entero * flotante
division = entero / flotante
division_entera = entero // flotante
modulo = entero % flotante
potencia = entero ** flotante
print('producto:', producto)
print('division:', division)
print('division entera:', division_entera)
print('modulo:', modulo)
print('potencia:', potencia)

##################################
# iterables en python
# LISTAS
iterable = [1, 2, 3]
print('iterable:', iterable)
# las listas son iterables con subsetting y slicing
# operaciones con listas
ampliacion = iterable + [6, 7, 8]
print('ampliacion:', ampliacion)
ampliacion  = ampliacion * 2
print('ampliacion:', ampliacion)
# operaciones con strings
string = 'hola'
ampliacion = string + ' mundo'
# built-ins de listas
print('len:', len(ampliacion))
print('max:', max(iterable))
print('sum:', sum(iterable))

iterable.append(4)
print('iterable con append:', iterable)
iterable.append([5, 6, 7])
print('iterable admite todo tipo de elementos:', iterable)
iterable.remove(2)
print('iterable con remove:', iterable)


# dictionaries, sirven para almacenar key value pairs
dicc = {'a': 1, 'b': 2, 'c': 3}
keys = dicc.keys()
values = dicc.values()
print('tipo de datos de .keys(): ', type(keys))

# dict_keys es un iterable, pero no es subsettable y no se puede hacer slicing
keys[0]
keys_list = list(keys)
keys_list[0]

# diccionarios son mutables
dicc['a'] = 2
print('diccionario con cambio de valor:', dicc)
# diccionarios son expandables
dicc['d'] = 4
dicc.update({'e': 5})
print('diccionario con update:', dicc)

# para acceder a un valor de un diccionario
print('valor de a:', dicc['a'])

# Tuples are like lists, except they cannot be modified once created:
t = 12345, 54321, 'hello!'
print('t:', t)
print(t[0])
t[1] = 33
# tambien se pueden crear con el built-in tuple()
tuple([1, 2, 3])

# algunas tuples son un poco tricky de inicializar
empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)

len(singleton)


# las tuples tienen packing
x, y, z = t
print('x:', x)
# y los packing tienen sus unpacking
print(*t)

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
print('u:', u)

# Tuples are immutable:
t[0] = 88888


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v[0][2] = 6
print('v:', v)

# ###############################################
# loops for
iterable = [1, 2, 3]
for i in iterable:
    print(i)

for i in range(10):
    print(i)

# enumerate
iterable = [1, 2, 3]
for index, value in enumerate(iterable):
    print(index, value)

# añadimos if statements a un loop for con un f string
iterable = [1, 2, 3]
for i, element in enumerate(iterable):
    if element == 2:
        print(f'elemento {i} es igual a 2')
    else:
        print(f'elemento {i} no es igual a 2')

# la forma pythonica de hacer loops es mediante COMPREHENSION
iterable = [1, 2, 3]
list_comprehension = [i**2 for i in iterable]
dict_comprehension = {i: i**2 for i in iterable}
tuple_comprehension = tuple(i**2 for i in iterable)
generator = (i**2 for i in iterable)
tuple_comprehension == generator








