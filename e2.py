print ("Datos de la persona")

nombre=input("Ingrese el nombre del producto: ")
precio1=int(input("ingrese un precio: "))
nombre2=input("Ingrese el nombre del producto: ")
precio2=int(input("ingrese un precio: "))


BONIFICACION = 20
#comentario

"""
0'''
"""
compratotal = precio1+precio2
comparar= precio1>=precio2
logico=(precio1<precio2 and precio1==precio2)

#concaternar Textos

cabecera="resultados del producto {0} y del producto {1}"
print (cabecera.format(nombre,nombre2))
print("el precio del primer valor es mayor o igual al precio del segundo valor: ")
print (comparar)

print("la suma es "+str(compratotal))
print ("precio z precio2 and precio1 == precio2")
print (logico)

#operador de asignacion
preciocompratotal += BONIFICACION
print("al precio total le incrementamos su valor que tine la constante")