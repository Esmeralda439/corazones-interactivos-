import turtle
import random

# Configuración de la pantalla
ventana = turtle.Screen()
ventana.title("¡Corazones instantáneos!")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)

# Desactivamos la animación paso a paso para que sea instantáneo
ventana.tracer(0)

colores = ["#FF3366", "#FF3399", "#FF0055", "#FF66B2", "#E60073", "#FF1A75", "#FF0000"]

def crear_corazon(x, y):
    corazon = turtle.Turtle()
    corazon.hideturtle()
    corazon.speed(0)
    corazon.penup()
    
    # Tamaño aleatorio para variar
    escala = random.uniform(0.6, 1.5)
    
    # Ajustamos la posición según el tamaño para que quede centrado al clic
    corazon.goto(x, y - (15 * escala))
    corazon.pendown()
    
    color_aleatorio = random.choice(colores)
    corazon.color(color_aleatorio)
    corazon.begin_fill()
    
    # Dibujar el corazón (multiplicado por la escala para variar tamaños)
    corazon.left(140)
    corazon.forward(40 * escala)
    
    for _ in range(200):
        corazon.right(1)
        corazon.forward(0.3 * escala)
        
    corazon.left(120)
    
    for _ in range(200):
        corazon.right(1)
        corazon.forward(0.3 * escala)
        
    corazon.forward(40 * escala)
    corazon.end_fill()
    
    # ¡Aquí está la magia! Forzamos a la pantalla a mostrar el dibujo YA terminado
    ventana.update()

# Escuchar los clics
ventana.onclick(crear_corazon)
ventana.listen()

# Primera actualización para renderizar la ventana vacía
ventana.update()
ventana.mainloop()
