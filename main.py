import logging
from pathlib import Path

import flet as ft
import flet_fastapi
from core.common import CommonContent
from components.navbar import NavBar
from core.destinations import nev_bar_destinations as destinations_list
from main_halper import MainHelper
from urls import Urls

logging.basicConfig(level=logging.INFO)


async def zzroo(page: ft.Page):

    async def route_change(e):
        route_list = main_helper_obj.get_route_list(page.route)
        print(f"Route changed: {route_list}, {page.route}")

        if len(route_list) == 0:
            await page.go_async("/home")
        elif len(route_list) == 1:
            await display_control_group(route_list[0])
        elif len(route_list) == 2:
            await display_control_group(route_list[1])
        elif len(route_list) == 3:
            await display_control_group(route_list[1])
        else:
            print("Invalid route")

    def find_control_group_object(control_group_name):
        for control_group in destinations_list.items:
            if control_group.name == control_group_name:
                return control_group

    async def display_control_group(control_group_name):
        if page.session.get("user") is None and control_group_name not in ["login", "otp"]:
            await page.go_async("/login")
            return

        control_group = find_control_group_object(control_group_name)
        if control_group in destinations_list.items:
            page.navigation_bar.visible = True
            page.navigation_bar.selected_index = destinations_list.items.index(
                control_group
            )
        else:
            page.navigation_bar.visible = False

        examples.visible = False
        listview.controls = []
        page.floating_action_button = None
        temp_column.controls.clear()

        container.visible = True
        temp_column.controls = [
            urls_obj.get_coutrol_group(control_group_name)
        ]

        await page.update_async()

    urls_obj = Urls(page=page)
    main_helper_obj = MainHelper(page=page)
    page.title = "zzroo"
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.fonts = {
        "SoraVariableFont": "fonts/Sora-VariableFont_wght.ttf",
        "PlayfairDisplay": "fonts/PlayfairDisplay-VariableFont_wght.ttf",
    }

    page.theme = ft.Theme(
        font_family="SoraVariableFont",
        use_material3=True,
        color_scheme=ft.ColorScheme(
            on_secondary_container=CommonContent.PRIMARY,
            on_surface=CommonContent.PRIMARY,
        ))

    page.theme_mode = main_helper_obj.theme_changed

    temp_column = ft.Column()

    container = ft.Container(content=temp_column)

    listview = ft.Column(spacing=100, scroll=ft.ScrollMode.AUTO)
    examples = ft.Column(controls=[listview])

    # if page.session.get("user") is not None:
    page.appbar = ft.AppBar(
        leading=ft.Container(padding=5, content=ft.Row(
            controls=[
                ft.Container(padding=5,
                             content=ft.Image(src=f"zero.svg", width=30, height=30))]
        )),
        leading_width=40,
        center_title=False,
        bgcolor=ft.ThemeMode.LIGHT,
        actions=[
            ft.Container(
                padding=10, content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.BRIGHTNESS_2_OUTLINED,
                                            tooltip="Toggle brightness",
                                            on_click=main_helper_obj.theme_changed,
                                        ),
                                        ft.IconButton(ft.icons.SEARCH,
                                                      tooltip="Search",
                                                      on_click=lambda _: page.go_async('/')),
                                        ft.IconButton(icon=ft.icons.NOTIFICATIONS_OUTLINED,
                                                      tooltip="Notifications",
                                                      on_click=lambda _: page.go_async(
                                                          '/settings'))
                                    ],
                                ),
                            ],
                        )
                    ],
                )
            )
        ],
    )
    page.navigation_bar = NavBar(page=page).navbar()

    await page.add_async(
        ft.Column(
            [container, examples]
        )
    )

    page.on_route_change = route_change
    print(f"Initial route: {page.route}")
    await page.go_async(page.route)


async def main(page: ft.Page):
    await zzroo(page)
    return

app = flet_fastapi.app(
    main, assets_dir=str(Path(__file__).resolve().parent.joinpath("assets"))
)


if __name__ == "__main__":
    ft.app(main, assets_dir="assets")
