import flet as ft
from components.home import Home
from components.settings import Settings
from components.signup import Signup
from models.redirect import OnClickRedirectPage
from main_halper import MainHelper
from core.destinations import control_group_label_dict
from core.common import CommonContent


class Urls:
    def __init__(self, page: ft.Page):
        self.page = page
        self.home_obj = Home(page=page)
        self.settings_obj = Settings(page=page)
        self.signup_obj = Signup(page=page)

    def get_coutrol_group(self, control_group_name):
        self.page.appbar.visible = True

        if control_group_name == "login":
            self.page.appbar.title = ft.Text(
                control_group_label_dict.get(control_group_name), style=ft.TextThemeStyle.TITLE_MEDIUM,
                weight=ft.FontWeight.W_700, color=CommonContent.PRIMARY)
            self.page.appbar.visible = False
            return self.signup_obj.login_page()
        elif control_group_name == "otp":
            self.page.appbar.title = ft.Text(
                control_group_label_dict.get(control_group_name), style=ft.TextThemeStyle.TITLE_MEDIUM,
                weight=ft.FontWeight.W_700, color=CommonContent.PRIMARY)
            self.page.appbar.visible = False
            return self.signup_obj.otp_page()
        elif control_group_name == "user_profile":
            self.page.appbar.title = ft.Text(
                control_group_label_dict.get(control_group_name), style=ft.TextThemeStyle.TITLE_MEDIUM,
                weight=ft.FontWeight.W_700, color=CommonContent.PRIMARY)
            return self.signup_obj.user_profile()

        elif control_group_name == "home":
            self.page.appbar.title = ft.Text(
                control_group_label_dict.get(control_group_name), style=ft.TextThemeStyle.TITLE_MEDIUM,
                weight=ft.FontWeight.W_700, color=CommonContent.PRIMARY)
            return self.home_obj.home()
        elif control_group_name == "settings":
            self.page.appbar.title = ft.Text(
                control_group_label_dict.get(control_group_name), style=ft.TextThemeStyle.TITLE_MEDIUM,
                weight=ft.FontWeight.W_700, color=CommonContent.PRIMARY)
            return self.settings_obj.settings()

    async def control_floating_action(self, e):
        route = f"{self.page.route}/{e.control.data.url}"
        self.page.floating_action_button = None
        await self.page.go_async(f'{route}')
