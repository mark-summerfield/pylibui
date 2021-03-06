"""
 Python wrapper for libui.

"""

from pylibui import libui


class Control:

    def __init__(self, control=None):
        """
        Creates a new Control.

        """
        self.control = control

    def pointer(self):
        """
        Returns this control as ui pointer.

        :return: uiControl ctype pointer
        """
        return libui.uiControlPointer(self.control)

    def show(self):
        """
        Shows the control.

        :return: None
        """
        libui.uiControlShow(self.pointer())

    def destroy(self):
        """
        Destroys the control.

        :return: None
        """
        libui.uiControlDestroy(self.pointer())

