import flet as ft

def main(page: ft.Page):
    # Configurações da página
    page.title = "Aplicativo de Imóveis"
    page.bgcolor = ft.colors.WHITE
    page.padding = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 1. Componente de pontos indicadores
    def criar_dots():
        return ft.Row(
            controls=[
                ft.Container(
                    width=10,
                    height=10,
                    border_radius=5,
                    bgcolor=ft.colors.PINK
                ) for _ in range(9)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8
        )

    # 2. Barra superior
    top_bar = ft.Container(
        bgcolor=ft.colors.BLACK,
        padding=ft.padding.symmetric(horizontal=16, vertical=8),
        content=ft.Row(
            controls=[
                ft.CircleAvatar(
                    radius=36,
                    bgcolor=ft.colors.PINK,
                    content=ft.Icon(ft.icons.HOME, color=ft.colors.WHITE, size=36)
                ),
                ft.Icon(ft.icons.CHAT_BUBBLE_OUTLINE, color=ft.colors.WHITE, size=30),
                ft.Icon(ft.icons.MENU, color=ft.colors.WHITE, size=30)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    # 3. Cabeçalho
    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("Imóvel centro", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Belo Horizonte", size=16)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=8
    )

    # 4. Botões flutuantes (com ícones atualizados)
    floating_buttons = ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.PRIORITY_HIGH,
                    icon_color=ft.colors.WHITE,
                    bgcolor=ft.colors.PINK,
                    width=60,
                    height=60
                ),
                ft.IconButton(
                    icon=ft.icons.SEARCH,
                    icon_color=ft.colors.WHITE,
                    bgcolor=ft.colors.PINK,
                    width=60,
                    height=60
                ),
                ft.IconButton(
                    icon=ft.icons.ADD,
                    icon_color=ft.colors.WHITE,
                    bgcolor=ft.colors.PINK,
                    width=60,
                    height=60
                ),
                ft.IconButton(
                    icon=ft.icons.PHONE,  # Substituído WHATSAPP por PHONE
                    icon_color=ft.colors.WHITE,
                    bgcolor=ft.colors.PINK,
                    width=60,
                    height=60
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),
        padding=ft.padding.only(bottom=20)
    )

    # 5. Layout principal
    page.add(
        ft.Column(
            controls=[
                top_bar,
                header,
                ft.Image(
                    src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
                    width=page.width,
                    height=250,
                    fit=ft.ImageFit.COVER,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10)
                ),
                criar_dots(),
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Fulano e Siciliano curtiram este imóvel", 
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            "Casa moderna com 3 quartos, 2 banheiros e área gourmet. Excelente localização próxima ao centro comercial.",
                            max_lines=2,
                            overflow=ft.TextOverflow.ELLIPSIS
                        )
                    ], spacing=4),
                    padding=16
                ),
                ft.Container(
                    content=ft.Row([
                        ft.Icon(ft.icons.STAR_BORDER, color=ft.colors.PINK),
                        ft.Icon(ft.icons.CHAT_BUBBLE_OUTLINE, color=ft.colors.PINK),
                        ft.Text("4.5", weight=ft.FontWeight.BOLD)
                    ],
                    spacing=8,
                    alignment=ft.MainAxisAlignment.END),
                    padding=ft.padding.symmetric(horizontal=16, vertical=8)
                ),
                ft.Container(expand=True),  # Espaçador
                floating_buttons
            ],
            expand=True,
            spacing=0
        )
    )

# Inicialização do aplicativo
ft.app(target=main)