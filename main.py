from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QLineEdit, QComboBox, QVBoxLayout, QListWidget
from PySide6.QtGui import QPixmap, QIcon, QPalette, QColor
from PySide6.QtCore import QSize, QPropertyAnimation, QRect
from sys import argv, exit
from os import startfile, path, environ, makedirs
from minecraft_launcher_lib.utils import get_installed_versions
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        # Define Minecraft directory
        self.user_window = environ["USERNAME"]
        self.minecraft_directory = f"C:/Users/{self.user_window}/AppData/Roaming/Minecraft Launcher"
        # Create folder if it doesn't exist
        makedirs(self.minecraft_directory, exist_ok=True)

        self.setWindowTitle("MinePy Launcher")
        self.setWindowIcon(QIcon(self.resource_path("resources/image/logo.png")))
        self.setGeometry(400, 150, 960, 540)
        self.setFixedSize(960, 540) 
        self.center_window()
        
        # Create a QLabel to display the image
        self.label = QLabel(self)
        image = QPixmap(self.resource_path("resources/image/1_theme.png"))
        self.label.setPixmap(image)
        self.label.resize(960, 540)

        # Create a QWidget and set its background color
        self.widget = QWidget(self)
        self.widget.setGeometry(0, 0, 50, 540)
        palette = self.widget.palette()
        palette.setColor(QPalette.Window, QColor("#1e1e1e"))
        self.widget.setAutoFillBackground(True)
        self.widget.setPalette(palette)

        # Create a download Button
        self.button_download = QPushButton(self)
        self.button_download.setGeometry(2.8, 56, 44, 44)
        self.button_download.setIcon(QIcon(self.resource_path("resources/image/dowload.png")))
        self.button_download.setIconSize(QSize(28, 28))
        self.button_download.setStyleSheet("""
            QPushButton {
            }
            QPushButton:hover {
                background-color: #fe9814;
            }
        """)
        self.button_download.clicked.connect(self.select_widget)
        self.button_download.show()
        
        self.interface = False
        self.interface_user = False
        self.interface_play = False

        # Create a play button
        self.button_play = QPushButton(self)
        self.button_play.setGeometry(2.8, 493, 44, 44)
        self.button_play.setIcon(QIcon(self.resource_path("resources/image/play.png")))
        self.button_play.clicked.connect(self.select_widget_play)
        self.button_play.setStyleSheet("""
            QPushButton {
            }
            QPushButton:hover {
                background-color: #75ad2e;
            }
        """)
        self.button_play.setIconSize(QSize(15, 15))
        self.button_play.show()
        
        # Create a profile button
        self.button_profile = QPushButton(self)
        self.button_profile.setGeometry(2.8, 4, 44, 44)
        self.button_profile.setIcon(QIcon(self.resource_path("resources/image/profile.jpg")))
        self.button_profile.clicked.connect(self.select_widget_user)
        self.button_profile.setIconSize(QSize(28, 28))
        self.button_profile.setStyleSheet("""
            QPushButton {
            }
            QPushButton:hover {
                background-color: #5271ff;
            }
        """)
        self.button_profile.show()

    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', path.abspath("."))
        return path.join(base_path, relative_path)
    
    def select_widget(self):
        if not self.interface:
            self.interface = True
            self.show_interface_download()

            # Create and show tab
            self.tab = QPushButton(self)
            self.tab.setGeometry(2, 52, 10, 10)
            self.tab.setStyleSheet("background-color: #75ad2e;border-radius: 3px;")
            self.tab.show()

            self.widget_download.show()
        else:
            if not self.widget_download.isVisible():
                self.widget_download.show()

            current_geometry = self.widget_download.geometry()

            if current_geometry != QRect(50, 0, 0, 550):
                self.animation = QPropertyAnimation(self.widget_download, b"geometry")
                self.animation.setDuration(50)
                self.animation.setStartValue(current_geometry)
                self.animation.setEndValue(QRect(50, 0, 0, 550))
                self.animation.finished.connect(self.widget_download.hide)
                self.animation.start()

            self.interface = False
            self.tab.hide()

    def select_widget_user(self):
        if not self.interface_user:
            self.interface_user = True
            self.show_interface_user()

            self.tab_user = QPushButton(self)
            self.tab_user.setGeometry(2, 1, 10, 10)
            self.tab_user.setStyleSheet("background-color: #75ad2e;border-radius: 3px;")
            self.tab_user.show()

            self.widget_user.show()
        else:
            if not self.widget_user.isVisible():
                self.widget_user.show()

            current_geometry = self.widget_user.geometry()

            if current_geometry != QRect(50, 0, 0, 550):
                self.animation = QPropertyAnimation(self.widget_user, b"geometry")
                self.animation.setDuration(50)
                self.animation.setStartValue(current_geometry)
                self.animation.setEndValue(QRect(50, 0, 0, 550))
                self.animation.finished.connect(self.widget_user.hide)
                self.animation.start()

            self.interface_user = False
            self.tab_user.hide()

    def select_widget_play(self):
        if not self.interface_play:
            self.interface_play = True
            self.tab_play = QPushButton(self)
            self.tab_play.setGeometry(2, 490, 10, 10)
            self.tab_play.setStyleSheet("background-color: #5271ff;border-radius: 3px;")
            self.tab_play.show()
            self.run_minecraft()

        else:
            self.interface_play = False
            self.widget_run_minecraft.hide()
            self.version_combo_box_instaler.hide()
            self.tab_play.hide()

    def open_folder(self, path):
        return startfile(path)
    
    def show_interface_download(self):
        self.widget_download = QWidget(self)
        self.widget_download.setAutoFillBackground(True)
        self.widget_download.setGeometry(50, 0, 200, 300)
        self.widget_download.setStyleSheet("""
        QWidget {
            background-color: #1e1e1e;
        }""")
        self.widget_download.show()

        self.animation = QPropertyAnimation(self.widget_download, b"geometry")
        self.animation.setDuration(150)
        self.animation.setStartValue(QRect(50, 0, 0, 550))
        self.animation.setEndValue(QRect(50, 0, 200, 550))
        self.animation.start()

        label = QLabel(self.widget_download)
        label.setText("Instalar versiones")
        label.setGeometry(10, 8, 180, 30)
        label.setStyleSheet(""" QLabel { 
            color: white; 
            border-radius: 5px; 
            font-size: 14px;
                            }""")
        label.show()

        self.version_combo_box = QComboBox(self.widget_download)
        self.version_combo_box.addItems(['1.20.1 Forge', '1.19.2 Forge', '1.18.2 Forge', '1.17.1 Forge', '1.16.5 Forge', '1.15.2 Forge', '1.14.4 Forge', '1.12.2 Forge', '1.20.1 Vanilla', '1.20.0 Vanilla', '1.19.4 Vanilla', '1.19.3 Vanilla', '1.19.2 Vanilla', '1.19.1 Vanilla', '1.19.0 Vanilla', '1.18.2 Vanilla', '1.18.1 Vanilla', '1.18.0 Vanilla', '1.17.1 Vanilla', '1.17.0 Vanilla', '1.16.5 Vanilla', '1.16.4 Vanilla', '1.16.3 Vanilla', '1.16.2 Vanilla', '1.16.1 Vanilla', '1.16.0 Vanilla', '1.15.2 Vanilla', '1.15.1 Vanilla', '1.15.0 Vanilla', '1.14.4 Vanilla', '1.14.3 Vanilla', '1.14.2 Vanilla', '1.14.1 Vanilla', '1.14.0 Vanilla', '1.13.2 Vanilla', '1.13.1 Vanilla', '1.13.0 Vanilla', '1.12.2 Vanilla', '1.12.1 Vanilla', '1.12.0 Vanilla', '1.11.2 Vanilla', '1.11.1 Vanilla', '1.11.0 Vanilla', '1.10.2 Vanilla', '1.10.1 Vanilla', '1.10.0 Vanilla', '1.9.4 Vanilla', '1.9.3 Vanilla', '1.9.2 Vanilla', '1.9.1 Vanilla', '1.9.0 Vanilla', '1.8.9 Vanilla', '1.8.8 Vanilla', '1.8.7 Vanilla', '1.8.6 Vanilla', '1.8.5 Vanilla', '1.8.4 Vanilla', '1.8.3 Vanilla', '1.8.2 Vanilla', '1.8.1 Vanilla'])
        self.version_combo_box.setGeometry(10, 38, 152, 33)
        self.version_combo_box.setStyleSheet("""
        QComboBox {
            padding-left: 10px;
            background-color: #393939;
            color: #fff;
        }
        QComboBox QAbstractItemView {
            color: #000;
            background-color: white;
            selection-background-color: #5271ff;
            selection-color: white;
            border-radius:5px;
            margin-top: 5px;
            margin-left: 3px;
        }
        QScrollBar::handle:vertical {
            background: #888;
            min-height: 20px;
            border-radius: 6px;
            margin: 5px;
        }
        QScrollBar::handle:vertical:hover {
            background: #555;
            margin: 5px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            background: none;
            height: 0px;
            margin: 5px;
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
            margin: 5px;
        }""")
        self.version_combo_box.show()

        self.button_install = QPushButton(self.widget_download)
        self.button_install.setStyleSheet("""
            QPushButton{
                background-color: #fe9814;
            }
            QPushButton:hover {   
                background-color: rgba(60,60,60, 0.9);
            }""")
        self.button_install.setIcon(QIcon(self.resource_path("resources/image/dowload.png")))
        self.button_install.setIconSize(QSize(20, 20))
        self.button_install.clicked.connect(self.install_minecraft)
        self.button_install.setGeometry(165, 40, 29, 29)
        self.button_install.show()

        label = QLabel(self.widget_download)
        label.setText("Ajustes")
        label.setGeometry(10, 95, 180, 30)
        label.setStyleSheet(""" QLabel { 
            color: white; 
            border-radius: 5px;
            font-size: 14px;
                            }""")


        self.ram_combo_box = QComboBox(self.widget_download)
        self.ram_combo_box.addItems(["Ninguno","2 GB","4 GB","6 GB","8 GB","10 GB","12 GB","14 GB","16 GB", "18 GB", "20 GB", "22 GB", "24 GB", "26 GB", "28 GB", "30 GB", "32 GB"])
        self.ram_combo_box.setStyleSheet("""
        QComboBox {
            padding-left: 10px;
            background-color: #393939;
            color: white;
        }
        QComboBox QAbstractItemView {
            color: #000;
            background-color: white;
            selection-background-color: #5271ff;
            selection-color: white;
            border-radius:5px;
            margin-top: 5px;
            margin-left: 3px;
        }
        QScrollBar::handle:vertical {
            background: #888;
            min-height: 20px;
            border-radius: 6px;
            margin: 5px;
        }
        QScrollBar::handle:vertical:hover {
            background: #555;
            margin: 5px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            background: none;
            height: 0px;
            margin: 5px;
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
            margin: 5px;
        }
        """)
        self.ram_combo_box.setGeometry(10, 126, 152, 33)
        self.ram_combo_box.show()

        with open(self.resource_path("data/ram.txt"), "r", encoding="UTF-8") as file:
            file_content = file.readline()
            if file_content != "":
                self.ram_combo_box.setItemText(0, f"> {file_content} GB")

        self.widget_list_version = QWidget(self.widget_download)
        self.widget_list_version.setFixedSize(190, 300)
        self.widget_list_version.move(6, 230)
        layout = QVBoxLayout(self.widget_list_version)

        
        label = QLabel(self.widget_download)
        label.setText("Versiones")
        label.setGeometry(10, 205, 175, 30)
        label.setStyleSheet(""" QLabel { 
            color: white; 
            border-radius: 5px;
            font-size: 14px;
                            }""")
        label.show()

        self.version_list = QListWidget()
        layout.addWidget(self.version_list)
        self.version_list.setStyleSheet("""
        QListWidget {
            background-color: #2e2e2e;
            color: white;
            border-radius: 5px;
            padding-top: 5px;
            padding-left: 5px;
        }""")
        self.load_versions()
        self.widget_list_version.show()

        def log_ram():
            with open(self.resource_path("data/ram.txt"), "w", encoding="UTF-8") as file:
                text = self.ram_combo_box.currentText()
                text = text.replace(" GB", "")
                file.write(text)

        self.submit_button = QPushButton("✓", self.widget_download)
        self.submit_button.setGeometry(165, 128, 29, 29)
        self.submit_button.clicked.connect(log_ram)
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(60,60,60,0.9);
                color: white;
            }
            QPushButton:hover {
                background-color: #5271ff;
            }
        """)
        self.submit_button.show()

        self.button_folder = QPushButton(self.widget_download)
        self.button_folder.setIcon(QIcon(self.resource_path("resources/image/folder.png")))
        self.button_folder.setIconSize(QSize(20, 20))
        self.button_folder.clicked.connect(lambda: self.open_folder(self.minecraft_directory))
        self.button_folder.setStyleSheet("""
            QPushButton{
                background-color: rgba(60,60,60,0.9);
            }
            QPushButton:hover {   
                background-color: #5271ff;
            }""")
        self.button_folder.setGeometry(160, 205, 29, 29)
        self.button_folder.show()

    def load_versions(self):
        versiones_instaladas = get_installed_versions(self.minecraft_directory)
        versiones_lista = [version['id'] for version in versiones_instaladas]

        if not versiones_lista:
            self.version_list.addItem("Ninguna")
        else:
            for version in versiones_lista:
                self.version_list.addItem(version)

    def show_interface_user(self):
        self.widget_user = QWidget(self)
        self.widget_user.setAutoFillBackground(True)
        self.widget_user.setGeometry(50, 0, 200, 300)
        self.widget_user.setStyleSheet("""
        QWidget {
            background-color: #1e1e1e;
        }""")
        self.widget_user.show()

        self.animation = QPropertyAnimation(self.widget_user, b"geometry")
        self.animation.setDuration(150)
        self.animation.setStartValue(QRect(50, 0, 0, 550))
        self.animation.setEndValue(QRect(50, 0, 200, 550))
        self.animation.start()

        self.username_input = QLineEdit(self.widget_user)
        self.username_input.setGeometry(10, 5, 180, 30)

        with open(self.resource_path("data/name.txt"), "r", encoding="UTF-8") as file:
            file_content = file.readline()
            if file_content != "":
                self.username_input.setText(file_content)

        self.username_input.setPlaceholderText("Nombre de usuario")
        self.username_input.setStyleSheet("""
        QLineEdit {
            padding-left: 5px;
            background-color: #393939;
            color: white;
            border-radius: 3px;
        }""")
        self.username_input.show()

        def log_name():
            with open(self.resource_path("data/name.txt"), "w", encoding="UTF-8") as file:
                file.write(self.username_input.text())
                self.name = file
        
        self.submit_button = QPushButton("✓", self.widget_user)
        self.submit_button.setGeometry(159, 38, 30, 30)
        self.submit_button.clicked.connect(log_name)
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(60,60,60,0.9);
                color: white;
            }
            QPushButton:hover {
                background-color: #75ad2e;
            }
        """)
        self.submit_button.show()

    def install_minecraft(self):
        from minecraft_launcher_lib.install import install_minecraft_version
        from minecraft_launcher_lib.forge import find_forge_version, install_forge_version
        from PySide6.QtCore import QThread, Signal
        from PySide6.QtWidgets import QProgressBar

        class InstallThread(QThread):
            progress = Signal(int)
            finished = Signal()

            def __init__(self, version, minecraft_directory, version_detecter):
                super().__init__()
                self.version = version
                self.minecraft_directory = minecraft_directory
                self.version_detecter = version_detecter

            def run(self):
                try:
                    if self.version_detecter:
                        forge_version = find_forge_version(self.version)
                        install_forge_version(forge_version, self.minecraft_directory)
                    else:
                        install_minecraft_version(self.version, self.minecraft_directory)
                    self.finished.emit()
                except Exception as e:
                    print(f"Error al instalar la versión: {e}")

        version = self.version_combo_box.currentText()

        self.widget_install_background = QWidget(self)
        self.widget_install_background.setGeometry(0, 0, 960, 540)
        self.widget_install_background.setStyleSheet("""
        QWidget {
            background-color: rgba(0, 0, 0, 0.3);
            }""")
        self.widget_install_background.show()

        self.widget_install = QWidget(self.widget_install_background)
        self.widget_install.setGeometry(270, 200, 500, 100)
        self.widget_install.setStyleSheet("""
        QWidget {
            background-color: #1e1e1e;
            border-radius: 10px;
            }""")
        self.widget_install.show()

        self.label_installer_version = QLabel(self.widget_install_background)
        self.label_installer_version.setText(f"Instalando {version}")
        self.label_installer_version.setGeometry(400, 210, 300, 35)
        self.label_installer_version.setStyleSheet("""
        QLabel {
            background-color: transparent;
            color: #fff;
            font-size: 24px;
            }""")
        self.label_installer_version.show()

        self.progress_bar = QProgressBar(self.widget_install_background)
        self.progress_bar.setGeometry(320, 250, 400, 20)
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #ffffff;
                border-radius: 5px;
                background-color: #1e1e1e;
            }
            QProgressBar::chunk {
                background-color: #ffffff;
                width: 20px;
            }
        """)
        self.progress_bar.show()

        self.select_widget()

        minecraft_directory = self.minecraft_directory
        version_detecter = "Forge" in version
        version = version.replace(" Forge", "").replace(" Vanilla", "")

        self.install_thread = InstallThread(version, minecraft_directory, version_detecter)
        self.install_thread.finished.connect(self.on_install_finished)
        self.install_thread.start()

    def on_install_finished(self):
        self.progress_bar.hide()
        self.label_installer_version.hide()
        self.widget_install.hide()
        self.widget_install_background.hide()

    def run_minecraft(self):
        from PySide6.QtWidgets import QVBoxLayout
        from minecraft_launcher_lib.utils import get_installed_versions

        # Obtener el directorio del usuario
        minecraft_directory = self.minecraft_directory

        # Crear la interfaz gráfica
        self.widget_run_minecraft = QWidget(self)
        self.widget_run_minecraft.setAutoFillBackground(True)
        self.widget_run_minecraft.setGeometry(350, 50, 300, 100)
        self.widget_run_minecraft.setStyleSheet("""
        QWidget {
            background-color: #1e1e1e;
            border-radius: 5px
        }""")
        self.widget_run_minecraft.show()

        layout = QVBoxLayout(self.widget_run_minecraft)

        label = QLabel("Selecciona la versión de Minecraft:")
        label.setStyleSheet("""
        QLabel {
            color: white;
        }""")
        layout.addWidget(label)

        self.version_combo_box_instaler = QComboBox(self.widget_run_minecraft)
        self.version_combo_box_instaler.setStyleSheet("""
        QComboBox {
            padding-left: 10px;
            background-color: #393939;
            color: #fff;
        }
        QComboBox QAbstractItemView {
            color: #000;
            background-color: white;
            selection-background-color: #5271ff;
            selection-color: white;
            border-radius:5px;
            margin-top: 5px;
            margin-left: 3px;
        }
        QScrollBar::handle:vertical {
            background: #888;
            min-height: 20px;
            border-radius: 6px;
            margin: 5px;
        }
        QScrollBar::handle:vertical:hover {
            background: #555;
            margin: 5px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            background: none;
            height: 0px;
            margin: 5px;
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
            margin: 5px;
        }""")
        layout.addWidget(self.version_combo_box_instaler)

        # Cargar las versiones instaladas
        versiones_instaladas = get_installed_versions(minecraft_directory)
        versiones_lista = [version['id'] for version in versiones_instaladas]

        if not versiones_lista:
            self.version_combo_box_instaler.addItem("No hay versiones instaladas.")
        else:
            for version in versiones_lista:
                self.version_combo_box_instaler.addItem(version)

        self.button_run = QPushButton("Iniciar Minecraft", self.widget_run_minecraft)
        self.button_run.setStyleSheet("""
            QPushButton{
                background-color: #75ad2e;
                color: white;
            }
            QPushButton:hover {   
                background-color: #403b0d;
            }""")
        self.button_run.clicked.connect(self.ejecutar_minecraft)
        layout.addWidget(self.button_run)

        self.widget_run_minecraft.show()

    def ejecutar_minecraft(self):
        from minecraft_launcher_lib.command import get_minecraft_command
        from subprocess import Popen, CREATE_NO_WINDOW

        # Obtener el directorio del usuario
        minecraft_directory = self.minecraft_directory

        with open(self.resource_path("data/name.txt"), "r", encoding="UTF-8") as file:
            file_content = file.readline()

        with open(self.resource_path("data/ram.txt"), "r", encoding="UTF-8") as file:
            file_content = file.readline()
            self.ram = int(file_content)

        # Variables predefinidas
        mine_user = file_content.strip() or "Player"
        ram = self.ram or 4
        version_seleccionada = self.version_combo_box_instaler.currentText()

        # Función para ejecutar Minecraft
        versiones_instaladas = get_installed_versions(minecraft_directory)
        versiones_lista = [version['id'] for version in versiones_instaladas]

        if not versiones_lista:
            print("No hay versiones instaladas.")
            return

        if version_seleccionada not in versiones_lista:
            print(f"La versión {version_seleccionada} no está instalada.")
            return

        options = {
            'username': mine_user,
            'uuid': '',
            'token': '',
            'jvmArguments': [f"-Xmx{ram}G", f"-Xms{ram}G"],
            'launcherVersion': "0.0.2"
        }

        try:
            minecraft_command = get_minecraft_command(version_seleccionada, minecraft_directory, options)

            # Ejecutar sin mostrar terminal (en Windows)
            Popen(
                minecraft_command,
                creationflags=CREATE_NO_WINDOW,  # Ocultar terminal
                shell=False
            )
        except Exception as e:
            print(f"Error al ejecutar Minecraft: {e}")
    
    def center_window(self):
        frame_geo = self.frameGeometry()
        screen = QApplication.primaryScreen()
        center_point = screen.availableGeometry().center()
        frame_geo.moveCenter(center_point)
        self.move(frame_geo.topLeft())

if __name__ == "__main__":
    app = QApplication(argv)   
    style_sheet = """
    QPushButton {
        background-color: rgba(60,60,60,0.75);
        color: black;
        border-radius: 5px;
        padding: 0px;
        font-size: 14px;
    }
    QComboBox {
        padding-left: 10px;
        color: white;
    }
    """
    app.setStyleSheet(style_sheet)
    ventana = MainWindow()
    ventana.show()
    exit(app.exec())
