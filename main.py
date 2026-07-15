import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

class NavButton(QPushButton):
    """A customized QPushButton styled for header navigation."""

    def __init__(self, text: str, parent: QWidget = None) -> None:
        """Initialize the button with standardized size and styling."""
        super().__init__(text, parent)
        self.setFixedSize(QSize(100, 40))
        self.setStyleSheet("""
            QPushButton {
                background-color: #222A2F;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 6px;
                border: none;
            }
            QPushButton:hover {
                background-color: #5c69af;
            }
            QPushButton:pressed {
                background-color: #353f8a;
            }
        """)

class TopBar(QFrame):
    """The top navigation bar containing control buttons and separators."""

    def __init__(self, parent: QWidget = None) -> None:
        """Initialize the top bar container, buttons, and separator line."""
        super().__init__(parent)
        self.setStyleSheet("background-color: #2c3e50;")
        self.setFixedHeight(50)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )

        # --- Navigation Bar Setup ---

        # Setup horizontal layout for the navigation buttons
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 0, 10, 0)
        layout.setSpacing(8)

        # Instantiate navigation buttons
        self.mixer_btn = NavButton("Mixer", self)
        self.game_btn = NavButton("Game", self)
        self.chat_btn = NavButton("Chat", self)
        self.media_btn = NavButton("Media", self)
        self.aux_btn = NavButton("Aux", self)
        self.mic_btn = NavButton("Mic", self)

        # Setup the separation line (30px high to fit cleanly inside top bar)
        line = QFrame()
        line.setFixedWidth(3)
        line.setFixedHeight(30)
        line.setStyleSheet("""
            background-color: #1E282C;
            border: none;
        """)

        # Add widgets to layout in precise visual order
        layout.addWidget(self.mixer_btn)
        layout.addWidget(line) # Visual separator between Mixer and Game
        layout.addWidget(self.game_btn)
        layout.addWidget(self.chat_btn)
        layout.addWidget(self.media_btn)
        layout.addWidget(self.aux_btn)
        layout.addWidget(self.mic_btn)

        # Flexible spacer to push all buttons to the left side
        layout.addStretch()

class MainWidget(QWidget):
    """The main body area managing the 6 audio channel columns."""

    def __init__(self, parent: QWidget = None) -> None:
        """Initialize the layout and create the audio channel columns."""
        super().__init__(parent)

        # Horizontal layout for the 6 columns
        layout = QHBoxLayout(self)
        layout.setSpacing(8) # 8px gap between columns
        layout.setContentsMargins(0, 0, 0, 0)

        # First column is 230px wide, the next 5 are 210px wide
        widths = (230, 210, 210, 210, 210, 210)

        for i, width in enumerate(widths, 1):
            col = QFrame()
            col.setStyleSheet(
                "background-color: #34495e; border-radius: 6px;"
            )
            col.setFixedWidth(width)
            col.setSizePolicy(
                QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding
            )

            # Inside column layout
            col_layout = QVBoxLayout(col)
            label_col = QLabel(f"Col {i}\n({width}px)")
            label_col.setStyleSheet("color: #ecf0f1; font-weight: bold;")
            label_col.setAlignment(Qt.AlignmentFlag.AlignCenter)
            col_layout.addWidget(label_col)

            layout.addWidget(col)

        # Align columns to the left
        layout.addStretch()

class MainWindow(QWidget):
    """The master window fusing TopBar and MainWidget together."""

    def __init__(self) -> None:
        """Set up main window settings, layouts, and sub-widgets."""
        super().__init__()
        self.setWindowTitle("Linux Sound Manager")
        self.setObjectName("MainWindow")

        # Applying background color directly to the main window container
        self.setStyleSheet("#MainWindow { background-color: #222A2F; }")

        # Global vertical layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 0, 0, 5)
        main_layout.setSpacing(5) # Space between TopBar and MainWidget

        # Instantiate the modular components
        self.top_bar = TopBar(self)
        self.main_widget = MainWidget(self)

        # Add components to the main layout
        main_layout.addWidget(self.top_bar)
        main_layout.addWidget(self.main_widget)

        # Connect signals from TopBar to MainWindow slots
        self.connect_signals()

    def connect_signals(self) -> None:
        """Connect all navigation button click signals to their slots."""
        self.top_bar.mixer_btn.clicked.connect(self.on_mixer_clicked)
        self.top_bar.game_btn.clicked.connect(self.on_game_clicked)
        self.top_bar.chat_btn.clicked.connect(self.on_chat_clicked)
        self.top_bar.media_btn.clicked.connect(self.on_media_clicked)
        self.top_bar.aux_btn.clicked.connect(self.on_aux_clicked)
        self.top_bar.mic_btn.clicked.connect(self.on_mic_clicked)

    # --- Navigation Slots ---

    def on_mixer_clicked(self) -> None:
        """Triggered when the Mixer button is clicked."""
        print("View switched to: Mixer")

    def on_game_clicked(self) -> None:
        """Triggered when the Game button is clicked."""
        print("View switched to: Game")

    def on_chat_clicked(self) -> None:
        """Triggered when the Chat button is clicked."""
        print("View switched to: Chat")

    def on_media_clicked(self) -> None:
        """Triggered when the Media button is clicked."""
        print("View switched to: Media")

    def on_aux_clicked(self) -> None:
        """Triggered when the Aux button is clicked."""
        print("View switched to: Aux")

    def on_mic_clicked(self) -> None:
        """Triggered when the Mic button is clicked."""
        print("View switched to: Mic")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())