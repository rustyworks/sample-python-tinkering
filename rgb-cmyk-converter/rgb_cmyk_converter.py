import sys

from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel,
                             QLineEdit, QMainWindow, QTextEdit, QWidget)


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

        self.redLineEdit = QLineEdit()
        self.greenLineEdit = QLineEdit()
        self.blueLineEdit = QLineEdit()

        cyanLabel = QLabel('Cyan')
        magentaLabel = QLabel('Magenta')
        yellowLabel = QLabel('Yellow')
        blackLabel = QLabel('Black')

        self.cyanLineEdit = QLineEdit()
        self.magentaLineEdit = QLineEdit()
        self.yellowLineEdit = QLineEdit()
        self.blackLineEdit = QLineEdit()

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

        # self.redLineEdit.textChanged[int].connect(rgb_to_cmyk)
        # self.redLineEdit.textChanged[int].connect(rgb_to_cmyk)
        # self.redLineEdit.textChanged[int].connect(rgb_to_cmyk)

        widget.setLayout(gridLayout)
        self.setCentralWidget(widget)

        self.show()

    # This calculation from http://www.rapidtables.com/convert/color/rgb-to-cmyk.htm
    def rgb_to_cmyk(self, _):
        red = self.get_red()
        green = self.get_green()
        blue = self.get_blue()

        black = 1 - max(red, green, blue)
        cyan = (1 - self.inverse_rgb(red) - black) / (1 - black)
        magenta = (1 - self.inverse_rgb(green) - black) / (1 - black)
        yellow = (1 - self.inverse_rgb(blue) - black) / (1 - black)

        self.set_cmyk(cyan, magenta, yellow, black)

    def cmyk_to_rgb(self, _):
        pass

    def set_rgb(red, green, blue):
        pass

    def set_cmyk(cyan, magenta, yellow, black):
        self.cyanLineEdit.text(cyan)
        self.magentaLineEdit.text(magenta)
        self.yellowLineEdit.text(yellow)
        self.blackLineEdit.text(black)

    # Eval this?
    def get_red():
        return int(self.redLineEdit.text()) if self.redLineEdit.text().isdigit() else 0

    def get_green():
        return int(self.greenLineEdit.text()) if self.greenLineEdit.text().isdigit() else 0

    def get_blue():
        return int(self.blueLineEdit.text()) if self.blueLineEdit.text().isdigit() else 0

    def get_red():
        return int(self.redLineEdit.text()) if self.redLineEdit.text().isdigit() else 0

    def get_green():
        return int(self.greenLineEdit.text()) if self.greenLineEdit.text().isdigit() else 0

    def get_blue():
        return int(self.blueLineEdit.text()) if self.blueLineEdit.text().isdigit() else 0

    def inverse_rgb(self, rgb):
        return rgb / 255


if __name__ == '__main__':
    app = QApplication([])
    converter = Converter()
    sys.exit(app.exec_())
