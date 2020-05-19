"""valor = str(input("Coloca cualquier cosa: "))
print(valor)

valor_D = float(input('Un numero entero o decimal: '))
print(valor_D)

valor_I = int(input('Un numero entero o decimal: '))
print(valor_I)
"""
"""
tiempo para hacerlo 5 a 10 minutos

ejercicio, hacer un pequeño formulario que solicite los siguientes datos
            nombre
            edad
            fecha de nacimiento
            telefono
            dias que trabajo 
            salario
            *** el nombre y la fecha debe ser de tipo cadena
            *** hacer una multipicacion entre los dias que trabajo y el salario
            *** el salario puede ser decimal o entero
            ejem 10 *200 = 2000
           

"""

nombre = str(input("Cual es tu nombre: "))

edad = int(input("Edad: "))

fec_nac = str(input("Fecha de nacimiento: "))

telefono = int(input("Numero telefonico: "))

dias_trabajo = int(input("Dias que trabajo? "))

salario = float(input("Cuanto gana por dia: "))
salario_total = dias_trabajo * salario

print("Su salario en total es: "+str(salario_total))