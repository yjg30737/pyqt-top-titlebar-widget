import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QFont, QIcon, QPixmap, QColor
from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel

from pyqt_windows_min_max_close_buttons_widget import WindowsMinMaxCloseButtonsWidget
from pyqt_mac_min_max_close_buttons_widget import MacMinMaxCloseButtonsWidget

from python_color_getter.pythonColorGetter import PythonColorGetter
from pyqt_svg_icon_text_widget.svgIconTextWidget import SvgIconTextWidget


class TopTitleBarWidget(QWidget):
    def __init__(self, base_widget: QWidget, text: str = '', font: QFont = QFont('Arial', 12),
                 icon_filename: str = None,
                 align=Qt.AlignCenter):
        super().__init__()
        self.__baseWidget = base_widget
        self.__initVal()
        self.__initUi(text=text, font=font, icon_filename=icon_filename, align=align)

    def __initVal(self):
        self.__svgIconTitleWidget = ''
        self.__iconLbl = QLabel()
        self.__titleLbl = QLabel()
        self.__btnWidget = ''

    def __initUi(self, text: str, font: QFont = QFont('Arial', 12), icon_filename: str = None, align=Qt.AlignCenter):
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

        self.__baseWidgetColor = self.__baseWidget.palette().color(QPalette.Base)

        title_lbl_r, title_lbl_g, title_lbl_b = PythonColorGetter.get_complementary_color(self.__baseWidgetColor.red(),
                                                                                          self.__baseWidgetColor.green(),
                                                                                          self.__baseWidgetColor.blue())
        self.__titleLblColor = QColor(title_lbl_r, title_lbl_g, title_lbl_b)

        self.setObjectName('topTitleBar')
        self.setStyleSheet(f'''
                            QWidget 
                            {{ 
                            background-color: {self.__baseWidgetColor.name()};
                            }}
                            QLabel
                            {{
                            color: {self.__titleLblColor.name()};
                            }}
                            '''
                           )

        self.setMinimumHeight(self.__titleLbl.fontMetrics().height())

        lay = self.__svgIconTitleWidget.layout()
        lay.setContentsMargins(0, 0, 0, 0)

        lay = QGridLayout()
        lay.addWidget(self.__svgIconTitleWidget, 0, 0, 1, 2, alignment=align)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)

    def setButtons(self, hint, style):
        lay = self.layout()
        if style == 'Windows':
            self.__btnWidget = WindowsMinMaxCloseButtonsWidget(base_widget=self.__baseWidget, hint=hint, font=self.__titleLbl.font())
            lay.addWidget(self.__btnWidget, 0, 1, 1, 1, alignment=Qt.AlignRight)
        elif style == 'Mac':
            self.__btnWidget = MacMinMaxCloseButtonsWidget(hint=hint)
            lay.addWidget(self.__btnWidget, 0, 0, 1, 3, alignment=Qt.AlignLeft)
            lay.addWidget(self.__svgIconTitleWidget, 0, 2, 1, 3)

    def getIconTitleWidget(self):
        return self.__svgIconTitleWidget

    def getIconLbl(self):
        return self.__iconLbl

    def getTitleLbl(self):
        return self.__titleLbl

    def getBtnWidget(self):
        return self.__btnWidget