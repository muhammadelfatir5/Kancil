# Kancil UI
#
# Copyright (C) 2026 Muhammad El Fatir
# SPDX-License-Identifier: GPL-3.0-or-later

from pathlib import Path
import tomlkit

CONFIG_DIR = Path.home() / ".config" / "kancil"
CONFIG_FILE = CONFIG_DIR / "config.toml"

def generate_config(username="", school="", current_class="", phone_number=""):
    if CONFIG_FILE.exists():   
        return

    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    config = tomlkit.document()
    config.add(tomlkit.comment("Kancil User Configuration"))
    config.add(tomlkit.nl())

    config.add("username", username)
    config.add("school", school)
    config.add("current_class", current_class)
    config.add("phone_number", phone_number)

    with CONFIG_FILE.open("w", encoding="utf-8") as config_file:
        tomlkit.dump(config, config_file)