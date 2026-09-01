# Kancil UI
#
# Copyright (C) 2026 Muhammad El Fatir
# SPDX-License-Identifier: GPL-3.0-or-later

from datetime import datetime

def get_suffix(n):
    if 11 <= n % 100 <= 13:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

def get_datetime():
    now = datetime.now()
    day = now.day
    suffix = get_suffix(day)
    return (
        now.strftime("%H:%M:%S"),
        now.strftime(f"Today is %A, {day}{suffix} %B of %Y"),
    )