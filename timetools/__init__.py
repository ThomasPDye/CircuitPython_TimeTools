# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2024 Thomas Dye
#
# SPDX-License-Identifier: MIT
"""
`timetools`
================================================================================

A CircuitPython library of tools to work with time


* Author(s): Thomas Dye

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

* Adafruit's NTP library: https://github.com/adafruit/Adafruit_CircuitPython_NTP
"""

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/ThomasPDye/CircuitPython_TimeTools.git"

from .comparisons import struct_time_equivalent
