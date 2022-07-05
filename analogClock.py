import turtle
import datetime


class Clock:
    tool_name = 'Cody Buddy'

    def __init__(self, title='Cody Buddy',
                 time_deltas=(0, 0, 0)):
        turtle.title(title)
        self.time_deltas = time_deltas

    @staticmethod
    def move(distance):
        turtle.penup()
        turtle.forward(distance)
        turtle.pendown()

    def createhand(self, name, length):
        turtle.reset()
        self.move(-length * 0.01)
        turtle.begin_poly()
        turtle.forward(length * 1.01)
        turtle.end_poly()
        hand = turtle.get_poly()
        turtle.register_shape(name, hand)

    def createClock(self, radius):
        turtle.reset()
        turtle.pensize(7)
        for i in range(60):
            self.move(radius)
            if i % 5 == 0:
                turtle.forward(20)
                self.move(-radius - 20)
            else:
                turtle.dot(5)
                self.move(-radius)
            turtle.right(6)

    @staticmethod
    def getweekday(today):
        return ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri',
                'Sat', 'Sun'][today.weekday()]

    @staticmethod
    def getdate(today):
        return '%s:%s:%s' % (today.year, today.month, today.day)

    def starttick(self, second_hand, minute_hand, hour_hand, printer):
        today = datetime.datetime.today()
        second = today.second + \
                 self.time_deltas[0] + today.microsecond * 1e-6
        minute = today.minute + \
                 self.time_deltas[1] + second / 60.
        hour = (today.hour + self.time_deltas[2] + minute / 60) % 12
        second_hand.setheading(6 * second)
        minute_hand.setheading(6 * minute)
        hour_hand.setheading(30 * hour)
        turtle.tracer(False)
        printer.forward(65)
        printer.write(self.getweekday(today),
                      align='center', font=("Times New Roman", 14, "bold"))
        printer.forward(120)
        printer.write('12', align='center',
                      font=("Times New Roman", 14, "bold"))
        printer.back(250)
        printer.write(self.getdate(today), align='center',
                      font=("Times New Roman", 14, "bold"))
        printer.back(145)
        printer.write('6', align='center',
                      font=("Times New Roman", 14, "bold"))
        printer.home()
        printer.right(92.5)
        printer.forward(200)
        printer.write('3', align='center',
                      font=("Times New Roman", 14, "bold"))
        printer.left(2.5)
        printer.back(400)
        printer.write('9', align='center',
                      font=("Times New Roman", 14, "bold"))
        printer.home()
        turtle.tracer(True)

        turtle.ontimer(lambda: self.starttick(
            second_hand, minute_hand, hour_hand, printer), 100)

    def run(self):

        turtle.tracer(False)
        turtle.mode('logo')
        self.createhand('second_hand', 150)
        self.createhand('minute_hand', 140)
        self.createhand('hour_hand', 90)

        second_hand = turtle.Turtle()
        second_hand.shape('second_hand')
        minute_hand = turtle.Turtle()
        minute_hand.shape('minute_hand')
        hour_hand = turtle.Turtle()
        hour_hand.shape('hour_hand')
        for hand in [second_hand,
                     minute_hand, hour_hand]:
            hand.shapesize(1, 1, 3)
            hand.speed(0)

        printer = turtle.Turtle()
        printer.hideturtle()
        printer.penup()
        self.createClock(160)

        turtle.tracer(True)
        self.starttick(second_hand,
                       minute_hand, hour_hand, printer)
        turtle.mainloop()


clock = Clock()
clock.run()
