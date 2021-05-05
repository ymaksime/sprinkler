#!/usr/bin/env python3

from gpiozero import OutputDevice

class PowerSupply:
    """This Class describes the power supply used for the sprinkler system.
    This information can be used to check the compatibility with the overall
    system.  It is assumed that Raspeberry Pi would have a way to control the
    power supply.
    """

    models = [
            {'model': 'HS-AC024V750', 'brand': 'Orbit', \
                    'input':{'volt': 120, 'watt': 24}, \
                    'output':{'volt': 24, 'current': 750}}
            ]

    def __init__(self, model, gpioPort):
        self.specifications = next((specs for specs in self.models if \
                specs["model"] == model), None)
        assert self.specifications != None, "No such power supply model exist"
        self.line = OutputDevice(gpioPort)

    def on(self):
        """Turns ON the power supply"""
        self.line.on()

    def off(self):
        """Turns OFF the power supply"""
        self.line.off()

    def is_active(self):
        """Verifies if the power supply is currently ON"""
        return self.line.value == 1

    def info_max_out_current(self):
        """Returns the maximum output current the power supply can deliver"""
        return self.specifications['output']['current']

    def info(self):
        """Prints out the hardware characteristics for the power supply"""
        print(self.specifications)
