# Kancil UI
#
# Copyright (C) 2026 Muhammad El Fatir
# SPDX-License-Identifier: GPL-3.0-or-later

from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical, Container
from textual.widgets import Label, Button, Digits, Static, Input

from utils.GENERATE_CONFIG import generate_config

class InitScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("Welcome to Kancil!")
        yield Input(placeholder="Type your name here ", id="username")
        yield Input(placeholder="Type your institution here ", id="school")
        yield Input(placeholder="Type your current class here 󰑴", id="current_class")
        yield Input(placeholder="Type your phone number here ", id="phone_number")

        with Horizontal():
            yield Button("Finish Setup", variant="success", id="button_SAVE")

        yield Static("", id="setup_message")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "button_SAVE":
            username = self.query_one("#username", Input).value.strip()
            school = self.query_one("#school", Input).value.strip()
            current_class = self.query_one("#current_class", Input).value.strip()
            phone_number = self.query_one("#phone_number", Input).value.strip()

            if not username:
                self.query_one("#setup_message", Static).update("Please enter a username.")
                return

            try:
                generate_config(
                    username=username,
                    school=school,
                    current_class=current_class,
                    phone_number=phone_number,
                )
            except (OSError, FileExistsError) as error:
                self.query_one("#setup_message", Static).update(f"Could not save configuration: {error}")
                return