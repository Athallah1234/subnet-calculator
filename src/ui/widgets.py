from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox,
    QTableWidget, QTableWidgetItem, QHeaderView
)
from PySide6.QtCore import Qt
from typing import Dict, List, Tuple, Any

class InfoCard(QGroupBox):
    """Custom Card/Groupbox to display key-value metrics cleanly."""
    def __init__(self, title: str, parent: QWidget = None):
        super().__init__(title, parent)
        self.layout_widget = QVBoxLayout()
        self.layout_widget.setContentsMargins(12, 12, 12, 12)
        self.layout_widget.setSpacing(8)
        self.setLayout(self.layout_widget)
        self.rows: Dict[str, Tuple[QLabel, QLabel]] = {}

    def add_row(self, key: str, label_text: str):
        row_widget = QWidget()
        row_layout = QHBoxLayout(row_widget)
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.setSpacing(10)
        
        key_label = QLabel(label_text)
        key_label.setStyleSheet("color: #a1a1aa; font-weight: normal;")
        
        val_label = QLabel("-")
        val_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        val_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        row_layout.addWidget(key_label)
        row_layout.addWidget(val_label)
        
        self.layout_widget.addWidget(row_widget)
        self.rows[key] = (key_label, val_label)

    def update_val(self, key: str, val: str):
        if key in self.rows:
            self.rows[key][1].setText(val)

    def clear_vals(self):
        for key in self.rows:
            self.rows[key][1].setText("-")


class SubnetTable(QTableWidget):
    """A standard table widget designed to show subnets dynamically."""
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels([
            "Subnet", "Network Range", "First Host", "Last Host", "Broadcast"
        ])
        
        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setVisible(False)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionBehavior(QTableWidget.SelectRows)

    def populate(self, subnet_list: List[Dict[str, Any]]):
        self.setRowCount(0)
        self.setRowCount(len(subnet_list))
        for row, sub in enumerate(subnet_list):
            self.setItem(row, 0, QTableWidgetItem(f"Subnet {sub.get('index', '')}"))
            self.setItem(row, 1, QTableWidgetItem(sub.get('network', '')))
            self.setItem(row, 2, QTableWidgetItem(sub.get('first_host', '')))
            self.setItem(row, 3, QTableWidgetItem(sub.get('last_host', '')))
            self.setItem(row, 4, QTableWidgetItem(sub.get('broadcast', '')))

    def clear_table(self):
        self.setRowCount(0)
