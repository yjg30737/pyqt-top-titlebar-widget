import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QFont, QColor
from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel, QFrame
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
        self.__separator = QFrame()

    def __initUi(self, text: str, font: QFont = QFont('Arial', 12), icon_filename: str = None, align=Qt.AlignCenter):
        self.__svgIconTitleWidget = SvgIconTextWidget()

        self.__iconLbl = self.__svgIconTitleWidget.getSvgLabel()
        self.__titleLbl = self.__svgIconTitleWidget.getTextLabel()

        self.__filename_ext = os.path.splitext(icon_filename)[-1]
        if icon_filename:
            self.__svgIconTitleWidget.setSvgFile(icon_filename)
        else:
            self.__iconLbl.setVisible(False)
        self.__svgIconTitleWidget.setText(text)

        self.__titleLbl.setFont(font)

        self.__baseWidgetColor = self.__baseWidget.palette().color(QPalette.Base)

        self.__titleLblColor = QColor(self.__baseWidgetColor.red() ^ 255,
                                      self.__baseWidgetColor.green() ^ 255,
                                      self.__baseWidgetColor.blue() ^ 255)

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

    def setButtons(self, btnWidget, align=Qt.AlignRight):
        lay = self.layout()
        self.__btnWidget = btnWidget
        self.__btnWidget.setFont(self.__titleLbl.font())
        if align == Qt.AlignRight:
            lay.addWidget(self.__btnWidget, 0, 1, 1, 1, alignment=align)
        elif align == Qt.AlignLeft:
            lay.addWidget(self.__btnWidget, 0, 0, 1, 1, alignment=align)

    def setBottomSeparator(self):
        lay = self.layout()
        self.__separator.setFrameShape(QFrame.HLine)
        self.__separator.setFrameShadow(QFrame.Sunken)
        lay.addWidget(self.__separator, 1, 0, 1, 2)

    def getIconTitleWidget(self):
        return self.__svgIconTitleWidget

    def getIconLbl(self):
        return self.__iconLbl

    def getTitleLbl(self):
        return self.__titleLbl

    def getBtnWidget(self):
        return self.__btnWidget