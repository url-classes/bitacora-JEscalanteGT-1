from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from color_widget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Layouts')

        layout = QVBoxLayout()
        layout.addWidget(
            ColorWidget('red')
        )
        layout.addWidget(
            ColorWidget('yellow')
        )
        layout.addWidget(
            ColorWidget('green')
        )

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

