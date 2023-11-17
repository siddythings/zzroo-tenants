import flet as ft
from core.destinations import nev_bar_destinations
from core.common import CommonContent


class NavBar:
    def __init__(self, page: ft.Page):
        self.page = page

    def get_destinations(self):
        destinations = []
        for destination in nev_bar_destinations.items:
            destinations.append(ft.NavigationDestination(
                icon=destination.icon,
                label=destination.label,
                selected_icon_content=ft.Icon(destination.selected_icon)
            ))
        return destinations

    async def control_group_selected(self, e):
        control_group_name = nev_bar_destinations.items[e.control.selected_index].name
        await self.page.go_async(f"/{control_group_name}")

    def navbar(self):
        navbar = ft.NavigationBar(
            destinations=self.get_destinations(),
            on_change=self.control_group_selected,
            selected_index=0
        )
        return navbar
