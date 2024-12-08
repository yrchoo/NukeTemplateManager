
try:
    from PySide2 import QtWidgets
except:
    from PySide6 import QtWidgets

import validate_checker

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class TemplateManager(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("Template Manager")
        self.setMinimumSize(500, 700)
        self._create_widget()
        self._set_layout()
        self._set_event()


    def _create_widget(self):
        self.edit_path = QtWidgets.QLineEdit()
        self.edit_show = QtWidgets.QLineEdit()
        self.edit_shot = QtWidgets.QLineEdit()
        self.edit_name = QtWidgets.QLineEdit()
        self.spin_version = QtWidgets.QSpinBox()
        self.label_path = QtWidgets.QLabel()

        self.push_save = QtWidgets.QPushButton("Save")
        self.push_cancel = QtWidgets.QPushButton("Cancel")
        self.push_file = QtWidgets.QPushButton("...")
        self.push_file.setMaximumSize(20, 100)


    def _set_layout(self):
        layout_main = QtWidgets.QVBoxLayout()
        layout_form = QtWidgets.QFormLayout()
        layout_file = QtWidgets.QHBoxLayout()
        layout_btn = QtWidgets.QHBoxLayout()

        layout_file.addWidget(self.edit_path)
        layout_file.addWidget(self.push_file)

        layout_form.addRow("Work Directory : ", layout_file)
        layout_form.addRow("Show : ", self.edit_show)
        layout_form.addRow("Shot : ", self.edit_shot)
        layout_form.addRow("Template Name : ", self.edit_name)
        layout_form.addRow("Template Version : ", self.spin_version)
        layout_form.addRow("Output Path : ", self.label_path)

        layout_btn.addWidget(self.push_save)
        layout_btn.addWidget(self.push_cancel)

        layout_main.addLayout(layout_form)
        layout_main.addLayout(layout_btn)

        self.setLayout(layout_main)

    def _set_event(self):
        self.push_save.clicked.connect(self.save_template)
        self.push_cancel.clicked.connect(self.close)
        self.push_file.clicked.connect(self.pop_file_dialog)

    def _set_data(self):
        # TODO: Get data from setting.yaml & get proper version data
        pass

    def close(self):
        # TODO: Add write personal setting data here!!!!
        super().close()

    def save_template(self):
        # TODO: Get data from widget & save template!!!!
        self.close()

    def run_validate(self):
        checker = validate_checker.ValidateChecker(self)
        checker.exec_()

    def pop_file_dialog(self):
        # TODO: Get file path from widget and if it's empty just get home directory
        directory = QtWidgets.QFileDialog().exec_()
        print(directory)
