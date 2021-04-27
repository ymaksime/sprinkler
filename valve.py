#!/usr/bin/env python

from gpiozero import OutputDevice

class Valve:
    """This is a class for a single inline valve and all associated hardware
    around it such as LEDs, etc.
    Along with all necessary methods it should store some hardware
    specifications such as pipe diameter, operational AC current, etc.
    """
    models = [
            {'model': 'CP075', 'brand': 'RainBird', 'thread': 0.75, 'acVolt': 24, 'mAcurrent': 250},
            {'model': 'CPF075', 'brand': 'RainBird', 'thread': 0.75, 'acVolt': 24, 'mAcurrent': 300}
            ]
    def __init__(self, model, gpioPort):
        self.specifications = next((specs for specs in self.models if specs["model"] == model), None)
        assert self.specifications != None, "No such sprinkler model exist"
        self.line = OutputDevice(gpioPort)

    def on(self):
        """Turns ON this valve"""
        self.line.on()

    def off(self):
        """Turns OFF this valve"""
        self.line.off()

    def is_active(self):
        """Verifies if the valve is currently ON"""
        return self.line.value == 1

    def info(self):
        """Prints out the hardware characteristics of the current valve"""
        print(self.specifications)
