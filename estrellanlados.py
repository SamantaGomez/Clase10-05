numeroLados=int(imput("ingrsar numero impar"))
import turtle
t=turtle
t=turtle.Pen()
angulo=(360/numeroLados+180)+2
def estimpar(size):
	for i in range(1,numeroLados+1):
		t.forward(300)
		t.left(size)

t.reset()
estrella(angulo)
turtle._getscreen().root.mainloop()

		
		
