#Asignar valor a la gravedad de cada Planeta, estrella o satélite.
GRAVEDADES = {
    "Tierra": 9.81 ,
    "Marte": 3.71 ,
    "Sol": 274 ,
    "Luna": 1.62 ,
    "Mercurio": 3.7 ,
    "Venus": 8.87 ,
    "Jupiter":24.79 ,
    "Saturno": 10.44 ,
    "Urano": 8.87 ,
    "Neptuno": 11.15 ,
    "Pluton": 0.62 ,
}
# Vamos a preguntar al tio en que planeta, estrella o satelite tiene su movil
ASTRO = input("¿En que astro estás? : ").capitalize()
GRAVITY = GRAVEDADES[ASTRO]

# Preguntamos a que altura se situa el movil
Altura_inicial = float(input("Altura a la que se encuentra el movil.(En metros): "))
#preguntamos por el tiempo de caída del movil
Tiempo = float(input("¿Cuanto tiempo se encuentra callendo el movil? (En segundos): "))
# Preguntamos por la velocidad a la que se lanza el objeto o si se deja caer
Velocidad0 = float(input("Velocidad inicial a la que se lanza el movil verticalmente: "))
"""
Vamos a codificar la fórmula para que opere con los datos que hemos pedido anteriormente


y= posición final (m)
y0= posición inicial del movil (m)
v0= velocidad inicial del movil (m/s)
t = tiempo (segundos)
g = aceleración de la gravedad (m/s^2)

y= y0+(v0*t)-(0,5*g*t**2)

"""
# convertimos la función a python
Altura_actual = Altura_inicial + (Velocidad0 * Tiempo)- ( 0.5 * GRAVITY * Tiempo**2)

# Convertimos los datos dados pasando por la formula en un resultado
if Altura_actual <=0:
    print("El movil sas estampao to duro con el suelo")
else:
    print(f"La altura en el segundo {Tiempo} es {Altura_actual}")
