# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2024 Thomas Dye
#
# SPDX-License-Identifier: Unlicense

import time

from rtc import RTC
from socketpool import SocketPool
import wifi

from adafruit_ntp import NTP

from timetools import struct_time_equivalent

pool = SocketPool(wifi.radio)
ntp = NTP(pool, tz_offset=0)
rtc = RTC()

while True:
    if not struct_time_equivalent(rtc.datetime, ntp.datetime):
        rtc.datetime = ntp.datetime
        print("Updating RTC")
    time.sleep(1)
