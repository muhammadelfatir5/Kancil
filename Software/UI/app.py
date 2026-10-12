# Kancil UI
#
# Copyright (C) 2026 Muhammad El Fatir
# SPDX-License-Identifier: GPL-3.0-or-later
from pathlib import Path


from textual.app import App

from screens.HOME import HomeScreen
from screens.SETTINGS import SettingScreen
from screens.FIRST_INIT import InitScreen

class KancilUI(App):
    CONFIG_DIR = Path.home() / ".config" / "kancil"
    CONFIG_FILE = CONFIG_DIR / "config.toml"

    def on_mount(self):
        self.theme = "ansi-light"

        self.install_screen(HomeScreen(), "home")
        self.install_screen(SettingScreen(), "settings")
        self.install_screen(InitScreen(), "init")
        if self.CONFIG_FILE.exists():
            self.push_screen("home")
        else:
            self.push_screen("init")