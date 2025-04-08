import flet as ft

def main(page: ft.Page):
    page.title = "Página Inicial Home"
    page.padding = 0
    page.bgcolor = ft.colors.WHITE

    current_index = ft.Ref 

    properties = [
        {
            "title": "Imóvel Centro",
            "city": "Belo Horizonte",
            "image": "https://cdn.pixabay.com/photo/2016/03/27/19/31/house-1283691_960_720.jpg"
        },
        {
            "title": "Imóvel Ponte Preta",
            "city": "Rio de Janeiro",
            "image": "https://cdn.pixabay.com/photo/2017/03/28/12/10/house-2187173_960_720.jpg"
        }
    ]

    # Propriedade selecionada
    property_card = ft.Ref[ft.Image]()
    title_text = ft.Ref[ft.Text]()
    city_text = ft.Ref[ft.Text]()

    def update_property(index):
        current = properties[index]
        property_card.current.src = current["image"]
        title_text.current.value = current["title"]
        city_text.current.value = current["city"]
        page.update()

    def next_property(_):
        current_index.current = (current_index.current + 1) % len(properties)
        update_property(current_index.current)

    def previous_property(_):
        current_index.current = (current_index.current - 1 + len(properties)) % len(properties)
        update_property(current_index.current)

    app_bar = ft.Container(
        bgcolor=ft.colors.BLACK,
        padding=10,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.CircleAvatar(content=ft.Icon(ft.icons.HOME, color=ft.colors.WHITE), bgcolor=ft.colors.PINK, radius=25),
                ft.Icon(ft.icons.CHAT_BUBBLE_OUTLINE, color=ft.colors.WHITE),
                ft.Icon(ft.icons.MENU, color=ft.colors.WHITE),
            ]
        )
    )

    image_section = ft.Container(
        on_scroll=next_property,
        content=ft.Image(
            ref=property_card,
            src=properties[0]["image"],
            height=240,
            fit=ft.ImageFit.COVER
        )
    )

    carousel_dots = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                margin=5,
                width=10,
                height=10,
                bgcolor=ft.colors.PINK if i == 0 else ft.colors.GREY_300,
                border_radius=10
            ) for i in range(len(properties))
        ]
    )

    info_section = ft.Column(
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(properties[0]["title"], ref=title_text, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(properties[0]["city"], ref=city_text, size=16),
                ]
            ),
            ft.Text("João e Ana curtiram este imóvel", weight=ft.FontWeight.BOLD),
            ft.Text("Casa moderna com 3 quartos, 2 banheiros, 1 vaga de garagem e área gourmet."),
        ]
    )

    features = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        controls=[
            ft.Column([ft.Icon(ft.icons.KING_BED), ft.Text("3 Quartos", size=12)]),
            ft.Column([ft.Icon(ft.icons.BATHTUB), ft.Text("2 Banheiros", size=12)]),
            ft.Column([ft.Icon(ft.icons.GARAGE), ft.Text("1 Garagem", size=12)]),
            ft.Column([ft.Icon(ft.icons.SQUARE_FOOT), ft.Text("120m²", size=12)])
        ]
    )

    rating_actions = ft.Row(
        alignment=ft.MainAxisAlignment.END,
        controls=[
            ft.Icon(ft.icons.STAR, color=ft.colors.ORANGE),
            ft.Text("4.5", weight=ft.FontWeight.BOLD),
            ft.Icon(ft.icons.FAVORITE_BORDER, color=ft.colors.PINK),
            ft.Icon(ft.icons.CHAT_BUBBLE_OUTLINE, color=ft.colors.PINK)
        ]
    )

    floating_buttons = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        controls=[
            ft.FloatingActionButton(icon=ft.icons.SEARCH, bgcolor=ft.colors.PINK, tooltip="Buscar"),
            ft.FloatingActionButton(icon=ft.icons.ADD, bgcolor=ft.colors.PINK, tooltip="Adicionar aos favoritos"),
            ft.FloatingActionButton(icon=ft.icons.SMARTPHONE, bgcolor=ft.colors.PINK, tooltip="WhatsApp")
        ]
    )

    page.add(
        app_bar,
        info_section,
        image_section,
        carousel_dots,
        features,
        rating_actions,
        floating_buttons
    )

    update_property(0)

ft.app(target=main)
