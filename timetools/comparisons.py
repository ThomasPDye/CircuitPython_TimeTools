# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2024 Thomas Dye
#
# SPDX-License-Identifier: MIT

"""
`timetools.comparisons`
"""

import time


def struct_time_equivalent(time_a: time.struct_time, time_b: time.struct_time):
    """compare time_a and time_b for equivalence taking into account unknowns"""
    for i in range(len(time.struct_time)):
        member_a, member_b = time_a[i], time_b[i]
        if member_a != member_b and member_a != -1 and member_b != -1:
            return False
    return True
