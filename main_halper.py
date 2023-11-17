import flet as ft


class MainHelper:
    def __init__(self, page: ft.Page):
        self.page = page

    async def theme_changed(self, e):
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
        await self.page.update_async()

    def get_route_list(self, route):
        route_list = [item for item in route.split("/") if item != ""]
        return route_list
