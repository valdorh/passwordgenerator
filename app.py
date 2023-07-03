import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtGui import QCloseEvent

import buttons
import password
from mainUI.main import Ui_MainWindow


class PasswordGenerator(QMainWindow):
    def __init__(self):
        super(PasswordGenerator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connect_slider_to_spinbox()
        self.set_password()
        self.do_when_password_edit()

        for btn in buttons.GENERATE_PASSWORD:
            getattr(self.ui, btn).clicked.connect(self.set_password)

        self.ui.pushButton_3.clicked.connect(self.change_password_visibility)
        self.ui.btn_copy.clicked.connect(self.copy_to_clipboard)

    def connect_slider_to_spinbox(self) -> None:
        self.ui.sld_length.valueChanged.connect(self.ui.spinbox_length.setValue)
        self.ui.spinbox_length.valueChanged.connect(self.ui.sld_length.setValue)

        self.ui.spinbox_length.valueChanged.connect(self.set_password)

    def get_characters(self) -> str:
        chars = ""

        for btn in buttons.Characters:
            if getattr(self.ui, btn.name).isChecked():
                chars += btn.value

        return chars

    def set_password(self):
        try:
            self.ui.ln_password.setText(
                password.create_new(
                    length=self.ui.sld_length.value(),
                    characters=self.get_characters())
            )
        except IndexError:
            self.ui.ln_password.clear()

        self.set_entropy()
        self.set_strength()

    def get_character_number(self) -> int:
        num = 0

        for btn in buttons.CHARACTER_NUMBER.items():
            if getattr(self.ui, btn[0]).isChecked():
                num += btn[1]

        return num

    def set_entropy(self) -> None:
        length = len(self.ui.ln_password.text())
        char_num = self.get_character_number()

        self.ui.lb_entropy.setText(
            f"Entropy: {password.get_entropy(length, char_num)}"
        )

    def set_strength(self) -> None:
        length = len(self.ui.ln_password.text())
        char_num = self.get_character_number()

        for strength in password.StrengthToEntropy:
            if password.get_entropy(length, char_num) >= strength.value:
                self.ui.lb_strenght.setText(
                    f"Strength: {strength.name}")

    def change_password_visibility(self) -> None:
        if self.ui.pushButton_3.isChecked():
            self.ui.ln_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.ln_password.setEchoMode(QLineEdit.Password)

    def copy_to_clipboard(self) -> None:
        QApplication.clipboard().setText(self.ui.ln_password.text())

    def closeEvent(self, event: QCloseEvent) -> None:
        QApplication.clipboard().clear()

    def do_when_password_edit(self) -> None:
        self.ui.ln_password.textEdited.connect(self.set_entropy)
        self.ui.ln_password.textEdited.connect(self.set_strength)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PasswordGenerator()
    window.show()

    sys.exit(app.exec())
