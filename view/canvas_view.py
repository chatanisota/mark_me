from PyQt5.QtWidgets import QDialog, QLabel
from PyQt5.QtCore import Qt
from handler.handler import Handler

class CanvasView(QLabel):

    # singleton
    __instance = None

    __drag = False

    def __init__(self, parent=None):
        super(CanvasView, self).__init__(parent)
        self.setMouseTracking(True)

        if CanvasView.__instance == None:
            CanvasView.__instance = self

    def mousePressEvent(self, event):
        qrect = event.pos()
        Handler.canvas_mouse_press(qrect.x(), qrect.y())
        CanvasView.__drag = True

    def mouseMoveEvent(self, event):
        if CanvasView.__drag:
            qrect = event.pos()
            Handler.canvas_mouse_drag(qrect.x(), qrect.y())
        else:
            qrect = event.pos()
            Handler.canvas_mouse_move(qrect.x(), qrect.y())

    def mouseReleaseEvent(self, event):
        CanvasView.__drag = False
        if event.button() == Qt.RightButton:
            Handler.canvas_right_mouse_press()
        else:
            qrect = event.pos()
            Handler.canvas_mouse_release(qrect.x(), qrect.y())

    #def wheelEvent(self, event):
    #    Handler.canvas_mouse_wheel(event.angleDelta().y())

    @staticmethod
    def get_size():
        qrect = CanvasView.__instance.frameGeometry()
        return (qrect.width(), qrect.height())
