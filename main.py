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