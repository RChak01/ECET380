import pyvisa as visa
import numpy as np
import time
import matplotlib.pyplot as plt
from tme import device_addresses
from power_supply_library import power_supply
from dmm import dmm
from waveform import wave
from scope import scope


devices = device_addresses()
rm=visa.ResourceManager()
wave_add = devices.wfg_address
wave = wave(rm, wave_add)
scope_add = devices.scope_address
scope = scope(rm, scope_add)

wave.connect()
scope.connect()
# Automated Replacement
wave.high_z()
wave.square_wave()
wave.output(1)
scope.channel("on", 2)
scope.channel("on", 1)
scope.run()
scope.autoscale()
# Burst Section
wave.output(1)
time.sleep(5)
wave.output(0)
wave.burst_characteristics()
scope.single()
wave.trigger()
wave.output(1)