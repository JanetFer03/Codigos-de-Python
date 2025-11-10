# modulo arroga el residuo de la operacion %
# // division entera
# / division normal

# asigancion c=5 c+2=5+2. se puede hacer con las operaciones comunes 
# logica/comparacion igualdad (==), desigualdad(!=), <,>. 
#comparacion logica AND multipliacion , OR suma , NOT negacion (da el dato contrario). dato booleano true (p) o false (q)


input('BIENVENIDO')
x = float (input ('iNGRESA UN NUMERO:  '))
y = float (input('INGRESA UN SEGUNDO NUMERO: '))

print (f' Resultado de la suma es: ', x + y)
print (f' Resultado de la resta es: ', x - y)
print (f' Resultado de la multipliacion es: ', x * y)
print (f' Resultado de la divion es: ', x / y)
print (f'Resultado de modulo es: ', x % y)
print (f' Resultado de la potencia es: ', x ** y)

print('\n\n AHORA HAREMOS OTRAS OPERACIONES \n\n')
z = float(input('iNGRESA UN NUMERO: '))
w = float (input('INGRESA UN SEGUNDO NUMERO: ' ))

z+=2
print (f' Resultado de la asignacion suma: ', z)
w-=13
print (f' Resultado de la asignacion resta es: ', w)
print (f' Resultado de la igualdad es: ', z == w)
print (f' Resultado de la desigualdad es: ', z!= w)
print (f'Resultado de mayor que es: ', z > w)
print (f' Resultado de menor que es: ', z < w)

print('\n\n TABLAS DE VERDAD \n\n')
print('\n\n AND \n\n')
k=0
l=0
print(f' {k} * {l}= {k and l} ')
k=0
l=1
print(f' {k} * {l}= {k and l} ')
k=1
l=0
print(f' {k} * {l}= {k and l} ')
k=1
l=1
print(f' {k} * {l}= {k and l} ')

print('\n\n OR \n\n')
k=0
l=0
print(f' {k} + {l}= {k or l} ')
k=0
l=1
print(f' {k} + {l}= {k or l} ')
k=1
l=0

print(f' {k} + {l}= {k or l} ')
k=1
l=1
print(f' {k} + {l}= {k or l} ')

print('\n\n NOT \n\n')
k=0
print(f' ~{k} = {not k} ')
k=1
print(f' ~{k} = {not k} ')







