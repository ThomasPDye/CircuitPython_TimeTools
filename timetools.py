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

.. todo:: Add links to any specific hardware product page(s), or category page(s).
  Use unordered list & hyperlink rST inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

* Adafruit's NTP library: https://github.com/adafruit/Adafruit_CircuitPython_NTP
"""

# imports

import time

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/ThomasPDye/CircuitPython_TimeTools.git"


def struct_time_equivalent(time_a: time.struct_time, time_b: time.struct_time):
    """compare time_a and time_b for equivalence taking into account unknowns"""
    for i in range(len(time.struct_time)):
        member_a, member_b = time_a[i], time_b[i]
        if member_a != member_b and (member_a != -1 or member_b != -1):
            return False
    return True
