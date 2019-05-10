import sys
def crear():
  archi=open("volumen.txt","w")
  archi.close()
def llenar():
  archi=open("volumen.txt","a")
  archi.write(v)
  archi.close()

def menu():
  print("1 = Calcular volumen de un cubo")
  print("2 = Calcular volumen de un cilindro")
  print("3 = Calcular volumen de una esfera")
  print("4 = Salir")

def opcion():
  print ("Presione 1 para continuar ")
  print ("Presione 0 para salir")
  
  
def cubo():
  a=int(input("Ingrese el alto del cubo => "))
  b=int(input("Ingrese el ancho del cubo => "))
  c=int(input("Ingrese el largo del cubo => "))
  volumen=a*b*c
  print("El volumen del cubo es: ")
  print(volumen)

def cilindro():
  r1=int(input("Ingrese el radio del cilindro => "))
  h=int(input("Ingrese la altura del cilindro => "))
  volumen2=((3.14)*(r1*r1)*(h))
  print("El volumen del cilindro es: ")
  print(volumen2)

def esfera():
  r2=int(input("Ingrese el radio de la esfera => "))
  volumen3=(4/3)*(3.14)*(r2*r2*r2)
  print("El volumen de la esfera es: ")
  print(volumen3)

def todo():
  v=" "
  x=int(input(" "))
  if x==1:
    menu()
    t=int(input(" "))
    if t==1:
      cubo()
      opcion()
      todo()
      v=volumen
      llenar()

    elif t==2:
      cilindro()
      opcion()
      todo()
      v=volumen2
      llenar()
    elif t==3:
      esfera()
      opcion()
      todo()
      v=volumen3
      llenar()
  elif x==0:
    sys.exit(0)
  else:
    print("Opcion incorrecta")
    todo()

print("Bienvenido")
opcion()
crear()
todo()

