import sys
from PyQt5.QtWidgets import QWidget
from Vistas.V2 import ventanaTuplas2
from PyQt5.QtWidgets import QApplication


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.gui = ventanaTuplas2()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
