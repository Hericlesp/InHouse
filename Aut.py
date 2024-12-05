# PAGINA DE LOGIN 05 12 2024

import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window.maximized = True
    page.window.resizable = False

    login = ft.Column([ # aplica configuração a pagina peicipal roxa
        ft.Container(
            bgcolor=ft.colors.PURPLE_400,
            width=page.window_width - 10,
            height= page.window.height - 60,
            border_radius=10,

            content= ft.Column([ # aplica configuraçoes a caixa de informações
                ft.Container(
                    bgcolor=ft.colors.WHITE70,
                    width=400,
                    height=320,
                    border_radius=10,  

                    content=ft.Column([
                        ft.Column([
                            ft.Text(
                                #bgcolor=ft.colors.BLACK, a cor aplica a caixa completa
                                value='Sign-In',
                                weight='Bold',
                                size=20
                            )
                        ],spacing=20,horizontal_alignment='center')
                    ])                  
                )
            ], horizontal_alignment='center',alignment='center')
        )

    ])

    '''register = ft.Column([
        pass
    ])'''

    page.add(login)

if __name__ == '__main__':
    ft.app(target=main)