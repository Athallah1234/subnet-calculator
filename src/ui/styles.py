def get_stylesheet(dark_mode: bool = True) -> str:
    """Returns the QSS stylesheet for the application based on the dark/light mode preference."""
    if dark_mode:
        return """
        /* Dark Theme Stylesheet */
        QMainWindow {
            background-color: #121214;
        }
        
        QWidget {
            color: #e4e4e7;
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
            font-size: 13px;
        }
        
        QGroupBox {
            background-color: #1e1e24;
            border: 1px solid #2d2d34;
            border-radius: 8px;
            margin-top: 12px;
            padding-top: 16px;
            font-weight: bold;
        }
        
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            left: 12px;
            padding: 2px 8px;
            background-color: #1e1e24;
            color: #a1a1aa;
        }

        QLineEdit {
            background-color: #27272a;
            border: 1px solid #3f3f46;
            border-radius: 6px;
            padding: 8px 12px;
            color: #ffffff;
            selection-background-color: #3f3f46;
        }
        
        QLineEdit:focus {
            border: 1px solid #71717a;
        }

        QComboBox {
            background-color: #27272a;
            border: 1px solid #3f3f46;
            border-radius: 6px;
            padding: 8px 12px;
            color: #ffffff;
        }
        
        QComboBox::drop-down {
            border: none;
            width: 24px;
        }
        
        QComboBox::down-arrow {
            image: none;
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 5px solid #a1a1aa;
            margin-top: 2px;
        }

        QPushButton {
            background-color: #27272a;
            border: 1px solid #3f3f46;
            border-radius: 6px;
            padding: 8px 16px;
            color: #ffffff;
            font-weight: bold;
        }
        
        QPushButton:hover {
            background-color: #3f3f46;
        }
        
        QPushButton:pressed {
            background-color: #52525b;
        }

        QPushButton#calculateButton {
            background-color: #097969;
            border: 1px solid #0b6623;
            color: #ffffff;
        }
        
        QPushButton#calculateButton:hover {
            background-color: #0b6623;
        }

        QPushButton#clearButton {
            background-color: #7f1d1d;
            border: 1px solid #991b1b;
            color: #ffffff;
        }
        
        QPushButton#clearButton:hover {
            background-color: #991b1b;
        }

        QTableWidget {
            background-color: #1e1e24;
            border: 1px solid #2d2d34;
            gridline-color: #2d2d34;
            border-radius: 6px;
            color: #e4e4e7;
        }
        
        QHeaderView::section {
            background-color: #27272a;
            color: #a1a1aa;
            padding: 6px;
            border: 1px solid #2d2d34;
            font-weight: bold;
        }
        
        QTableWidget::item:selected {
            background-color: #27272a;
            color: #ffffff;
        }

        QScrollBar:vertical {
            border: none;
            background: #18181b;
            width: 10px;
            margin: 0px;
        }
        
        QScrollBar::handle:vertical {
            background: #3f3f46;
            min-height: 20px;
            border-radius: 5px;
        }
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0px;
        }
        
        QListWidget {
            background-color: #1e1e24;
            border: 1px solid #2d2d34;
            border-radius: 6px;
            padding: 5px;
            color: #e4e4e7;
        }
        
        QListWidget::item {
            padding: 8px;
            border-radius: 4px;
        }
        
        QListWidget::item:hover {
            background-color: #27272a;
        }
        
        QListWidget::item:selected {
            background-color: #3f3f46;
            color: #ffffff;
        }
        
        QLabel#appTitle {
            font-size: 20px;
            font-weight: bold;
            color: #ffffff;
        }
        
        QLabel#appSubtitle {
            font-size: 12px;
            color: #a1a1aa;
        }
        """
    else:
        return """
        /* Light Theme Stylesheet */
        QMainWindow {
            background-color: #f4f4f5;
        }
        
        QWidget {
            color: #18181b;
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
            font-size: 13px;
        }
        
        QGroupBox {
            background-color: #ffffff;
            border: 1px solid #e4e4e7;
            border-radius: 8px;
            margin-top: 12px;
            padding-top: 16px;
            font-weight: bold;
        }
        
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            left: 12px;
            padding: 2px 8px;
            background-color: #ffffff;
            color: #71717a;
        }

        QLineEdit {
            background-color: #ffffff;
            border: 1px solid #d4d4d8;
            border-radius: 6px;
            padding: 8px 12px;
            color: #18181b;
            selection-background-color: #e4e4e7;
        }
        
        QLineEdit:focus {
            border: 1px solid #a1a1aa;
        }

        QComboBox {
            background-color: #ffffff;
            border: 1px solid #d4d4d8;
            border-radius: 6px;
            padding: 8px 12px;
            color: #18181b;
        }
        
        QComboBox::drop-down {
            border: none;
            width: 24px;
        }
        
        QComboBox::down-arrow {
            image: none;
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 5px solid #71717a;
            margin-top: 2px;
        }

        QPushButton {
            background-color: #ffffff;
            border: 1px solid #d4d4d8;
            border-radius: 6px;
            padding: 8px 16px;
            color: #18181b;
            font-weight: bold;
        }
        
        QPushButton:hover {
            background-color: #f4f4f5;
        }
        
        QPushButton:pressed {
            background-color: #e4e4e7;
        }

        QPushButton#calculateButton {
            background-color: #10b981;
            border: 1px solid #059669;
            color: #ffffff;
        }
        
        QPushButton#calculateButton:hover {
            background-color: #059669;
        }

        QPushButton#clearButton {
            background-color: #ef4444;
            border: 1px solid #dc2626;
            color: #ffffff;
        }
        
        QPushButton#clearButton:hover {
            background-color: #dc2626;
        }

        QTableWidget {
            background-color: #ffffff;
            border: 1px solid #e4e4e7;
            gridline-color: #e4e4e7;
            border-radius: 6px;
            color: #18181b;
        }
        
        QHeaderView::section {
            background-color: #f4f4f5;
            color: #71717a;
            padding: 6px;
            border: 1px solid #e4e4e7;
            font-weight: bold;
        }
        
        QTableWidget::item:selected {
            background-color: #f4f4f5;
            color: #18181b;
        }

        QScrollBar:vertical {
            border: none;
            background: #f4f4f5;
            width: 10px;
            margin: 0px;
        }
        
        QScrollBar::handle:vertical {
            background: #d4d4d8;
            min-height: 20px;
            border-radius: 5px;
        }
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0px;
        }
        
        QListWidget {
            background-color: #ffffff;
            border: 1px solid #e4e4e7;
            border-radius: 6px;
            padding: 5px;
            color: #18181b;
        }
        
        QListWidget::item {
            padding: 8px;
            border-radius: 4px;
        }
        
        QListWidget::item:hover {
            background-color: #f4f4f5;
        }
        
        QListWidget::item:selected {
            background-color: #e4e4e7;
            color: #18181b;
        }
        
        QLabel#appTitle {
            font-size: 20px;
            font-weight: bold;
            color: #18181b;
        }
        
        QLabel#appSubtitle {
            font-size: 12px;
            color: #71717a;
        }
        """
