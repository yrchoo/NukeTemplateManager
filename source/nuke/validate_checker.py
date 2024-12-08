"""
This runs before saving Nuke Template Script.
"""

try:
    import nuke
    from PySide2 import QtWidgets, QtGui
    from PySide2.QtCore import Qt
except Exception:
    from PySide6 import QtWidgets, QtGui, Qt  # to check UI outside of Nuke


class ValidateChecker(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__()
        self._setup_ui()
        self.run_validate()


    def _setup_ui(self):
        self.setWindowTitle("Template Validate Checker")
        self.setMinimumSize(700, 1000)
        self._create_widget()
        self._set_layout()


    def _create_widget(self):
        self.label_show = QtWidgets.QLabel()
        self.label_shot = QtWidgets.QLabel()
        self.label_file = QtWidgets.QLabel()
        self.label_path = QtWidgets.QLabel()
        self.label_user = QtWidgets.QLabel()

        self.plain_text = QtWidgets.QPlainTextEdit()
        self.plain_text.setReadOnly(True)
        self.plain_text.setFont(QtGui.QFont("Courier New"))

        self.btn_close = QtWidgets.QPushButton("Close")
        self.btn_close.setEnabled(False)
        self.btn_close.clicked.connect(self.close)


    def _set_layout(self):
        layout_main = QtWidgets.QVBoxLayout()
        layout_form = QtWidgets.QFormLayout()

        layout_form.addRow("Show : ", self.label_show)
        layout_form.addRow("Shot : ", self.label_shot)
        layout_form.addRow("File Name : ", self.label_file)
        layout_form.addRow("File Path : ", self.label_path)
        layout_form.addRow("Created By : ", self.label_user)
        layout_main.addLayout(layout_form)

        layout_main.addWidget(self.plain_text)

        layout_main.addWidget(self.btn_close, alignment=Qt.AlignRight)

        self.setLayout(layout_main)

    def _set_data(self):
        pass

    def run_validate(self):
        self.print_string("Running template valid checker...")

        validate_list = [
            self.check_read_node,
            self.check_write_node,
            self.check_require_node,
            self.check_disconnected_node,
            self.check_color,
        ]

        success = bool()
        for idx, check in enumerate(validate_list):
            self.print_string(f"Checking validation ({idx}/{len(validate_list)}) :")
            success = check()
            if not success:
                break

        self.print_string("Finishing checking...")
        self.print_result_message(success)


    def check_read_node(self):
        self.print_string("Checking read node validation... :", 1)

        error_msg = list()
        read_nodes = nuke.allNodes("Read")
        if not read_nodes:
            error_msg.append("There is no Read node in script.")
        elif len(read_nodes) > 1:
            error_msg.append("There's so many Read nodes in script.")
            error_msg.append("Only ONE Read node could be accepted for template.")
            error_msg.append(f"Now found : {len(read_nodes) + 1} : {read_nodes}")
        else:
            self.print_string(f"One Read node is founded : {read_nodes[0].name}")

        if error_msg:
            self.print_string("Validate error occurred :", 2)
            for msg in error_msg:
                self.print_string(msg, 3)
            return False
        self.print_string("Success checking Read node validation!")
        return True

    def check_write_node(self):
        return True

    def check_require_node(self):
        return True

    def check_disconnected_node(self):
        return True

    def check_color(self):
        return True

    def print_string(self, msg, indent=0):
        msg = "  " * indent + msg
        self.plain_text.appendPlainText(msg)

    def print_result_message(self, res):
        self.print_string("")
        if res:
            # TODO: Add saving template function here!!!!!!
            self.print_string("Template saved successfully!!")
        else:
            self.print_string("Template saved failed caused by validate error.")
            self.print_string("Check script and try again...")

        self.btn_close.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    win = ValidateChecker()
    app.exec()
    win.exec_()