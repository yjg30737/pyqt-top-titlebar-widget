# pyqt-top-titlebar-widget
PyQt top title bar widget for frameless window

## Requirements
* PyQt5 >= 5.15

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-top-titlebar-widget.git --upgrade```

## Imported Packages
* <a href="https://github.com/yjg30737/python-color-getter.git">python-color-getter</a>
* <a href="https://github.com/yjg30737/pyqt-svg-icon-text-widget.git">pyqt-svg-icon-text-widget</a>
* <a href="https://github.com/yjg30737/pyqt-windows-min-max-close-buttons-widget.git">pyqt-windows-min-max-close-buttons-widget</a>
* <a href="https://github.com/yjg30737/pyqt-mac-min-max-close-buttons-widget.git">pyqt-mac-min-max-close-buttons-widget</a>

## Detailed Description
This package is made for <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>'s title bar part.

## Usage
* ```TopTitleBarWidget(base_widget: QWidget, text: str = '', font: QFont = QFont('Arial', 12), icon_filename: str = None, align=Qt.AlignCenter)``` - Constructor
* ```setButtons(hint, style)``` - Set hint and style of buttons. Three hints are valid(Qt.WindowCloseButtonHint, Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint, Qt.WindowMinMaxCloseButton | Qt.WindowCloseButtonHint),  Two styles are valid(```'Windows'```, ```'Mac'```). 
* ```getIconTitleWidget() -> SvgIconTextWidget(QWidget)``` - Get icon and title widget
* ```getIconLbl() -> QLabel``` - Get icon label
* ```getTitleLbl() -> QLabel``` - Get title label
* ```getBtnWidget() -> MinMaxCloseButtonsWidget``` - Get buttons widget

## Note
If something goes wrong about this please contact me. 

I had accidentally done all procedure from ```git init``` to ```git push``` in wrong directory so i fixed it. 

But i don't know what kind of hidden impacts will occur. 

I don't want to delete the whole online repository by this, because i believe that deleting repository caused bad influence. 

It's just a hunch, though.

<hr>

Current version(v0.0.1) supports Windows 10 OS style only.
