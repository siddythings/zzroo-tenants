from flet import *


class ControlGroup:
    def __init__(self, name, label, icon, selected_icon):
        self.name = name
        self.label = label
        self.icon = icon
        self.selected_icon = selected_icon
        self.grid_items = []


class NevBarDestinations:
    items = [
        ControlGroup(
            name="home",
            label="Home",
            icon=icons.HOME_OUTLINED,
            selected_icon=icons.HOME_ROUNDED,
        ),
        ControlGroup(
            name="settings",
            label="Settings",
            icon=icons.SETTINGS_OUTLINED,
            selected_icon=icons.SETTINGS_ROUNDED,
        )
    ]


nev_bar_destinations = NevBarDestinations()

control_group_label_dict = {
    "login": "Login",
    "otp": "OTP",
    "user_profile": "User Profile",
    "home": "Home",
    "settings": "Settings",
}
