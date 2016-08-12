import os, sys
from yocto.yocto_api import *
from yocto.yocto_relay import *


def relay_control(target, channel): #, state
    """
    taget is logical name of relay or factory serial number
    channel - 1 or 2 as a string
    state - A or B
    """
    # Setup the API to use local USB devices
    errmsg=YRefParam()
    if YAPI.RegisterHub("usb", errmsg)== YAPI.SUCCESS:
        relay = YRelay.FirstRelay()
        # check that any relay is connected, in case I pass the
        # wrong logical name or something.
        if relay is None : 
            return 'No module connected'
        else:
            m=relay.get_module()
            if channel < '3': 
                # activate 1 to open or 2 to close      
                relay = YRelay.FindRelay(target + '.relay'+ channel)
                # relay.maxTimeOnStateB = 500
                """
                if state == 'A' :
                    relay.set_state(YRelay.STATE_A)
                else:
                    relay.set_output(YRelay.STATE_B)
                """
                relay.set_pulseTimer(500)
                return "Last action was: " + channel
            else:
                # pulse both to stop
                relay1 = YRelay.FindRelay(target + '.relay1')
                relay2 = YRelay.FindRelay(target + '.relay2')
                relay1.set_pulseTimer(500)
                relay2.set_pulseTimer(500)
                return "Last action was Stop "
    else:
        return "init error" + errmsg.value


