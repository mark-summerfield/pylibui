"""
 Python wrapper for libui.

"""

import ctypes
import os
import platform


if platform.system() == 'Darwin':
    libname = 'libui.dylib'
elif platform.system() == 'Windows':
    libname = 'libui.dll'
elif platform.system() == 'Linux':
    libname = 'libui.so'


CURR_PATH = os.path.dirname(os.path.realpath(__file__))
SHARED_LIBS_PATH = os.path.join(CURR_PATH, 'sharedlibs')
SHARED_LIBS = os.path.join(SHARED_LIBS_PATH, libname)


ctypes.cdll.LoadLibrary(SHARED_LIBS)
clibui = ctypes.CDLL(SHARED_LIBS)


from .box import *
from .control import *
from .label import *
from .main import *
from .window import *
