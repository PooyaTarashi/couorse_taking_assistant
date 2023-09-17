import sys
import pyperclip as ppc
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea, QLabel, QLineEdit, QPushButton, QHBoxLayout
from main import System, Item

class APushButton(QPushButton):
    def __init__(self, item:Item):
        super().__init__(f'{item.id} | {item.caption}')
        self.clicked.connect(lambda: ppc.copy(item.id))

class DPushButton(QPushButton):
    def __init__(self, item:Item, win):
        super().__init__('X')
        self.clicked.connect(lambda: self.func(item, win))

    def func(self, item, win):
        item.delete_from_pickle()
        win.initUI()

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 200, 1000, 600)
        self.initUI()

    def add_item(self, s:System, caption, id):
        s.add_item(caption, id)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Course Taking Assistant')
        # Create a central widget to hold the main layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a QVBoxLayout for the central widget
        main_layout = QVBoxLayout()

        # Create a QScrollArea and set its widget
        scroll_area = QScrollArea(self)
        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)

        # Create a QVBoxLayout for the scroll widget
        scroll_layout = QVBoxLayout(scroll_widget)

        # Add some content to the scroll area (e.g., labels)
        s = System()
        item_list = s.load_data()
        for item in item_list.values():
            copy_btn = APushButton(item=item)
            remove_btn = DPushButton(item=item, win=self)
            remove_btn.setFixedWidth(40)
            copy_btn.setFixedHeight(50)
            scroll_layout.addWidget(copy_btn)
            scroll_layout.addWidget(remove_btn)
            scroll_layout.addWidget(QLabel('____________________________________________'))


        # Set the scroll area widget resizable
        scroll_area.setWidgetResizable(True)

        # Add the scroll area to the main layout
        main_layout.addWidget(scroll_area)

        # Create a QHBoxLayout for the bottom row
        bottom_layout = QHBoxLayout()

        # Add two labels, two text boxes, and a button to the bottom row
        label1 = QLabel('Course ID:')
        label1.setFixedWidth(75)
        text_box1 = QLineEdit()
        text_box1.setFixedWidth(200)
        text_box1.setFixedHeight(40)
        label2 = QLabel('Course Caption:')
        text_box2 = QLineEdit()
        text_box2.setFixedWidth(500)
        text_box2.setFixedHeight(40)
        button = QPushButton('Submit')
        button.setFixedWidth(100)
        button.setFixedHeight(40)
        button.clicked.connect(lambda: self.add_item(s, text_box2.text(), text_box1.text()))

        bottom_layout.addWidget(button)
        bottom_layout.addWidget(label1)
        bottom_layout.addWidget(text_box1)
        bottom_layout.addWidget(label2)
        bottom_layout.addWidget(text_box2)

        # Add the bottom row layout to the main layout
        main_layout.addLayout(bottom_layout)

        # Set the main layout as the layout for the central widget
        central_widget.setLayout(main_layout)

    def submit_new_item(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
