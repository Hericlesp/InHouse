import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Home - Imóveis"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    # ----- AppBar (Barra Superior) -----
    page.appbar = ft.AppBar(
        title=ft.Text("Imóveis Disponíveis", color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE_800,
        center_title=True,
    )

    # ----- Card de Imóvel (Exemplo 1) -----
    card_centro = ft.Card(
        elevation=5,
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Image(
                        src="https://placehold.co/400x200/blue/white?text=Imóvel+CENTRO",
                        fit=ft.ImageFit.COVER,
                        height=150,
                    ),
                    ft.ListTile(
                        title=ft.Text("Imóvel Centro", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text("Belo Horizonte", color=ft.colors.GREY_600),
                    ),
                    ft.Row(
                        [
                            ft.Icon(ft.icons.STAR, color=ft.colors.AMBER),
                            ft.Text("4.5", size=14),
                            ft.Text("(100 curtidas)", size=12, color=ft.colors.GREY),
                        ],
                        spacing=5,
                    ),
                    ft.Text(
                        "Inserir um pouquinho de texto sobre o imóvel. Descrição breve aqui.",
                        size=12,
                        color=ft.colors.GREY_700,
                    ),
                    ft.ElevatedButton("Ver Detalhes", width=150),
                ],
                spacing=10,
            ),
            padding=15,
        ),
    )

    # ----- Card de Imóvel (Exemplo 2) -----
    card_ponte = ft.Card(
        elevation=5,
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Image(
                        src="https://placehold.co/400x200/green/white?text=Imóvel+PONTE",
                        fit=ft.ImageFit.COVER,
                        height=150,
                    ),
                    ft.ListTile(
                        title=ft.Text("Imóvel Ponte Preta", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text("Rio de Janeiro", color=ft.colors.GREY_600),
                    ),
                    ft.Row(
                        [
                            ft.Icon(ft.icons.STAR, color=ft.colors.AMBER),
                            ft.Text("4.8", size=14),
                            ft.Text("(150 curtidas)", size=12, color=ft.colors.GREY),
                        ],
                        spacing=5,
                    ),
                    ft.Text(
                        "Outra descrição breve do imóvel. Detalhes como localização e comodidades.",
                        size=12,
                        color=ft.colors.GREY_700,
                    ),
                    ft.ElevatedButton("Ver Detalhes", width=150),
                ],
                spacing=10,
            ),
            padding=15,
        ),
    )

    # ----- Layout Principal (GridView) -----
    page.add(
        ft.GridView(
            controls=[card_centro, card_ponte],
            runs_count=2,  # 2 colunas
            max_extent=400,  # Largura máxima dos cards
            spacing=20,
            run_spacing=20,
        )
    )

ft.app(target=main)