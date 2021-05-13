#!/usr/bin/env python3

import logging
from gpiozero import OutputDevice, LED

valve_logger = logging.getLogger('Valve')

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
    def __init__(self, model, valveGpioPort, ledGpioPort, name):
        self.specifications = next((specs for specs in self.models if specs["model"] == model), None)
        assert self.specifications != None, "No such sprinkler model exist"
        self.line = OutputDevice(valveGpioPort)
        self.led = LED(ledGpioPort)
        self.name = name
        valve_logger.debug('Created %s valve', self.name)
        valve_logger.debug('valve gpio: %s, led gpio: %s', self.line, self.led)
        self.info()

    def on(self):
        """Turns ON this valve"""
        self.line.on()
        self.led.on()
        valve_logger.info('Turned ON the %s valve', self.name)

    def off(self):
        """Turns OFF this valve"""
        self.line.off()
        self.led.off()
        valve_logger.info('Turned OFF the %s valve', self.name)

    def is_active(self):
        """Verifies if the valve is currently ON"""
        return self.line.value == 1

    def info_max_current(self):
        """Maximum current required for operation"""
        return self.specifications['mAcurrent']

    def info(self):
        """Prints out the hardware characteristics of the current valve"""
        valve_logger.info(self.specifications)
