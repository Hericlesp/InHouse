import flet as ft

def main(page: ft.Page):
    page.bgcolor = '#8ab9eb'
    page.theme_mode = 'dark'
    page.title= "Navegação"
    page.window_width = 450
    page.window_height = 700
    page.window_maximizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'



    def btn_editar(e):
        _stack_main.controls.clear()
        _stack_main.update()


        _stack_main.controls.append(_editar)
        _stack_main.update()

    def btn_pesquisar(e):
        _stack_main.controls.clear()
        _stack_main.update()


        _stack_main.controls.append(_pesquisar)
        _stack_main.update()

    def btn_home(e):
        _stack_main.controls.clear()
        _stack_main.update()


        _stack_main.controls.append(_main)
        _stack_main.update()

    def btn_config(e):
        _stack_main.controls.clear()
        _stack_main.update()


        _stack_main.controls.append(_config)
        _stack_main.update()

    def btn_compar(e):
        _stack_main.controls.clear()
        _stack_main.update()


        _stack_main.controls.append(_compartilhar)
        _stack_main.update()





    #botao centro flutuante
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD, bgcolor='blue',on_click=btn_home)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    #aba de navegação
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor='#F6F6F6FF',
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,icon_size=28, on_click=btn_editar),
                ft.IconButton(icon=ft.icons.SEARCH,icon_color=ft.colors.BLUE,icon_size=28,on_click=btn_pesquisar),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.SETTINGS,icon_color=ft.colors.BLUE,icon_size=28,on_click=btn_config),
                ft.IconButton(icon=ft.icons.SHARE,icon_color=ft.colors.BLUE,icon_size=28,on_click=btn_compar),
            ]
        )
    )

    #container principal
    _main = ft.Container(
        width=400,
        height= 550,
        bgcolor= '#F6F6F6FF',
        border_radius=16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.4,color='black')),
        content=ft.Text(
            value = 'INICIO',
            color = 'black',
            size = 32
        )
 
    )


    #container editar
    _editar = ft.Container(
        width=400,
        height= 550,
        bgcolor= '#F6F6F6FF',
        border_radius=16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.4,color='black')),
        content=ft.Text(
            value = 'EDITAR',
            color = 'black',
            size = 32
        )
 
    )

    #container pesquisar
    _pesquisar = ft.Container(
        width=400,
        height= 550,
        bgcolor= '#F6F6F6FF',
        border_radius=16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.4,color='black')),
        content=ft.Text(
            value = 'PESQUISAR',
            color = 'black',
            size = 32
        )
 
    )

    #container CONFIGURAÇÃO
    _config = ft.Container(
        width=400,
        height= 550,
        bgcolor= '#F6F6F6FF',
        border_radius=16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.4,color='black')),
        content=ft.Text(
            value = 'CONFIGURAÇÃO',
            color = 'black',
            size = 32
        )
 
    )


    #container COMPARTILHAR
    _compartilhar = ft.Container(
        width=400,
        height= 550,
        bgcolor= '#F6F6F6FF',
        border_radius=16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.4,color='black')),
        content=ft.Text(
            value = 'COMPARTILHAR',
            color = 'black',
            size = 32
        )
 
    )




    #stack principal
    _stack_main = ft.Stack(
        alignment=ft.alignment.center,
        controls=[
            _main
        ]
    )



    page.add(_stack_main)


ft.app(target=main)