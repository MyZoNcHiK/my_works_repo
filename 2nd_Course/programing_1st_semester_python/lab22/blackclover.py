import turtle
import math

class BlackClover:
    def __init__(self, x=0, y=0, size=120):
        self.x = x
        self.y = y
        self.size = size
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.penup()
        self.pen.pencolor("black")
        self.pen.fillcolor("black")

    def draw_leaf(self, angle):
        points = []
        rotation = math.radians(angle - 90)
        offset = self.size * 0.025
        shift_x = offset * math.cos(math.radians(angle))
        shift_y = offset * math.sin(math.radians(angle))

        for i in range(201):
            t = 2 * math.pi * i / 200
            hx = 16 * math.sin(t) ** 3
            hy = (
                13 * math.cos(t)
                - 5 * math.cos(2 * t)
                - 2 * math.cos(3 * t)
                - math.cos(4 * t)
            )

            lx = hx * self.size / 32 * 0.80
            ly = (hy + 17) * self.size / 32

            px = lx * math.cos(rotation) - ly * math.sin(rotation)
            py = lx * math.sin(rotation) + ly * math.cos(rotation)

            points.append((
                self.x + px + shift_x,
                self.y + py + shift_y
            ))

        self.pen.penup()
        self.pen.goto(points[0])
        self.pen.pendown()
        self.pen.begin_fill()

        for point in points[1:]:
            self.pen.goto(point)

        self.pen.goto(points[0])
        self.pen.end_fill()
        self.pen.penup()

    def draw(self):
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.dot(self.size * 0.20, "black")

        for angle in [90, 18, -54, -126, 162]:
            self.draw_leaf(angle)


clover1 = BlackClover(-220, 0, 75)
clover2 = BlackClover(0, 0, 125)
clover3 = BlackClover(220, 0, 80)

clover1.draw()
clover2.draw()
clover3.draw()

turtle.done()
