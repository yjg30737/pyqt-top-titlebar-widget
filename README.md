# pyqt-top-titlebar-widget
PyQt top title bar widget for frameless window

This package is made for <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>'s title bar part. You can see the preview of this in the documentation at the link.

## Requirements
* PyQt5 >= 5.15

## Setup
`python -m pip install pyqt-top-titlebar-widget`

## Imported Packages
* <a href="https://github.com/yjg30737/python-color-getter.git">python-color-getter</a>
* <a href="https://github.com/yjg30737/pyqt-svg-icon-text-widget.git">pyqt-svg-icon-text-widget</a>
* <a href="https://github.com/yjg30737/pyqt-windows-buttons-widget.git">pyqt-windows-buttons-widget</a>
* <a href="https://github.com/yjg30737/pyqt-mac-buttons-widget.git">pyqt-mac-buttons-widget</a>

## Usage
* `TopTitleBarWidget(base_widget: QWidget, text: str = '', font: QFont = QFont('Arial', 12), icon_filename: str = None, align=Qt.AlignCenter)` - Constructor
* `setButtons(hint, style)` - Set hint and style of buttons. Currently three hints are valid(Qt.WindowCloseButtonHint, Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint, Qt.WindowMinMaxCloseButton | Qt.WindowCloseButtonHint),  Two styles are valid(```'Windows'```, ```'Mac'```).
* `setBottomSeparator()` - Set the `QFrame` type horizontal line separator which is used for the border between title bar and menu bar.
* `getIconTitleWidget() -> SvgIconTextWidget(QWidget)` - Get icon and title widget
* `getIconLbl() -> QLabel` - Get icon label
* `getTitleLbl() -> QLabel` - Get title label
* `getBtnWidget() -> TitleBarButtonsWidget` - Get buttons widget
