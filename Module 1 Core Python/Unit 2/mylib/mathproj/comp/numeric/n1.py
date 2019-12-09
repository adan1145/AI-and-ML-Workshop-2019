#from mathproj import version
#from mathproj.comp import c1
#from mathproj.comp.numeric.n2 import h
#from .n2 import h
from ... import version
from .. import c1
from . n2 import h

def g():
    print("version is", version)
    print(h())
