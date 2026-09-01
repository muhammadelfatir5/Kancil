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
from textual.widgets import Label, Button, Digits, Static

from utils.utils_DATETIME import get_datetime

# The idea is for these variables to be set on first start-up.
# Save it to a file and read it instead of having these be variables.
# Or, a more fun idea is to let students change these variables to fit their own infos and stuff.
username = "Fatir"
school = "SMK Telkom Jakarta"
current_class = "XI RPL 5"
phone_number = "+62-xxx-xxx-xxxx"

ASCII_LOGO = f"""⢀⠰⢠⢀⠀⠀⠄⢁⢀
⠢⠈⠐⠨⠢⢄⠂⠐⢄⢁           KANCIL DESIGN MOCKUP
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

        time, message, date = get_datetime()

        with Horizontal():
            with Vertical():
                yield Static(ASCII_LOGO)

            with Vertical():
                with Container(id="container_BUTTON-PROGRAM-WRAPPER"):
                    yield Button("\nSettings", classes="button_PROGRAMS", id="button_SETTINGS")
                    yield Button("󱅶\nPROGRAM", classes="button_PROGRAMS")
                    yield Button("󱅶\nPROGRAM", classes="button_PROGRAMS")
                    yield Button("󱅶\nPROGRAM", classes="button_PROGRAMS")

                with Container(id="container_DATE-TIME-WRAPPER"):
                    with Horizontal():
                        yield Digits(time, id="digits_CLOCK")
                        yield Label(message, id="label_MESSAGE")
                    yield Label(date, id="label_DATE")
                    yield Static()
                    yield Label("Failure should be our teacher,\nnot our undertaker. Failure is delay,\nnot defeat.\n -- Denis Waitley")

    def on_mount(self) -> None:
        self.clock = self.query_one("#digits_CLOCK", Digits)
        self.message = self.query_one("#label_MESSAGE", Label)
        self.date = self.query_one("#label_DATE", Label)

        self.refresh_datetime()
        self.set_interval(1.0, self.refresh_datetime)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "button_SETTINGS":
                self.app.push_screen("settings")

    def refresh_datetime(self):
        time, message, date = get_datetime()
        self.clock.update(time)
        self.message.update(message)
        self.date.update(date)