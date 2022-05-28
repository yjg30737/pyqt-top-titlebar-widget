# pyqt-top-titlebar-widget
PyQt top title bar widget for frameless window

This package is made for <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>'s title bar part. You can see the preview of this in the documentation at the link.

I don't recommend that you use this on your own class, But if you want to do it, try it and please teach me that it works well or not.

## Requirements
* PyQt5 >= 5.15

## Setup
`python -m pip install pyqt-top-titlebar-widget`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-svg-icon-text-widget.git">pyqt-svg-icon-text-widget</a>

## Methods Overview
* `TopTitleBarWidget(base_widget: QWidget, text: str = '', font: QFont = QFont('Arial', 14), icon_filename: str = None, align=Qt.AlignCenter)` - Constructor
* `setButtons(btnWidget, align=Qt.AlignRight)` - Set button widget(<a href="https://github.com/yjg30737/pyqt-titlebar-buttons-widget.git">pyqt-titlebar-buttons-widget</a>). `align` is to set alignment of buttons widget. Size of `font` should be at least 14. 
* `setBottomSeparator()` - Set the `QFrame` type horizontal line separator which is used for the border between title bar and menu bar.
* `getIconTitleWidget() -> SvgIconTextWidget(QWidget)` - Get icon and title widget
* `getIconLbl() -> QLabel` - Get icon label
* `getTitleLbl() -> QLabel` - Get title label
* `getBtnWidget() -> TitleBarButtonsWidget` - Get buttons widget
