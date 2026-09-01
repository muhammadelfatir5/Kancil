# Kancil UI
#
# Copyright (C) 2026 Muhammad El Fatir
# SPDX-License-Identifier: GPL-3.0-or-later

# For now, this is just a general mockup of where things should be.
# Most (if not all) functions don't really work yet.

from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical, Container
from textual.widgets import Label, Button, Digits, Static

from utils.utils_DATETIME import get_datetime

# The idea is for these variables to be set on first start-up.
# Save it to a file and read it instead of having these be variables.
# Or, a more fun idea is to let students change these variables to fit their own infos and stuff.
username = "Fatir"
school = "SMK Telkom Jakarta"
current_class = "XI RPL 5"
phone_number = "+62-123-123-1234"

ASCII_LOGO = f"""⢀⠰⢠⢀⠀⠀⠄⢁⢀
⠢⠈⠐⠨⠢⢄⠂⠐⢄⢁           KANCIL
⡑⡀⠁⠄⠑⢄⠑⢄⠢⢄⠤⡀⡀        Owned By: {username}
⠐⢄⢈⠐⢅⠢⢑⢐⠘⢔⠥⡑⠕⡔⢄      {school}
⠀⢐⠠⡑⡐⠌⡂⠢⡑⠄⠅⢕⠑⢌⠪⡢⡀    {current_class}
⠨⡐⡐⡐⠌⠢⡈⡂⠢⠡⡑⠄⠑⠄⠅⡇⡇
⠐⢐⠐⠌⢌⢂⠢⠨⠨⠢⠨⡀⠀⠨⡈⢎⢎⢆   If found,
⠀⠠⠡⡑⡐⠄⠅⠅⢅⢅⢑⠐⠄⠢⡈⡂⠣⠃   please contact:
⠀⢐⢀⠢⠨⠨⠨⠨⡂⡂⠢⠡⠡⡑⡐⠌⢌    {phone_number}
⠀⠀⠐⠌⠌⠌⢌⢂⠢⠨⠨⠨⡂⠢⠨⡈⡂⠢⠠
⠀⠀⠁⠅⠅⢅⢑⠐⢄⠡⢁⢡⣨⣌⣌⢄⢀⡢⢰⢴⠮⡎⣪⡪⠾⢾⢰⡨⡨⡈⠪⢢⠢
⠀⠀⠠⠡⠡⡑⢄⢑⠐⢌⢂⠢⡈⠪⡩⢕⢐⣭⣢⡆⡓⣢⣬⢌⢙⣝⣕⣕⢗⣎⢌⠂⢇⢇
⠀⠀⢸⠨⡈⡂⡂⠢⡑⡐⡐⡐⢌⠢⡈⠢⠩⡈⡂⡃⡊⡋⡊⠢⠡⡉⠪⡐⡐⠌⡂⡑⢔⢑⠄
⠀⠀⢸⡕⡐⡐⢌⢂⢂⢂⠢⡈⡂⠢⠨⠨⡂⡂⡂⡂⡂⠪⠨⡈⡂⡊⡂⠢⡈⡂⠢⠠
⠀⠀⢸⣧⠢⡈⡂⡂⡂⡢⢑⠐⠌⠌⢌⢂⢂⠢⡈⡢⠨⠨⡂⡂⠢⠢⠨⡂⡂⠪⠨⠨⠂
⠀⠀⠈⣯⣧⡂⡂⡂⡢⡈⠢⠡⠡⠡⡑⡐⢄⠑⠐⠌⢌⢂⠢⠨⡨⠨⡢⡢⠨⠨⠨⡨
⠀⠀⠀⠐⣷⣻⣦⣂⡢⢨⠨⢨⠨⡈⠢⠨⡐⡈⡀⣑⣐⣤⡅⡇⡇⡳⡰⡘⢬⠨⡊⡐
⠀⠀⠀⠀⠀⠻⢾⡽⣯⡷⣝⢔⠱⡨⠨⡂⠢⢸⢸⢜⢷⢳⢣⢣⢱⢱⠱⡑⠌⡂⠢⠐⢀
⠀⠀⠀⠀⠀⠀⠌⢉⠛⠻⠽⢎⢊⢊⠢⠨⡈⠢⠃⠃⠃⢁⠡⠐⢀⠱⢱⠡⡑⠨⠨⡐
⠀⠀⠀⠀⠀⠀⠑⠠⠀⠡⠐⢘⠔⠄⢅⢑⠈⠀⠀⠀⠀⠀⠐⢈⠠⠐⢘⠔⡨⡈⡂⡂⠐
⠀⠀⠀⠀⠀⠀⠈⡂⢁⠐⠈⠘⡜⡈⡂⢂⠀⠀⠀⠀⠀⠈⡂⠠⠐⠀⠄⡇⡂⡂⠢⠐
⠀⠀⠀⠀⠀⠀⠀⡂⠄⠂⠁⢠⢣⠢⢈⠀⠀⠀⠀⠀⠀⠀⠠⠐⢈⠀⠂⢰⢐⠨⡈⠄
⠀⠀⠀⠀⠀⠀⠀⡂⢀⠁⠀⢸⢐⠅⠠⠀⠀⠀⠀⠀⠀⠀⠈⠂⡀⠂⠀⠀⢕⠐⠄
⠀⠀⠀⠀⠀⠀⡀⠀⢀⠀⠀⠈⠂⠈⠀⠀⠀⠀⠀⠀⠀⠀⡀⢁⠀⠀⠀⠀⠕⠨
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠂⢀"""

class HomeScreen(Screen):
    CSS= """
        #container_BUTTON-PROGRAM-WRAPPER {
            layout: grid;
            grid-size: 2 2;
            grid-columns: 22 22;
            grid-rows: 5 5;
            grid-gutter: 1;
            height: 1fr;
        }

        .button_PROGRAMS {
            content-align: center middle;
            height: 85%;
            width: 100%
        }

        #container_DATE-TIME-WRAPPER{
            border: solid black;
            width: 100%
        }
    """

    def compose(self) -> ComposeResult:

        # Naming of IDs and (Textual) classes should follow the form of: widget_NAME-NAME
        # Where the widget is all lowercase while the name of the ID/class is uppercase.
        # The widget should connect to the name with lowercase. While the name should be with a hyphen. 
        # For example; button_PROGRAM-WEB-BROWSER / container_DATE-TIME-WRAPPER
        # Also use the full name. DO NOT USE ACRONYMS!
        # I know, it's pretty extra. But, I'd rather avoid all the headaches for now and just keep everything consistent.

        time, date = get_datetime()

        with Horizontal():
            with Vertical():
                yield Static(ASCII_LOGO)

            with Vertical():
                with Container(id="container_BUTTON-PROGRAM-WRAPPER"):
                    yield Button("󱅶\nPROGRAM", classes="button_PROGRAMS")
                    yield Button("󱅶\nPROGRAM", classes="button_PROGRAMS")
                    yield Button("󱅶\nPROGRAM", classes="button_PROGRAMS")
                    yield Button("󱅶\nPROGRAM", classes="button_PROGRAMS")

                with Container(id="container_DATE-TIME-WRAPPER"):
                    yield Digits(time, id="digits_CLOCK")
                    yield Label(date, id="label_DATE")
                    yield Static()
                    yield Label("Failure should be our teacher,\nnot our undertaker. Failure is delay,\nnot defeat.\n -- Denis Waitley")

    def on_mount(self) -> None:
        self.clock = self.query_one("#digits_CLOCK", Digits)
        self.date = self.query_one("#label_DATE", Label)

        self.refresh_datetime()
        self.set_interval(1.0, self.refresh_datetime)

    def refresh_datetime(self):
        time, date = get_datetime()
        self.clock.update(time)
        self.date.update(date)