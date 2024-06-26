# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2024 Thomas Dye
#
# SPDX-License-Identifier: Unlicense

from rtc import RTC
from socketpool import SocketPool
import wifi

from adafruit_ntp import NTP

from timetools import struct_time_equivalent

pool = SocketPool(wifi.radio)
ntp = NTP(pool, tz_offset=0)
rtc = RTC()

if struct_time_equivalent(ntp.datetime, rtc.datetime):
    print("RTC in sync with NTP")
else:
    print("RTC not in sync with NTP")
