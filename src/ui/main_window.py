import os
import json
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QComboBox, QPushButton, QTabWidget, QScrollArea, QFileDialog,
    QMessageBox, QListWidget, QSplitter, QGroupBox, QTableWidget,
    QTableWidgetItem, QHeaderView, QMenu, QMenuBar, QApplication
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QKeySequence, QAction, QClipboard
from src.ui.styles import get_stylesheet
from src.ui.widgets import InfoCard, SubnetTable
from src.calculator.ipv4 import calculate_ipv4, subnet_ipv4
from src.calculator.ipv6 import calculate_ipv6
from src.calculator.cidr import calculate_cidr
from src.utils.validators import validate_cidr_input
from src.utils.formatters import format_number, format_to_txt, format_to_json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Subnet Calculator")
        self.setMinimumSize(QSize(950, 700))
        
        # Load user configurations (theme, history)
        self.config_dir = os.path.join(os.path.expanduser("~"), ".gemini", "antigravity", "simple-subnet-calculator")
        os.makedirs(self.config_dir, exist_ok=True)
        self.config_file = os.path.join(self.config_dir, "config.json")
        self.history_file = os.path.join(self.config_dir, "history.json")
        
        self.dark_mode = self.load_theme_preference()
        self.history_list_data = self.load_history()
        
        # Setup UI
        self.init_ui()
        self.apply_theme()

    def load_theme_preference(self) -> bool:
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as f:
                    cfg = json.load(f)
                    return cfg.get("dark_mode", True)
            except Exception:
                pass
        return True

    def save_theme_preference(self):
        try:
            with open(self.config_file, "w") as f:
                json.dump({"dark_mode": self.dark_mode}, f)
        except Exception:
            pass

    def load_history(self) -> list:
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, "r") as f:
                    return json.load(f)
            except Exception:
                pass
        return []

    def save_history(self):
        try:
            with open(self.history_file, "w") as f:
                json.dump(self.history_list_data, f)
        except Exception:
            pass

    def add_to_history(self, input_val: str, calc_type: str):
        item = {"input": input_val, "type": calc_type}
        if item in self.history_list_data:
            self.history_list_data.remove(item)
        self.history_list_data.insert(0, item)
        # limit history size to 20
        self.history_list_data = self.history_list_data[:20]
        self.save_history()
        self.update_history_widget()

    def update_history_widget(self):
        self.history_widget.clear()
        for idx, item in enumerate(self.history_list_data):
            self.history_widget.addItem(f"{item['input']} ({item['type']})")

    def init_ui(self):
        # Menu Bar
        self.setup_menu_bar()

        # Central Widget Splitter
        main_splitter = QSplitter(Qt.Horizontal)
        self.setCentralWidget(main_splitter)

        # Right Panel: History Panel (Collapsible / Toggleable)
        self.history_panel = QWidget()
        history_layout = QVBoxLayout(self.history_panel)
        history_layout.setContentsMargins(10, 10, 10, 10)
        
        hist_title = QLabel("Calculation History")
        hist_title.setStyleSheet("font-weight: bold; font-size: 14px;")
        history_layout.addWidget(hist_title)

        self.history_widget = QListWidget()
        self.history_widget.itemDoubleClicked.connect(self.load_history_item)
        history_layout.addWidget(self.history_widget)
        self.update_history_widget()

        hist_btn_layout = QHBoxLayout()
        self.btn_del_hist = QPushButton("Delete")
        self.btn_del_hist.clicked.connect(self.delete_selected_history)
        self.btn_clear_hist = QPushButton("Clear All")
        self.btn_clear_hist.clicked.connect(self.clear_all_history)
        hist_btn_layout.addWidget(self.btn_del_hist)
        hist_btn_layout.addWidget(self.btn_clear_hist)
        history_layout.addLayout(hist_btn_layout)

        # Left Panel: Main Workspace Panel
        workspace_widget = QWidget()
        workspace_layout = QVBoxLayout(workspace_widget)
        workspace_layout.setContentsMargins(16, 16, 16, 16)
        workspace_layout.setSpacing(12)

        # Application Title Header
        header_widget = QWidget()
        header_layout = QVBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(2)
        
        app_title = QLabel("Simple Subnet Calculator")
        app_title.setObjectName("appTitle")
        app_sub = QLabel("IPv4 / IPv6 / CIDR Network Calculator")
        app_sub.setObjectName("appSubtitle")
        
        header_layout.addWidget(app_title)
        header_layout.addWidget(app_sub)
        workspace_layout.addWidget(header_widget)

        # Top Control Area: Inputs
        top_ctrl_group = QGroupBox("Configuration")
        top_ctrl_layout = QHBoxLayout(top_ctrl_group)
        top_ctrl_layout.setContentsMargins(12, 16, 12, 12)
        top_ctrl_layout.setSpacing(10)

        # IP Input
        ip_label_layout = QVBoxLayout()
        ip_label_layout.setSpacing(4)
        ip_lbl = QLabel("IP Address / CIDR")
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("e.g. 192.168.1.10/24 or 2001:db8::1/64")
        self.ip_input.returnPressed.connect(self.calculate)
        ip_label_layout.addWidget(ip_lbl)
        ip_label_layout.addWidget(self.ip_input)
        top_ctrl_layout.addLayout(ip_label_layout, 4)

        # Calculator Type Dropdown
        type_layout = QVBoxLayout()
        type_layout.setSpacing(4)
        type_lbl = QLabel("Calculator Type")
        self.type_combo = QComboBox()
        self.type_combo.addItems(["IPv4", "IPv6", "CIDR"])
        self.type_combo.currentIndexChanged.connect(self.on_type_changed)
        type_layout.addWidget(type_lbl)
        type_layout.addWidget(self.type_combo)
        top_ctrl_layout.addLayout(type_layout, 2)

        # Prefix Dropdown (Visible only when missing from IP Input)
        self.prefix_layout = QVBoxLayout()
        self.prefix_layout.setSpacing(4)
        self.prefix_lbl = QLabel("Default Prefix")
        self.prefix_combo = QComboBox()
        self.prefix_combo.addItems([f"/{i}" for i in range(33)])
        self.prefix_combo.setCurrentText("/24")
        self.prefix_layout.addWidget(self.prefix_lbl)
        self.prefix_layout.addWidget(self.prefix_combo)
        top_ctrl_layout.addLayout(self.prefix_layout, 2)

        # Device Count Input (Optional)
        self.device_layout = QVBoxLayout()
        self.device_layout.setSpacing(4)
        self.device_lbl = QLabel("Jumlah Perangkat (Opsional)")
        self.device_input = QLineEdit()
        self.device_input.setPlaceholderText("e.g. 50")
        self.device_input.textChanged.connect(self.on_device_count_changed)
        self.device_layout.addWidget(self.device_lbl)
        self.device_layout.addWidget(self.device_input)
        top_ctrl_layout.addLayout(self.device_layout, 2)

        # Calculate & Clear Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(8)
        self.btn_calc = QPushButton("Calculate")
        self.btn_calc.setObjectName("calculateButton")
        self.btn_calc.clicked.connect(self.calculate)
        
        self.btn_clear = QPushButton("Clear")
        self.btn_clear.setObjectName("clearButton")
        self.btn_clear.clicked.connect(self.clear_fields)
        
        btn_layout.addWidget(self.btn_calc)
        btn_layout.addWidget(self.btn_clear)
        
        # Assemble Top Controls
        top_layout_wrapper = QVBoxLayout()
        top_layout_wrapper.addWidget(top_ctrl_group)
        top_layout_wrapper.addLayout(btn_layout)
        workspace_layout.addLayout(top_layout_wrapper)

        # Central Workspace Tab Widget
        self.tab_widget = QTabWidget()
        
        # Tab 1: Calculator Outputs
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setSpacing(12)
        
        self.setup_result_cards()
        self.scroll_area.setWidget(self.scroll_widget)
        
        self.tab_widget.addTab(self.scroll_area, "Calculations")
        
        # Tab 2: Prefix Reference Table
        self.ref_table = QTableWidget()
        self.setup_reference_table()
        self.tab_widget.addTab(self.ref_table, "Prefix Reference Table")
        
        workspace_layout.addWidget(self.tab_widget)

        # Bottom Actions Bar
        bottom_actions = QHBoxLayout()
        self.btn_copy = QPushButton("Copy Result")
        self.btn_copy.clicked.connect(self.copy_result)
        self.btn_save_txt = QPushButton("Save TXT")
        self.btn_save_txt.clicked.connect(self.save_txt_result)
        self.btn_save_json = QPushButton("Export JSON")
        self.btn_save_json.clicked.connect(self.save_json_result)
        
        bottom_actions.addWidget(self.btn_copy)
        bottom_actions.addWidget(self.btn_save_txt)
        bottom_actions.addWidget(self.btn_save_json)
        workspace_layout.addLayout(bottom_actions)

        # Add widgets to splitter
        main_splitter.addWidget(workspace_widget)
        main_splitter.addWidget(self.history_panel)
        main_splitter.setSizes([750, 200])

        # Active calculation store
        self.last_calculation_data = {}

    def setup_menu_bar(self):
        menubar = self.menuBar()

        # File Menu
        file_menu = menubar.addMenu("File")
        
        act_calc = QAction("Calculate", self)
        act_calc.setShortcut("Ctrl+Return")
        act_calc.triggered.connect(self.calculate)
        file_menu.addAction(act_calc)
        
        act_clear = QAction("Clear", self)
        act_clear.setShortcut("Ctrl+L")
        act_clear.triggered.connect(self.clear_fields)
        file_menu.addAction(act_clear)
        
        act_save = QAction("Save Result (TXT)", self)
        act_save.setShortcut("Ctrl+S")
        act_save.triggered.connect(self.save_txt_result)
        file_menu.addAction(act_save)
        
        act_json = QAction("Export JSON", self)
        act_json.triggered.connect(self.save_json_result)
        file_menu.addAction(act_json)
        
        file_menu.addSeparator()
        
        act_quit = QAction("Exit", self)
        act_quit.setShortcut("Ctrl+Q")
        act_quit.triggered.connect(self.close)
        file_menu.addAction(act_quit)

        # Tools Menu
        tools_menu = menubar.addMenu("Tools")
        
        act_t_ipv4 = QAction("IPv4 Calculator", self)
        act_t_ipv4.triggered.connect(lambda: self.type_combo.setCurrentText("IPv4"))
        tools_menu.addAction(act_t_ipv4)
        
        act_t_ipv6 = QAction("IPv6 Calculator", self)
        act_t_ipv6.triggered.connect(lambda: self.type_combo.setCurrentText("IPv6"))
        tools_menu.addAction(act_t_ipv6)
        
        act_t_cidr = QAction("CIDR Calculator", self)
        act_t_cidr.triggered.connect(lambda: self.type_combo.setCurrentText("CIDR"))
        tools_menu.addAction(act_t_cidr)

        # View Menu
        view_menu = menubar.addMenu("View")
        
        act_light = QAction("Light Mode", self)
        act_light.triggered.connect(lambda: self.set_theme(False))
        view_menu.addAction(act_light)
        
        act_dark = QAction("Dark Mode", self)
        act_dark.triggered.connect(lambda: self.set_theme(True))
        view_menu.addAction(act_dark)

        # Toggle History Shortcut
        act_hist = QAction("Toggle History Panel", self)
        act_hist.setShortcut("Ctrl+H")
        act_hist.triggered.connect(self.toggle_history_panel)
        view_menu.addAction(act_hist)

        # Help Menu
        help_menu = menubar.addMenu("Help")
        
        act_shortcuts = QAction("Keyboard Shortcuts", self)
        act_shortcuts.triggered.connect(self.show_shortcuts)
        help_menu.addAction(act_shortcuts)
        
        act_about = QAction("About", self)
        act_about.triggered.connect(self.show_about)
        help_menu.addAction(act_about)

    def setup_result_cards(self):
        # Card 1: Basic Information
        self.card_basic = InfoCard("Basic Information")
        self.card_basic.add_row("ip_address", "IP Address")
        self.card_basic.add_row("cidr", "CIDR Prefix")
        self.card_basic.add_row("subnet_mask", "Subnet Mask")
        self.card_basic.add_row("wildcard_mask", "Wildcard Mask")
        self.card_basic.add_row("network_address", "Network Address")
        self.card_basic.add_row("broadcast_address", "Broadcast Address")
        self.card_basic.add_row("first_host", "First Usable Host")
        self.card_basic.add_row("last_host", "Last Usable Host")
        self.card_basic.add_row("total_addr", "Total Addresses")
        self.card_basic.add_row("usable_hosts", "Usable Hosts")
        self.scroll_layout.addWidget(self.card_basic)

        # Card 2: Classification
        self.card_class = InfoCard("Classification")
        self.card_class.add_row("addr_type", "Address Type")
        self.card_class.add_row("scope", "Scope")
        self.card_class.add_row("private", "Private/Public")
        self.card_class.add_row("loopback", "Loopback")
        self.card_class.add_row("link_local", "Link-local")
        self.card_class.add_row("multicast", "Multicast")
        self.card_class.add_row("reserved", "Reserved")
        self.card_class.add_row("unspecified", "Unspecified")
        self.card_class.add_row("global", "Global")
        self.card_class.add_row("documentation", "Documentation")
        self.scroll_layout.addWidget(self.card_class)

        # Card 3: Binary Representation
        self.card_binary = QGroupBox("Binary Representation")
        binary_layout = QVBoxLayout(self.card_binary)
        binary_layout.setContentsMargins(12, 16, 12, 12)
        binary_layout.setSpacing(6)
        
        self.lbl_bin_ip = QLabel("IP Address: -")
        self.lbl_bin_ip.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.lbl_bin_bits = QLabel("Binary: -")
        self.lbl_bin_bits.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.lbl_bin_sep = QLabel("Network Bits | Host Bits:\n-")
        self.lbl_bin_sep.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        binary_layout.addWidget(self.lbl_bin_ip)
        binary_layout.addWidget(self.lbl_bin_bits)
        binary_layout.addWidget(self.lbl_bin_sep)
        self.scroll_layout.addWidget(self.card_binary)

        # Card 4: IPv4 Subnetting Pane
        self.card_subnetting = QGroupBox("IPv4 Subnetting")
        sub_layout = QVBoxLayout(self.card_subnetting)
        sub_layout.setContentsMargins(12, 16, 12, 12)
        sub_layout.setSpacing(8)

        inputs_layout = QHBoxLayout()
        lbl_new_pref = QLabel("New Prefix:")
        self.combo_new_prefix = QComboBox()
        self.combo_new_prefix.addItems([f"/{i}" for i in range(33)])
        self.combo_new_prefix.setCurrentText("/26")
        
        self.btn_calc_subnet = QPushButton("Calculate Subnets")
        self.btn_calc_subnet.clicked.connect(self.calculate_subnets)
        
        inputs_layout.addWidget(lbl_new_pref)
        inputs_layout.addWidget(self.combo_new_prefix)
        inputs_layout.addWidget(self.btn_calc_subnet)
        sub_layout.addLayout(inputs_layout)

        self.lbl_sub_info = QLabel("Subnet Information: -")
        sub_layout.addWidget(self.lbl_sub_info)

        self.subnet_table = SubnetTable()
        sub_layout.addWidget(self.subnet_table)
        self.scroll_layout.addWidget(self.card_subnetting)

    def setup_reference_table(self):
        self.ref_table.setColumnCount(5)
        self.ref_table.setHorizontalHeaderLabels([
            "Prefix", "Subnet Mask", "Wildcard Mask", "Total Addresses", "Usable Hosts"
        ])
        self.ref_table.verticalHeader().setVisible(False)
        self.ref_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ref_table.setSelectionBehavior(QTableWidget.SelectRows)
        header = self.ref_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        self.ref_table.setRowCount(33)
        for i in range(33):
            # CIDR info
            import ipaddress
            try:
                net = ipaddress.IPv4Network(f"0.0.0.0/{i}", strict=False)
                mask = str(net.netmask)
                netmask_int = int(net.netmask)
                wildcard_int = netmask_int ^ 0xFFFFFFFF
                wildcard = str(ipaddress.IPv4Address(wildcard_int))
                
                total = net.num_addresses
                if i == 32:
                    usable = 1
                elif i == 31:
                    usable = 2
                else:
                    usable = total - 2
            except Exception:
                mask, wildcard, total, usable = "-", "-", "-", "-"

            self.ref_table.setItem(i, 0, QTableWidgetItem(f"/{i}"))
            self.ref_table.setItem(i, 1, QTableWidgetItem(mask))
            self.ref_table.setItem(i, 2, QTableWidgetItem(wildcard))
            self.ref_table.setItem(i, 3, QTableWidgetItem(format_number(total)))
            self.ref_table.setItem(i, 4, QTableWidgetItem(format_number(usable)))

    def apply_theme(self):
        self.setStyleSheet(get_stylesheet(self.dark_mode))

    def set_theme(self, dark: bool):
        self.dark_mode = dark
        self.apply_theme()
        self.save_theme_preference()

    def toggle_history_panel(self):
        self.history_panel.setVisible(not self.history_panel.isVisible())

    def on_type_changed(self):
        calc_type = self.type_combo.currentText()
        if calc_type == "IPv4" or calc_type == "CIDR":
            self.prefix_combo.clear()
            self.prefix_combo.addItems([f"/{i}" for i in range(33)])
            self.prefix_combo.setCurrentText("/24")
            self.prefix_layout.setEnabled(True)
            self.card_subnetting.setVisible(True)
        else: # IPv6
            self.prefix_combo.clear()
            self.prefix_combo.addItems([f"/{i}" for i in range(129)])
            self.prefix_combo.setCurrentText("/64")
            self.prefix_layout.setEnabled(True)
            self.card_subnetting.setVisible(False)
        self.on_device_count_changed()

    def on_device_count_changed(self):
        text = self.device_input.text().strip()
        if not text:
            return
        
        try:
            num_devices = int(text)
            if num_devices <= 0:
                return
            
            calc_type = self.type_combo.currentText()
            if calc_type == "IPv6":
                import math
                prefix = 128 - math.ceil(math.log2(num_devices))
                prefix = max(0, min(128, prefix))
                self.prefix_combo.setCurrentText(f"/{prefix}")
            else:
                import math
                if num_devices == 1:
                    prefix = 30
                else:
                    prefix = 32 - math.ceil(math.log2(num_devices + 2))
                prefix = max(0, min(30, prefix))
                self.prefix_combo.setCurrentText(f"/{prefix}")
        except ValueError:
            pass

    def calculate(self):
        input_text = self.ip_input.text().strip()
        if not input_text:
            QMessageBox.warning(self, "Invalid Input", "Please enter an IP address or network range.")
            return

        is_valid, clean_ip_or_network, prefix = validate_cidr_input(input_text)
        if not is_valid:
            QMessageBox.critical(self, "Error Parsing Input", clean_ip_or_network)
            return

        # Determine actual version of the input
        import ipaddress
        ip_part = clean_ip_or_network.split('/')[0]
        try:
            ipaddress.IPv4Address(ip_part)
            detected_version = "IPv4"
        except ipaddress.AddressValueError:
            try:
                ipaddress.IPv6Address(ip_part)
                detected_version = "IPv6"
            except ipaddress.AddressValueError:
                QMessageBox.critical(self, "Error Parsing Input", f"Invalid IP address format: {ip_part}")
                return

        calc_type = self.type_combo.currentText()
        
        # Auto-switch dropdown type if there is a mismatch (unless CIDR is selected)
        if calc_type != "CIDR" and calc_type != detected_version:
            self.type_combo.setCurrentText(detected_version)
            calc_type = detected_version

        # If prefix is missing from IP field, parse default from dropdown
        if prefix is None:
            prefix_str = self.prefix_combo.currentText().replace('/', '')
            prefix = int(prefix_str)
            full_input = f"{clean_ip_or_network}/{prefix}"
        else:
            full_input = clean_ip_or_network

        try:
            if calc_type == "IPv4":
                # Ensure it's IPv4
                ip_part = full_input.split('/')[0]
                self.run_ipv4_calc(ip_part, prefix)
            elif calc_type == "IPv6":
                # Ensure it's IPv6
                ip_part = full_input.split('/')[0]
                self.run_ipv6_calc(ip_part, prefix)
            elif calc_type == "CIDR":
                self.run_cidr_calc(full_input)
            
            # Save search to history
            self.add_to_history(full_input, calc_type)
        except Exception as e:
            QMessageBox.critical(self, "Calculation Error", f"An error occurred: {str(e)}")

    def run_ipv4_calc(self, ip_str: str, prefix: int):
        data = calculate_ipv4(ip_str, prefix)
        self.last_calculation_data = data
        
        # Populate basic info card
        self.card_basic.update_val("ip_address", data["ip_address"])
        self.card_basic.update_val("cidr", data["cidr_prefix"])
        self.card_basic.update_val("subnet_mask", data["subnet_mask"])
        self.card_basic.update_val("wildcard_mask", data["wildcard_mask"])
        self.card_basic.update_val("network_address", data["network_address"])
        self.card_basic.update_val("broadcast_address", data["broadcast_address"])
        self.card_basic.update_val("first_host", data["first_usable_host"])
        self.card_basic.update_val("last_host", data["last_usable_host"])
        self.card_basic.update_val("total_addr", format_number(data["number_of_addresses"]))
        self.card_basic.update_val("usable_hosts", format_number(data["number_of_usable_hosts"]))

        # Populate classifications
        cls = data["classification"]
        self.card_class.update_val("addr_type", cls["address_type"])
        self.card_class.update_val("scope", cls["scope"])
        self.card_class.update_val("private", "Yes (Private)" if cls["address_type"] == "Private IPv4" else "No (Public)")
        self.card_class.update_val("loopback", cls["loopback"])
        self.card_class.update_val("link_local", cls["link_local"])
        self.card_class.update_val("multicast", cls["multicast"])
        self.card_class.update_val("reserved", cls["reserved"])
        self.card_class.update_val("unspecified", cls["unspecified"])
        self.card_class.update_val("global", cls["global"])
        self.card_class.update_val("documentation", cls["documentation"])

        # Binary
        bin_data = data["binary"]
        self.lbl_bin_ip.setText(f"IP Address: {bin_data['ip']}")
        self.lbl_bin_bits.setText(f"Binary: {bin_data['binary']}")
        self.lbl_bin_sep.setText(f"Network Bits | Host Bits:\n{bin_data['network_host']}")

        # Enable subnet combo setup
        self.combo_new_prefix.clear()
        self.combo_new_prefix.addItems([f"/{i}" for i in range(prefix, 33)])
        self.combo_new_prefix.setCurrentText(f"/{min(prefix+2, 32)}")
        self.card_subnetting.setVisible(True)
        self.subnet_table.clear_table()
        self.lbl_sub_info.setText("Subnet Information: -")

    def run_ipv6_calc(self, ip_str: str, prefix: int):
        data = calculate_ipv6(ip_str, prefix)
        self.last_calculation_data = data

        self.card_basic.update_val("ip_address", data["ipv6_address"])
        self.card_basic.update_val("cidr", data["prefix_length"])
        self.card_basic.update_val("subnet_mask", "N/A")
        self.card_basic.update_val("wildcard_mask", "N/A")
        self.card_basic.update_val("network_address", data["network_address"])
        self.card_basic.update_val("broadcast_address", "N/A")
        self.card_basic.update_val("first_host", data["first_address"])
        self.card_basic.update_val("last_host", data["last_address"])
        self.card_basic.update_val("total_addr", format_number(data["number_of_addresses"]))
        self.card_basic.update_val("usable_hosts", format_number(data["number_of_addresses"]))

        cls = data["classification"]
        self.card_class.update_val("addr_type", cls["address_type"])
        self.card_class.update_val("scope", cls["scope"])
        self.card_class.update_val("private", "Yes" if cls["documentation"] == "Yes" else "No")
        self.card_class.update_val("loopback", cls["loopback"])
        self.card_class.update_val("link_local", cls["link_local"])
        self.card_class.update_val("multicast", cls["multicast"])
        self.card_class.update_val("reserved", cls["reserved"])
        self.card_class.update_val("unspecified", cls["unspecified"])
        self.card_class.update_val("global", cls["global"])
        self.card_class.update_val("documentation", cls["documentation"])

        # Display Exploded vs Expanded
        self.lbl_bin_ip.setText(f"Compressed: {data['compressed_address']}")
        self.lbl_bin_bits.setText(f"Expanded  : {data['expanded_address']}")
        
        p_info = data["prefix_info"]
        self.lbl_bin_sep.setText(f"Prefix Length: {p_info['prefix_length']} | Network Bits: {p_info['network_bits']} | Interface Bits: {p_info['interface_bits']}")

        # Disable Subnetting Card (not support list subnets)
        self.card_subnetting.setVisible(False)

    def run_cidr_calc(self, network_cidr: str):
        parts = network_cidr.split('/')
        ip_addr = parts[0]
        prefix = int(parts[1]) if len(parts) == 2 else (24 if ":" not in ip_addr else 64)
        
        import ipaddress
        try:
            ipaddress.IPv4Address(ip_addr)
            self.run_ipv4_calc(ip_addr, prefix)
        except ipaddress.AddressValueError:
            self.run_ipv6_calc(ip_addr, prefix)

    def calculate_subnets(self):
        if not self.last_calculation_data or "ip_address" not in self.last_calculation_data:
            QMessageBox.warning(self, "No Base Network", "Please calculate an IPv4 base network first.")
            return

        base_network = self.last_calculation_data["network_address"]
        base_prefix = int(self.last_calculation_data["cidr_prefix"].replace('/', ''))
        
        new_prefix_str = self.combo_new_prefix.currentText().replace('/', '')
        new_prefix = int(new_prefix_str)

        if new_prefix < base_prefix:
            QMessageBox.warning(self, "Invalid Prefix", f"New prefix (/{new_prefix}) must be larger than or equal to base network prefix (/{base_prefix}).")
            return

        try:
            # We don't want to overflow the UI if they request a huge subnet division (e.g. /16 to /32 is 65536 subnets)
            # Limit display to max 1024 subnets for application stability
            if new_prefix - base_prefix > 10:
                # Ask confirmation since it generates 1024+ subnets
                num_subnets = 2**(new_prefix - base_prefix)
                reply = QMessageBox.question(
                    self, "Large Subnet Count",
                    f"This will generate {num_subnets} subnets, which might cause the UI to freeze temporarily.\nDo you want to continue?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if reply == QMessageBox.No:
                    return

            res = subnet_ipv4(f"{base_network}/{base_prefix}", new_prefix)
            
            # Save subnetting data into active calculation record
            self.last_calculation_data["subnets"] = res["subnets"]
            
            self.lbl_sub_info.setText(
                f"Original Network: {res['original_network']}  |  New Prefix: {res['new_prefix']}\n"
                f"Number of Subnets: {format_number(res['number_of_subnets'])}  |  "
                f"Addresses/Subnet: {format_number(res['addresses_per_subnet'])}  |  "
                f"Usable/Subnet: {format_number(res['usable_hosts'])}"
            )

            # Populate subnet table
            self.subnet_table.populate(res["subnets"])
        except Exception as e:
            QMessageBox.critical(self, "Subnetting Error", f"Failed to compute subnets: {str(e)}")

    def clear_fields(self):
        self.ip_input.clear()
        self.device_input.clear()
        self.card_basic.clear_vals()
        self.card_class.clear_vals()
        self.lbl_bin_ip.setText("IP Address: -")
        self.lbl_bin_bits.setText("Binary: -")
        self.lbl_bin_sep.setText("Network Bits | Host Bits:\n-")
        self.subnet_table.clear_table()
        self.lbl_sub_info.setText("Subnet Information: -")
        self.last_calculation_data = {}

    def copy_result(self):
        if not self.last_calculation_data:
            QMessageBox.warning(self, "No Result", "No calculation results to copy.")
            return

        try:
            txt = format_to_txt(self.last_calculation_data)
            QApplication.clipboard().setText(txt)
            QMessageBox.information(self, "Copied", "Subnet calculation results copied to clipboard.")
        except Exception as e:
            QMessageBox.critical(self, "Clipboard Error", f"Could not copy to clipboard: {str(e)}")

    def save_txt_result(self):
        if not self.last_calculation_data:
            QMessageBox.warning(self, "No Result", "No calculation results to save.")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Save TXT Result", "", "Text Files (*.txt)")
        if file_path:
            try:
                txt = format_to_txt(self.last_calculation_data)
                with open(file_path, "w") as f:
                    f.write(txt)
                QMessageBox.information(self, "Saved", "Result saved successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Save Error", f"Could not save file: {str(e)}")

    def save_json_result(self):
        if not self.last_calculation_data:
            QMessageBox.warning(self, "No Result", "No calculation results to export.")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Export JSON Result", "", "JSON Files (*.json)")
        if file_path:
            try:
                json_str = format_to_json(self.last_calculation_data)
                with open(file_path, "w") as f:
                    f.write(json_str)
                QMessageBox.information(self, "Exported", "Result exported successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Export Error", f"Could not export file: {str(e)}")

    def load_history_item(self, item):
        text = item.text()
        # format: "192.168.1.0/24 (IPv4)"
        if " (" in text:
            input_val, type_part = text.rsplit(" (", 1)
            type_val = type_part.replace(")", "")
            self.ip_input.setText(input_val)
            self.type_combo.setCurrentText(type_val)
            self.calculate()

    def delete_selected_history(self):
        selected = self.history_widget.currentRow()
        if selected >= 0:
            self.history_list_data.pop(selected)
            self.save_history()
            self.update_history_widget()

    def clear_all_history(self):
        self.history_list_data = []
        self.save_history()
        self.update_history_widget()

    def show_shortcuts(self):
        shortcuts_msg = (
            "Keyboard Shortcuts:\n\n"
            "Ctrl + Enter\t: Calculate Subnet\n"
            "Ctrl + L\t: Clear Input Fields\n"
            "Ctrl + C\t: Copy Result\n"
            "Ctrl + S\t: Save Result as TXT\n"
            "Ctrl + H\t: Toggle History Panel\n"
            "Ctrl + Q\t: Quit Application\n"
        )
        QMessageBox.information(self, "Keyboard Shortcuts", shortcuts_msg)

    def show_about(self):
        about_msg = (
            "Simple Subnet Calculator\n"
            "IPv4 / IPv6 / CIDR Network Calculator\n\n"
            "Version: 1.0.0\n"
            "Built with Python + PySide6\n\n"
            "A lightweight offline subnet calculator\n"
            "for networking and educational purposes."
        )
        QMessageBox.information(self, "About App", about_msg)
