import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QFont
import subprocess

class SimpleGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("Sign Language Detection and Speech Recongnition", self)
        title_font = QFont("Algerian", 20, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        image_label = QLabel(self)
        pixmap = QPixmap(r"C:\Users\MAAZ ALI BAIG\sign-language-and-speech-recognition-mab\asl.jpg")

        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

        load_image_btn = QPushButton('Alphabet Prediction', self)
        load_image_btn.clicked.connect(self.run_x_py)
        load_image_btn.setStyleSheet("color: white; background-color: #00aa5a;")
        layout.addWidget(load_image_btn)

        live_prediction_btn = QPushButton('Words Prediction', self)
        live_prediction_btn.clicked.connect(self.run_y_py)
        live_prediction_btn.setStyleSheet("color: white; background-color: #008547;")
        layout.addWidget(live_prediction_btn)

        self.central_widget.setLayout(layout)

    def run_x_py(self):
        try:
            subprocess.run(["python","C:\\Users\\MAAZ ALI BAIG\\sign-language-and-speech-recognition-mab\\inference_classifier_alphabets.py"],check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running x.py: {e}")

    def run_y_py(self):
        try:
            subprocess.run(["python","C:\\Users\\MAAZ ALI BAIG\\sign-language-and-speech-recognition-mab\\inference_classifier_words.py"],check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running y.py: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleGUI()
    window.show()
    sys.exit(app.exec_())
