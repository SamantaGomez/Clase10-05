def crear():
  archi=open("matriz.txt","w")
  archi.close()
def llenar():
  archi=open("matriz.txt","a")
  archi.write(y)
  archi.close()

f1=[0,0,0]
f2=[0,0,0]
f3=[0,0,0]
f4=[0,0,0]
f5=[0,0,0]
matriz=[f1,f2,f3,f4,f5]
t1=[0,0,0,0,0]
t2=[0,0,0,0,0]
t3=[0,0,0,0,0]
matrizt=[t1,t2,t3]

f1[0]=int(input("Llene la matriz => ")) 
f1[1]=int(input("Llene la matriz => "))
f1[2]=int(input("Llene la matriz => ")) 

f2[0]=int(input("Llene la matriz => ")) 
f2[1]=int(input("Llene la matriz => "))
f2[2]=int(input("Llene la matriz => ")) 

f3[0]=int(input("Llene la matriz => ")) 
f3[1]=int(input("Llene la matriz => "))
f3[2]=int(input("Llene la matriz => ")) 

f4[0]=int(input("Llene la matriz => ")) 
f4[1]=int(input("Llene la matriz => "))
f4[2]=int(input("Llene la matriz => ")) 

f5[0]=int(input("Llene la matriz => ")) 
f5[1]=int(input("Llene la matriz => "))
f5[2]=int(input("Llene la matriz => ")) 

t1[0]=f1[0]
t1[1]=f2[0]
t1[2]=f3[0]
t1[3]=f4[0]
t1[4]=f5[0]

t2[0]=f1[1]
t2[1]=f2[1]
t2[2]=f3[1]
t2[3]=f4[1]
t2[4]=f5[1]

t3[0]=f1[2]
t3[1]=f2[2]
t3[2]=f3[2]
t3[3]=f4[2]
t3[4]=f5[2]


print (" ")
print ("La matriz original (5x3) es: ")
print (matriz)
print (" ")
print ("La matriz transpuesta (3x5) es: ")
print (matrizt)
crear()
llenar()