from src.capture import QtCapture
from src.control import ControlWindow
from src.exploration import explorationThread

import sys
from PyQt5.QtWidgets import QApplication



global pictureSaved
global taskReady
pictureSaved = None
taskReady = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ControlWindow()
    sys.exit(app.exec_())