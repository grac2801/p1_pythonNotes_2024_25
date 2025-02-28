import turtle

pat=turtle.Turtle()

pat.shape("turtle")
for i in range(6):
    pat.circle(80, 60)
    pat.stamp()
  
pat.penup()
pat.right(90)
pat.fd(100)
pat.right(90)

pat.pendown()
shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']

for j in range(len(shapes)):
    pat.shape(shapes[j])
    pat.circle(80, 60)
    pat.stamp()



turtle.mainloop()
