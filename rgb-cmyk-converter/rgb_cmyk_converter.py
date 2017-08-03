import sys

from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel,
                             QLineEdit, QMainWindow, QTextEdit, QWidget)


# Source learning:
# http://zetcode.com/gui/pyqt5/widgets2/
# http://zetcode.com/gui/pyqt5/layout/
# https://stackoverflow.com/questions/17989231/how-to-add-buttons-to-a-main-window-in-qt

class Converter(QMainWindow):

    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        self.resize(500, 150)
        self.move(300, 300)
        self.setWindowTitle('Simple')

        widget = QWidget()
        gridLayout = QGridLayout(widget)

        redLabel = QLabel('Red')
        greenLabel = QLabel('Green')
        blueLabel = QLabel('Blue')

        self.redLineEdit = QLineEdit('0')
        self.greenLineEdit = QLineEdit('0')
        self.blueLineEdit = QLineEdit('0')

        cyanLabel = QLabel('Cyan')
        magentaLabel = QLabel('Magenta')
        yellowLabel = QLabel('Yellow')
        blackLabel = QLabel('Black')

        self.cyanLineEdit = QLineEdit('0')
        self.magentaLineEdit = QLineEdit('0')
        self.yellowLineEdit = QLineEdit('0')
        self.blackLineEdit = QLineEdit('0')

        gridLayout.addWidget(redLabel, 1, 1)
        gridLayout.addWidget(greenLabel, 2, 1)
        gridLayout.addWidget(blueLabel, 3, 1)
        gridLayout.addWidget(self.redLineEdit, 1, 2)
        gridLayout.addWidget(self.greenLineEdit, 2, 2)
        gridLayout.addWidget(self.blueLineEdit, 3, 2)

        gridLayout.addWidget(cyanLabel, 1, 3)
        gridLayout.addWidget(magentaLabel, 2, 3)
        gridLayout.addWidget(yellowLabel, 3, 3)
        gridLayout.addWidget(blackLabel, 4, 3)
        gridLayout.addWidget(self.cyanLineEdit, 1, 4)
        gridLayout.addWidget(self.magentaLineEdit, 2, 4)
        gridLayout.addWidget(self.yellowLineEdit, 3, 4)
        gridLayout.addWidget(self.blackLineEdit, 4, 4)

        self.bind_events()

        widget.setLayout(gridLayout)
        self.setCentralWidget(widget)

        self.show()

    def bind_events(self):
        self.redLineEdit.textChanged[str].connect(self.rgb_to_cmyk)
        self.greenLineEdit.textChanged[str].connect(self.rgb_to_cmyk)
        self.blueLineEdit.textChanged[str].connect(self.rgb_to_cmyk)

    # This calculation from http://www.rapidtables.com/convert/color/rgb-to-cmyk.htm
    def rgb_to_cmyk(self, text):
        red = self.get_color('red')
        green = self.get_color('green')
        blue = self.get_color('blue')
        self.set_rgb(red, green, blue)

        inverse_red = self.inverse_rgb(red)
        inverse_green = self.inverse_rgb(green)
        inverse_blue = self.inverse_rgb(blue)

        black = 1 - max(inverse_red, inverse_green, inverse_blue)

        try:
            cyan = (1 - inverse_red - black) / (1 - black)
            magenta = (1 - inverse_green - black) / (1 - black)
            yellow = (1 - inverse_blue - black) / (1 - black)
        except ZeroDivisionError:
            cyan = 0
            magenta = 0
            yellow = 0

        self.set_cmyk(cyan, magenta, yellow, black)

    def set_rgb(self, red, green, blue):
        self.redLineEdit.setText(str(int(red)))
        self.greenLineEdit.setText(str(int(green)))
        self.blueLineEdit.setText(str(int(blue)))

    def set_cmyk(self, cyan, magenta, yellow, black):
        self.cyanLineEdit.setText(str(round(cyan, 3)))
        self.magentaLineEdit.setText(str(round(magenta, 3)))
        self.yellowLineEdit.setText(str(round(yellow, 3)))
        self.blackLineEdit.setText(str(round(black, 3)))


    def get_color(self, color):
        qLineEditText = 'self.{color}LineEdit.text()'.format(color=color)
        return int(eval(qLineEditText)) if self.valid_rgb_color(eval(qLineEditText)) else 0

    def valid_rgb_color(self, color_value):
        return color_value.isdigit() and int(color_value) >= 0 and int(color_value) <= 255

    def inverse_rgb(self, rgb):
        return rgb / 255


if __name__ == '__main__':
    app = QApplication([])
    converter = Converter()
    sys.exit(app.exec_())
