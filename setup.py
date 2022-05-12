from setuptools import setup, find_packages

setup(
    name='pyqt-top-titlebar-widget',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt top title bar widget for frameless window',
    url='https://github.com/yjg30737/pyqt-top-titlebar-widget.git',
    install_requires=[
        'PyQt5>=5.15',
        'python-color-getter>=0.0.1',
        'pyqt-windows-buttons-widget>=0.0.1',
        'pyqt-mac-min-max-close-buttons-widget @ git+https://git@github.com/yjg30737/pyqt-mac-min-max-close-buttons-widget.git@main',
        'pyqt-svg-icon-text-widget>=0.0.1'
    ]
)