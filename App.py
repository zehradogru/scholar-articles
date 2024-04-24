import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QCheckBox
from ScholarArticlesApp import ScholarArticlesApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScholarArticlesApp()
    window.show()
    sys.exit(app.exec_())
