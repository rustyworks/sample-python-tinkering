from turtle import *


class Fractal():

    def __init__(self):
        shape('turtle')
        speed(5)
        color('blue', 'turquoise')

    def draw(self):
        begin_fill()
        sharp_counter = 1
        dull_counter = 0
        is_dull = False

        while True:
            if is_dull:
                dull_counter += 1
                if dull_counter == 3:
                    is_dull = False
                    dull_counter = 0
                self.dull()
            else:
                self.sharp()
                self.dull()
                if sharp_counter == 3:
                    is_dull = True
                    sharp_counter = 0
                sharp_counter += 1
            if abs(pos()) < 1:
                break

        end_fill()
        done()

    def sharp(self):
        forward(25)
        left(135)

    def dull(self):
        forward(25)
        right(60)


if __name__ == '__main__':
    fractal = Fractal()
    fractal.draw()
