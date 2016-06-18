Setup
======

yocto library
--------------

yocto relay source files need to be on python path
In this case I copied yocto_api.py, yocto_relay and the cdll dir from YoctoLib.python.24182/Source to 
a dir called "yocto")

In line 42 of yocto_relay.py changed
from yocto_api import *
to
from .yocto_api import *
