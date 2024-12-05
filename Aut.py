# PAGINA DE LOGIN 05 12 2024

import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window.maximized = True
    page.window.resizable = False

    login = ft.Column([
        ft.Container(
            bgcolor=ft.colors.PURPLE_400,
            width=page.window_width - 10,
            height= page.window.height - 60,
            border_radius=10,

            content= ft.Column(
                ft.Container(
                    bgcolor=ft.colors.WHITE70,
                    width=400,
                    height=320,
                    border_radius=10,                    
                )
            )
        )

    ])

    '''register = ft.Column([
        pass
    ])'''

    page.add(login)

if __name__ == '__main__':
    ft.app(target=main)