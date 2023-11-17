import flet as ft
from db import settings_list
from core.common import CommonContent
from models.settings import SettingsModel
from models.redirect import OnClickRedirectPage


class Settings:
    def __init__(self, page: ft.Page):
        self.page = page

    async def on_click(self, e):
        route = f"{self.page.route}/{e.control.data.url}"
        print(route, "-------------")
        await self.page.go_async(route)

    def settings_card(self, setting):
        settings_model_obj = SettingsModel(**setting)
        card = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                      controls=[
                          ft.Container(
                              data=OnClickRedirectPage(
                                  url=settings_model_obj.settings_route
                              ),
                              on_click=self.on_click,
                              content=ft.Column(
                                  controls=[
                                      ft.Row(
                                          controls=[
                                              #   ft.Container(
                                              #       width=80,
                                              #       height=80,
                                              #       padding=5,
                                              #       border_radius=10,
                                              #       content=ft.CircleAvatar(
                                              #   bgcolor=ft.colors.SECONDARY_CONTAINER,
                                              #           bgcolor=CommonContent.PRIMARY,
                                              #           foreground_image_url="https://avatars.githubusercontent.com/u/_5041459?s=88&v=4",
                                              #           content=ft.Text(
                                              #               f"{tenant_model_obj.first_name[0]} {tenant_model_obj.last_name[0] if tenant_model_obj.last_name else ''}"),
                                              #       ),

                                              #   ),
                                              ft.Image(
                                                  src=settings_model_obj.settings_icon, border_radius=10),
                                              ft.Column(
                                                  controls=[
                                                      ft.Text(
                                                          max_lines=2,
                                                          value=f'{settings_model_obj.settings_name}',
                                                          weight=ft.FontWeight.W_500
                                                      ),
                                                  ]
                                              ),
                                          ]
                                      )
                                  ],
                              )
                          ),
                          ft.Row(
                              controls=[
                                  ft.IconButton(
                                      content=ft.Image(
                                          src=f"icon/Arrow_Left_LG.svg"),
                                      icon_color=ft.colors.GREEN,
                                  ),
                              ]
                          )
                      ]
                      )

        return card

    def settings(self):
        controls = []
        for setting in settings_list:
            controls.append(self.settings_card(setting))
            controls.append(ft.Divider())

        t_column = ft.Column(
            controls=controls
        )

        tenants_containers = ft.Container(
            border_radius=10,
            # bgcolor=ft.colors.SECONDARY_CONTAINER,
            content=t_column,
            padding=10,
            visible=True
        )

        container = ft.Container(
            border_radius=10,

            content=ft.Container(
                # bgcolor=ft.colors.SECONDARY_CONTAINER,
                content=ft.Column(
                    controls=[
                        tenants_containers
                    ]
                ),
                # padding=10,
            ),

            visible=True
        )
        return container
