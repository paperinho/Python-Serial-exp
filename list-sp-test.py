#! /d/Python/Python37/python
import serial.tools.list_ports
print(list(serial.tools.list_ports.comports()))