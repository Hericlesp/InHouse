import flet as ft

def main(page: ft.Page):
    page.title = "Imóvel Social"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 10
    page.scroll = "always"

    # ===== ESTILOS =====
    title_style = ft.TextStyle(
        size=24,
        weight="bold",
        color=ft.colors.BLUE_800
    )
    
    subtitle_style = ft.TextStyle(
        size=16,
        color=ft.colors.GREY_600
    )
    
    rating_style = ft.TextStyle(
        size=18,
        weight="bold",
        color=ft.colors.AMBER
    )
    
    likes_style = ft.TextStyle(
        size=14,
        color=ft.colors.GREY
    )
    
    desc_style = ft.TextStyle(
        size=14,
        color=ft.colors.GREY_700
    )

    # ===== COMPONENTE DE CARD =====
    def property_card(title, location, rating, likes, description, image_url):
        return ft.Card(
            elevation=5,
            content=ft.Container(
                content=ft.Column(
                    [
                        # Imagem do imóvel
                        ft.Image(
                            src=image_url,
                            height=200,
                            width=400,
                            fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.only(top_left=10, top_right=10)
                        ),
                        
                        # Título e localização
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(title, style=title_style),
                                    ft.Text(location, style=subtitle_style),
                                ],
                                spacing=0
                            ),
                            padding=ft.padding.symmetric(horizontal=15, vertical=10)
                        ),
                        
                        # Divisor
                        ft.Divider(height=1, color=ft.colors.GREY_300),
                        
                        # Avaliação e curtidas
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.icons.STAR, color=ft.colors.AMBER),
                                    ft.Text(str(rating), style=rating_style),
                                    ft.Text(f"({likes} curtidas)", style=likes_style),
                                ],
                                spacing=5,
                                alignment="start"
                            ),
                            padding=ft.padding.symmetric(horizontal=15, vertical=5)
                        ),
                        
                        # Descrição
                        ft.Container(
                            content=ft.Text(description, style=desc_style),
                            padding=ft.padding.symmetric(horizontal=15, vertical=10)
                        ),
                        
                        # Botões de ação
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.FAVORITE_BORDER,
                                    icon_size=30,
                                    icon_color=ft.colors.RED
                                ),
                                ft.IconButton(
                                    icon=ft.icons.CHAT_BUBBLE_OUTLINE,
                                    icon_size=30,
                                    icon_color=ft.colors.BLUE
                                ),
                                ft.IconButton(
                                    icon=ft.icons.SHARE,
                                    icon_size=30,
                                    icon_color=ft.colors.GREEN
                                ),
                                ft.Container(expand=True),  # Espaçador
                                ft.ElevatedButton(
                                    text="Ver Detalhes",
                                    bgcolor=ft.colors.BLUE_700,
                                    color=ft.colors.WHITE
                                )
                            ],
                            width=400,
                            padding=ft.padding.symmetric(horizontal=10)
                        )
                    ],
                    spacing=0
                ),
                border_radius=10
            ),
            width=400,
            margin=ft.margin.symmetric(vertical=10)
        )

    # ===== FEED PRINCIPAL =====
    feed = ft.Column(
        controls=[
            property_card(
                "Imóvel centro",
                "Belo Horizonte",
                4.5,
                100,
                "Inserir um pouquinho de texto sobre o imóvel. Descrição breve aqui.",
                "https://placehold.co/600x400/2563eb/white?text=Imóvel+Centro"
            ),
            
            property_card(
                "Imóvel ponte preta",
                "Rio de Janeiro",
                4.8,
                150,
                "Outra descrição breve do imóvel. Detalhes como localização e comodidades.",
                "https://placehold.co/600x400/15803d/white?text=Imóvel+Ponte"
            ),
            
            # Adicione mais cards conforme necessário
        ],
        scroll="always",
        expand=True,
        spacing=20,
        horizontal_alignment="center"
    )

    # ===== BARRA DE NAVEGAÇÃO INFERIOR =====
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.WHITE,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.HOME, icon_color=ft.colors.BLUE_800),
                ft.IconButton(icon=ft.icons.SEARCH),
                ft.IconButton(icon=ft.icons.ADD_CIRCLE_OUTLINE),
                ft.IconButton(icon=ft.icons.FAVORITE_BORDER),
                ft.IconButton(icon=ft.icons.PERSON_OUTLINE),
            ],
            alignment="spaceAround"
        )
    )

    # ===== LAYOUT FINAL =====
    page.add(
        ft.Container(
            content=feed,
            expand=True,
            padding=ft.padding.symmetric(horizontal=20)
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)