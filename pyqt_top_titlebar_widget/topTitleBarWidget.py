import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QFont, QIcon, QPixmap, QColor
from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel, QMenuBar

from pyqt_windows_min_max_close_buttons_widget import WindowsMinMaxCloseButtonsWidget
from pyqt_mac_min_max_close_buttons_widget import MacMinMaxCloseButtonsWidget

from python_color_getter.pythonColorGetter import PythonColorGetter
from pyqt_svg_icon_text_widget.svgIconTextWidget import SvgIconTextWidget


class TopTitleBarWidget(QWidget):
    def __init__(self, menu_bar: QMenuBar, text: str = '', font: QFont = QFont('Arial', 12), icon_filename: str = None,
                 align=Qt.AlignCenter, hint=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint):
        super().__init__()
        self.__menuBar = menu_bar
        self.__initVal()
        self.__initUi(text=text, font=font, icon_filename=icon_filename, align=align, hint=hint)

    def __initVal(self):
        self.__svgIconTitleWidget = ''
        self.__iconLbl = QLabel()
        self.__titleLbl = QLabel()
        self.__btnWidget = ''

    def __initUi(self, text: str, font: QFont = QFont('Arial', 12), icon_filename: str = None, align=Qt.AlignCenter,
                 hint=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint):
        self.__svgIconTitleWidget = SvgIconTextWidget()

        self.__iconLbl = self.__svgIconTitleWidget.getSvgLabel()
        self.__titleLbl = self.__svgIconTitleWidget.getTextLabel()

        self.__filename_ext = os.path.splitext(icon_filename)[-1]
        if icon_filename:
            if self.__filename_ext == '.svg':
                self.__svgIconTitleWidget.setSvgFile(icon_filename)
            else:
                icon = QIcon(icon_filename)
                self.setWindowIcon(icon)
                icon_size = font.pointSize()
                icon = icon.pixmap(icon_size * 1.5, icon_size * 1.5)
                pixmap = QPixmap(icon)
                self.__windowTitleIconLabel.setPixmap(pixmap)
                self.__windowTitleIconLabel.setMaximumWidth(pixmap.width())
        else:
            self.__iconLbl.setVisible(False)
        self.__svgIconTitleWidget.setText(text)

        self.__titleLbl.setFont(font)

        menubar_base_color = self.__menuBar.palette().color(QPalette.Base)

        title_lbl_r, title_lbl_g, title_lbl_b = PythonColorGetter.get_complementary_color(menubar_base_color.red(),
                                                                                          menubar_base_color.green(),
                                                                                          menubar_base_color.blue())
        title_lbl_color = QColor(title_lbl_r, title_lbl_g, title_lbl_b)

        self.__btnWidget = WindowsMinMaxCloseButtonsWidget(menu_bar=self.__menuBar, hint=hint)
        self.__btnWidget.raise_()

        self.setObjectName('topTitleBar')
        self.setStyleSheet(f'''
                            QWidget 
                            {{ 
                            background-color: {menubar_base_color.name()};
                            }}
                            QLabel
                            {{
                            color: {title_lbl_color.name()};
                            }}
                            '''
                           )
        self.setMinimumHeight(self.__titleLbl.fontMetrics().height())

        lay = self.__svgIconTitleWidget.layout()
        lay.setContentsMargins(0, 0, 0, 0)

        lay = QGridLayout()
        lay.addWidget(self.__svgIconTitleWidget, 0, 0, 1, 2, alignment=align)
        lay.addWidget(self.__btnWidget, 0, 1, 1, 1, alignment=Qt.AlignRight)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)

    def getIconTitleWidget(self):
        return self.__svgIconTitleWidget

    def getIconLbl(self):
        return self.__iconLbl

    def getTitleLbl(self):
        return self.__titleLbl

    def getBtnWidget(self):
        return self.__btnWidget