# Kancil UI
#
# Copyright (C) 2026 Muhammad El Fatir
# SPDX-License-Identifier: GPL-3.0-or-later

from textual.app import App

from screens.screens_HOME import HomeScreen
from screens.screens_SETTINGS import SettingScreen

class KancilUI(App):
    def on_mount(self):
        self.theme = "textual-light"

        self.install_screen(HomeScreen(), "home")
        self.install_screen(SettingScreen(), "settings")
        self.push_screen("home")