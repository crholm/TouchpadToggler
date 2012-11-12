"""
AUTHOR
    Artur Barseghyan.

LICENSE
    GNU GPL

DESCRIPTION
    Enables/disables xinput devices.

    First argument represents device state (0 for disable and 1 for enable). Second argument represents device name.

    By default we operate with "Synaptics TouchPad" but it's possible to have custom device names.

INSTALLATION
    Copy the file "operate_xinput_device.py" to ~/.scripts/ directory (make sure to create one first).

USAGE EXAMPLES
    In terminal type:
        python ~/.scripts/operate_xinput_device.py 1 Synaptic TouchPad # Enable "Synaptic TouchPad"
        python ~/.scripts/operate_xinput_device.py 0 Genius Optical Mouse # Disable "Genius Optical Mouse"

    If you wish, you can edit your .bashrc file and add shortcuts:
        alias disable_touchpad='python ~/.scripts/operate_xinput_device.py 0 Synaptics TouchPad'
        alias enable_touchpad='python ~/.scripts/operate_xinput_device.py 1 Synaptics TouchPad'
"""

import os
import re
import sys
import getopt

MODE_ENABLE = '1'
MODE_DISABLE = '0'
DEFAULT_MODE = MODE_DISABLE

DEVICE_NAME_SYNAPTIC = 'Synaptics TouchPad'
DEFAULT_DEVICE_NAME = DEVICE_NAME_SYNAPTIC

def operate_xinput_device(mode=None, device_name=None):
    """
        Operates touchpad.
        @param str mode
        @param str device_name
    """
    if not mode in (MODE_ENABLE, MODE_DISABLE):
        mode = DEFAULT_MODE
    if not device_name:
        device_name = DEFAULT_DEVICE_NAME
    try:
        # We simply rely on "xinput" command. We grep "Synaptics TouchPad" word there.
        shell_response = os.popen('xinput list | grep "%s"' % str(device_name)).read()
        # RegEx to grab device ID        
        regex = re.compile('id=(?P<line>\d+)', re.IGNORECASE)
        # Grab device ID. If any errors occur, device name is invalid (no such device).        
        try:
            touchpad_id = regex.findall(shell_response)[0]
        except Exception, e:
            raise Exception('No such device "%s". Type "xinput list" in terminal to see the list of available devices.' % str(device_name))
        # Our command to enable/disable device.        
        os.system('xinput set-prop %s "Device Enabled" %s' % (touchpad_id, str(mode)))
    except Exception, e:
        print e

def main():
    # Parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # Process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    # Process arguments
    try:
        mode = args[0]
    except Exception, e:
        mode = None
    try:
        device_name = ' '.join(args[1:])
    except Exception, e:
        device_name = None
    
    operate_xinput_device(mode, device_name)

if __name__ == "__main__":
    main()
