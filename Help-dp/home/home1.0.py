import flet as ft

def main(page: ft.Page):
    page.title = "Imóvel Social"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # ---- AppBar (Topo) ----
    page.appbar = ft.AppBar(
        title=ft.Text("Imóvel+", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
        center_title=False,
        bgcolor=ft.colors.BLUE_800,
        actions=[
            ft.IconButton(ft.icons.FAVORITE_BORDER, icon_color=ft.colors.WHITE),
            ft.IconButton(ft.icons.CHAT_BUBBLE_OUTLINE, icon_color=ft.colors.WHITE),
        ],
    )

    # ---- Stories (Rolagem Horizontal) ----
    stories = ft.ListView(
        horizontal=True,
        height=100,
        spacing=10,
        padding=10,
        controls=[
            ft.CircleAvatar(
                foreground_image_url="https://placehold.co/100x100/blue/white?text=Casa+1",
                radius=35,
                content=ft.Text("BH"),  # Badge de localização
            ),
            ft.CircleAvatar(
                foreground_image_url="https://placehold.co/100x100/green/white?text=Apto+2",
                radius=35,
                content=ft.Text("RJ"),
            ),
            # Adicione mais stories...
        ],
    )

    # ---- Feed de Imóveis ----
    def build_post(imovel_img: str, local: str, descricao: str):
        return ft.Column(
            controls=[
                # Foto do Imóvel
                ft.Image(src=imovel_img, height=300, fit=ft.ImageFit.COVER),
                # Barra de Interações
                ft.Row(
                    controls=[
                        ft.IconButton(ft.icons.FAVORITE_BORDER, icon_size=30),
                        ft.IconButton(ft.icons.CHAT_BUBBLE_OUTLINE, icon_size=30),
                        ft.IconButton(ft.icons.BOOKMARK_BORDER, icon_size=30),
                        ft.ElevatedButton(
                            "Contatar Corretor",
                            bgcolor=ft.colors.GREEN_500,
                            color=ft.colors.WHITE,
                            height=30,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                # Localização + Descrição
                ft.Text(local, weight=ft.FontWeight.BOLD),
                ft.Text(descricao, size=12),
                ft.Divider(),
            ],
            spacing=5,
        )

    feed = ft.ListView(
        controls=[
            build_post(
                "https://placehold.co/600x400/blue/white?text=Casa+SP",
                "São Paulo - Casa com Piscina",
                "3 quartos, 2 banheiros, área gourmet. R$ 2.500/mês.",
            ),
            build_post(
                "https://placehold.co/600x400/green/white?text=Apto+RJ",
                "Rio de Janeiro - Apartamento Vista Mar",
                "2 quartos, 1 vaga na garagem. R$ 3.200/mês.",
            ),
            # Adicione mais posts...
        ],
        expand=True,
    )

    # ---- Barra Inferior ----
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.WHITE,
        content=ft.Row(
            controls=[
                ft.IconButton(ft.icons.HOME, icon_color=ft.colors.BLUE_800),
                ft.IconButton(ft.icons.SEARCH, icon_color=ft.colors.GREY),
                ft.IconButton(ft.icons.ADD_BOX_OUTLINED, icon_color=ft.colors.GREY),
                ft.IconButton(ft.icons.STAR_BORDER, icon_color=ft.colors.GREY),
                ft.IconButton(ft.icons.PERSON_OUTLINE, icon_color=ft.colors.GREY),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        ),
    )

    # ---- Layout Final ----
    page.add(
        ft.Column(
            controls=[stories, feed],
            spacing=0,
            expand=True,
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)  # Para abrir no navegador