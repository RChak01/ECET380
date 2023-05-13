import pyvisa as visa
import numpy as np
import time
import matplotlib.pyplot as plt
from tme import device_addresses
from power_supply_library import power_supply
from dmm import dmm

# devices = device_addresses()
# rm=visa.ResourceManager()
# dmm_add = devices.dmm_address
# dmm_dev = dmm(rm, dmm_add)
# dmm_dev.connect()
# dmm_dev.single_or_dual(1, "VOLT:DC", "CURR:DC")
# dmm_dev.identity()


