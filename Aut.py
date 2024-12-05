# PAGINA DE LOGIN 05 12 2024

import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window.maximized = True
    page.window.resizable = False

    login = ft.Column([ # aplica configuração a pagina peicipal roxa
        ft.Container(
            bgcolor=ft.colors.GREEN_200,
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
                        ft.Container(
                            padding=ft.padding.only(
                                top=10,
                                bottom=12
                            ),

                            content = ft.Column([
                                ft.Text(
                                    #bgcolor=ft.colors.BLACK, a cor aplica a caixa completa
                                    value='Sign-In',color='black',
                                    weight='bold',
                                    size=20
                                )
                            ])
                        ),

                    
                        ft.Column([
                            ft.TextField(
                                hint_text='DIGITE SEU EMAIL',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.EMAIL                          
                            ),

                            ft.TextField(
                                hint_text='DIGITE SUA SENHA',
                                width=300, # LARGURA
                                height=40, # altura
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password= True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
                            ),

                            ft.ElevatedButton(
                                text='SIGN-IN',
                                bgcolor=ft.colors.GREEN_600,
                                on_hover=ft.colors.GREEN_600,
                                width=300,
                                height=40
                            ),

                            ft.Row([
                                ft.TextButton('RECUPERAR CONTA'),
                                ft.TextButton('CRIAR NOVA CONTA'),

                            ],width=300,  alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        

                        ],spacing=10),

                        ft.Row([
                            ft.IconButton(icon=ft.icons.EMAIL),
                            ft.IconButton(icon=ft.icons.FACEBOOK),
                            ft.IconButton(icon=ft.icons.TELEGRAM)
                        ],alignment='center')


                    ],horizontal_alignment='center')                  
                )
            ], horizontal_alignment='center',alignment='center')
        )

    ])

    register = ft.Column([
        ft.Container(
            bgcolor=ft.colors.GREEN_200,
            width=page.window_width - 10,
            height= page.window.height - 60,
            border_radius=10,

            content= ft.Column([ # aplica configuraçoes a caixa de informações
                ft.Container(
                    bgcolor=ft.colors.WHITE70,
                    width=400,
                    height=450,
                    border_radius=10,  

                content=ft.Column([
                    ft.Container(
                        padding=ft.padding.only(
                            top=10,
                            bottom=12
                        ),

                        content = ft.Column([
                            ft.Text(
                                #bgcolor=ft.colors.BLACK, a cor aplica a caixa completa
                                value='REGISTER',color='black',
                                weight='bold',
                                size=20
                            )
                        ])
                    ),

                
                    ft.Column([
                        ft.TextField(
                            hint_text='PRIMEIRO NOME',
                            width=300,
                            height=40,
                            border_radius=40,
                            prefix_icon=ft.icons.PERSON,
                            text_vertical_align=1,
                            keyboard_type=ft.KeyboardType.NAME                         
                        ),

                        ft.TextField(
                            hint_text='SEGUNDO NOME',
                            width=300,
                            height=40,
                            border_radius=40,
                            prefix_icon=ft.icons.PERSON,
                            text_vertical_align=1,
                            keyboard_type=ft.KeyboardType.NAME                         
                        ),

                        ft.TextField(
                            hint_text='DIGITE SEU EMAIL',
                            width=300,
                            height=40,
                            border_radius=40,
                            prefix_icon=ft.icons.EMAIL,
                            text_vertical_align=1,
                            keyboard_type=ft.KeyboardType.EMAIL                         
                        ),

                        ft.TextField(
                            hint_text='DIGITE SEU TELEFONE',
                            width=300,
                            height=40,
                            border_radius=40,
                            prefix_icon=ft.icons.PHONE,
                            text_vertical_align=1,
                            keyboard_type=ft.KeyboardType.PHONE                   
                        ),


                        ft.TextField(
                            hint_text='DIGITE SUA SENHA',
                            width=300, # LARGURA
                            height=40, # altura
                            border_radius=40,
                            prefix_icon=ft.icons.LOCK,
                            text_vertical_align=1,
                            password= True,
                            can_reveal_password=True,
                            keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
                        ),


                        ft.TextField(
                            hint_text='DIGITE SUA SENHA NOVAMENTE',
                            width=300, # LARGURA
                            height=40, # altura
                            border_radius=40,
                            prefix_icon=ft.icons.LOCK,
                            text_vertical_align=1,
                            password= True,
                            can_reveal_password=True,
                            keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
                        ),

                        ft.ElevatedButton(
                            text='REGISTRAR',
                            bgcolor=ft.colors.GREEN_600,
                            on_hover=ft.colors.GREEN_600,
                            width=300,
                            height=40
                        ),

                        ft.Row([
                            ft.TextButton('RECUPERAR CONTA'),
                            ft.TextButton('JA TENHO UMA CONTA'),

                        ],width=300,  alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

                   ],spacing=8),

                ],horizontal_alignment='center')                  
             )
            ], horizontal_alignment='center',alignment='center')
         )
    ])

    page.add(register)

if __name__ == '__main__':
    ft.app(target=main)