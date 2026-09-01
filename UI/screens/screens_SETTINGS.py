# Kancil UI
#
# Copyright (C) 2026 Muhammad El Fatir
# SPDX-License-Identifier: GPL-3.0-or-later

# For now, this is just a general mockup of where things should be.
# Most (if not all) functions don't really work yet.
# When this placeholder is removed, that means it's ready for prod.

from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical, Container
from textual.widgets import Label, Button, Digits, Static, Input

ASCII_LOGO = f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⠠⠀⠀⠀⡠⢐⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠢⠈⠠⡠⢂⠑⠈⠀⡊
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡠⢄⠢⠨⢐⠨⠐⢈⠀⡁⠢
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⢕⢡⢱⠰⠡⡑⠄⢅⠑⠄⠄⡂⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢢⠣⢑⠨⠨⡂⢅⠑⢄⢑⠄⠅⢅⢑⠠
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢆⢣⠑⠄⠅⡑⠌⠄⢅⠑⠄⠅⢅⠑⠄⠅⠅
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⢜⢜⠨⠀⠀⠠⠡⡑⠄⠅⠅⢕⠐⠅⠅⢕
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢜⠐⠌⠢⠠⡈⠢⠨⠨⡈⠪⠠⠡⠡⡑⠐
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⠡⠡⠡⡑⠌⠌⠌⠌⠌⠌⠌⢌⢌⠠
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡊⠌⠌⢌⠢⠨⠨⠨⠨⡊⠌⢌⢊⢂⠢⡈
⠀⠀⢔⢔⠑⠅⢅⢕⢔⠷⢗⢎⣆⠳⡵⡦⡄⣢⠠⡁⣤⣡⣅⡁⡁⠅⡐⠨⡐⡐⢄⢑⠐
⠀⢄⠕⠄⢅⣕⢗⣇⢏⣻⡑⢅⣥⣑⠲⢨⣦⣪⡂⡪⠭⡑⡑⡐⠌⠢⡈⡂⡢⡈⡂⡂⡂
⡐⢅⢅⢃⠢⢑⢐⠐⢍⠑⢌⠢⡉⡋⡣⢑⠌⢌⠑⢌⢂⢂⠢⠨⡈⡂⡂⡂⡂⡂⡂⠢⡇
⠀⠀⠀⡂⡑⡐⠄⠕⢄⢑⢄⢑⢐⠐⢌⠐⢌⢂⢑⢐⠐⠄⢅⢑⢐⢐⠌⡂⡂⡂⡪⢸⡇
⠀⠀⠨⡐⡐⠌⠌⢌⢂⢂⢂⢂⠢⡑⠄⢕⢐⢐⢐⠄⠅⢅⢑⢐⢐⢄⢑⢐⢐⢐⠌⣾⡅
⠀⠀⠀⠢⠨⠨⡈⣂⠢⡂⡂⡢⡁⠢⡑⡐⡐⠐⡠⠡⠡⡑⡐⡐⡐⡐⡐⡐⡐⢄⣽⣗⠁
⠀⠀⠀⠡⠡⡑⡸⢐⢕⢜⢜⢔⢌⣆⣂⡂⡀⡂⠌⢌⢂⢂⢂⡂⡪⡐⣐⣌⣼⡽⣾⠁
⠀⠀⡀⠁⢅⠢⢑⢸⢨⢪⢪⠪⡪⡻⢽⠮⡇⢇⢑⢐⠐⢔⠕⡔⣕⣯⢷⣻⣾⠛⠁
⠀⠀⠄⠨⢐⢈⢂⠪⡪⠊⡀⢁⠁⡁⠃⠃⠣⠃⡂⠢⠡⡑⢅⠳⡻⠺⠛⠉⢄
⠀⠀⠂⡈⡂⡂⠢⡑⠌⠀⠄⠠⠀⡀⠀⠀⠀⠀⠨⡈⠢⡈⡢⡃⠀⢂⠈⢐⠐
⠀⠀⠀⠄⠢⡈⡂⡪⢀⠡⠐⠀⡁⠀⠀⠀⠀⠀⠀⠈⡂⡂⡎⠆⠁⠠⠐⢐
⠀⠀⠀⠀⠡⡂⡂⡇⠀⠐⠈⠠⠈⠀⠀⠀⠀⠀⠀⠀⢂⠂⡇⡅⠀⢂⠈⡐⡀
⠀⠀⠀⠀⢁⠢⢸⠀⠀⢀⠁⠨⠀⠀⠀⠀⠀⠀⠀⠀⢀⢑⢸⠀⠀⠠⠀⠂⠄
⠀⠀⠀⠀⠀⠊⠜⠀⠀⠀⠀⡁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠐⠈⠂⠀⠀⠈⠈⠀⠄
⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠄⠈⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠁⠀⠀⠐⠀⠐
"""

class SettingScreen(Screen):
    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical():
                yield Label(" Set your infos here!")

                yield Input(placeholder="Type your name here ")
                yield Input(placeholder="Type your institution here ")
                yield Input(placeholder="Type your current class here 󰑴")
                yield Input(placeholder="Type your phone number here ")

                with Horizontal():
                    yield Button("Save", variant="success", id="button_SAVE")
                    yield Button("󰈆 Exit", variant="error", id="button_EXIT")

            with Vertical():
                yield Label(ASCII_LOGO)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "button_EXIT":
            self.app.pop_screen()