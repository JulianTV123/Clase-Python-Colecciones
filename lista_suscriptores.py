print('*** Lista de Suscriptores ***')

suscriptores = set()

numero_suscriptores = int(input('Proporciona el numero de suscriptores iniciales: '))
for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))

#suscriptores = {'luisa@mail.com', 'marcos@mail.com', 'elena@mail.com'}
print(f'Lista de suscriptores inicial: {suscriptores}')

# Verifica si un nuevo suscriptor ya está en la lista
nuevo_suscriptor = input('Proporciona el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya está en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista {nuevo_suscriptor}')
print(f'Lista de suscriptores: {suscriptores}')

# Eliminamos un suscriptor
suscriptor_eliminar = input('Proporciona el suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista')
print(f'Lista de suscriptores: {suscriptores}')

# Verificamos la cantidad total de suscriptores
print(f'Cantidad total suscriptores: {len(suscriptores)}')

# Mostramos todos los suscriptores
print(f'--- Lista de Suscriptores ---')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')