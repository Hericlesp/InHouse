import flet as ft
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker

# ===== CONFIGURAÇÃO DO BANCO DE DADOS =====
Base = declarative_base()

class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    location = Column(String)
    rating = Column(Float)
    likes = Column(Integer)
    description = Column(String)
    image_url = Column(String)
    is_liked = Column(Boolean, default=False)
    is_favorite = Column(Boolean, default=False)

engine = create_engine('sqlite:///imoveis.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()

# ===== APLICAÇÃO PRINCIPAL =====
def main(page: ft.Page):
    # Configurações gerais da página
    page.title = "Imóvel Social+"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.WHITE
    page.padding = 0
    page.scroll = "always"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # ===== ESTILOS =====
    styles = {
        "title": ft.TextStyle(size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_800),
        "subtitle": ft.TextStyle(size=16, color=ft.colors.GREY_600),
        "rating": ft.TextStyle(size=18, weight=ft.FontWeight.BOLD, color=ft.colors.AMBER),
        "likes": ft.TextStyle(size=14, color=ft.colors.GREY),
        "desc": ft.TextStyle(size=14, color=ft.colors.GREY_700),
    }

    # ===== COMPONENTES DO PRIMEIRO CÓDIGO =====
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

    # Barra superior do primeiro código
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

    # Botões flutuantes do primeiro código
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
                    icon=ft.icons.PHONE,
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

    # ===== COMPONENTES DO SEGUNDO CÓDIGO =====
    search_field = ft.TextField(
        hint_text="Buscar imóveis...",
        expand=True,
        border_radius=30,
        border_color=ft.colors.GREY_300
    )

    # Cria o feed vazio primeiro
    feed = ft.Column(scroll="always", expand=True)

    # ===== FUNÇÕES PRINCIPAIS =====
    def load_initial_data():
        if db_session.query(Property).count() == 0:
            properties = [
                Property(
                    title="Imóvel centro",
                    location="Belo Horizonte",
                    rating=4.5,
                    likes=100,
                    description="Excelente localização, próximo ao centro comercial.",
                    image_url="https://images.unsplash.com/photo-1600585154340-be6161a56a0c"
                ),
                Property(
                    title="Imóvel ponte preta",
                    location="Rio de Janeiro",
                    rating=4.8,
                    likes=150,
                    description="Vista para o mar, com 3 quartos e 2 banheiros.",
                    image_url="https://placehold.co/600x400/15803d/white?text=Imóvel+Ponte"
                )
            ]
            db_session.add_all(properties)
            db_session.commit()

    def update_feed(properties=None):
        if properties is None:
            properties = db_session.query(Property).all()
        
        feed.controls.clear()
        feed.controls.extend([create_property_card(prop) for prop in properties])
        if page.views:  # Verifica se há views na página
            page.update()

    def create_property_card(property):
        return ft.Card(
            elevation=5,
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Image(
                            src=property.image_url,
                            height=200,
                            width=400,
                            fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.only(top_left=10, top_right=10)
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(property.title, style=styles["title"]),
                                    ft.Text(property.location, style=styles["subtitle"]),
                                ],
                                spacing=0
                            ),
                            padding=ft.padding.symmetric(horizontal=15, vertical=10)
                        ),
                        ft.Divider(height=1, color=ft.colors.GREY_300),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.IconButton(
                                        icon=ft.icons.FAVORITE,
                                        icon_color=ft.colors.RED if property.is_liked else ft.colors.GREY,
                                        on_click=lambda e, p=property: toggle_like(p)
                                    ),
                                    ft.Text(str(property.likes), style=styles["likes"]),
                                    ft.IconButton(
                                        icon=ft.icons.BOOKMARK,
                                        icon_color=ft.colors.BLUE if property.is_favorite else ft.colors.GREY,
                                        on_click=lambda e, p=property: toggle_favorite(p)
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.SHARE,
                                        icon_color=ft.colors.GREEN
                                    ),
                                    ft.Container(expand=True),
                                    ft.ElevatedButton(
                                        text="Ver Detalhes",
                                        on_click=lambda e, p=property: show_property_details(p),
                                        bgcolor=ft.colors.BLUE_700,
                                        color=ft.colors.WHITE
                                    )
                                ],
                                width=400
                            ),
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

    def toggle_like(property):
        property.is_liked = not property.is_liked
        property.likes += 1 if property.is_liked else -1
        db_session.commit()
        update_feed()

    def toggle_favorite(property):
        property.is_favorite = not property.is_favorite
        db_session.commit()
        update_feed()

    def show_property_details(property):
        details_view.controls = [
            ft.AppBar(title=ft.Text("Detalhes")),
            ft.Image(
                src=property.image_url,
                height=300,
                width=page.width,
                fit=ft.ImageFit.COVER,
                border_radius=ft.border_radius.all(10)
            ),
            criar_dots(),
            ft.ListTile(
                title=ft.Text(property.title, style=styles["title"]),
                subtitle=ft.Text(property.location, style=styles["subtitle"]),
            ),
            ft.Row([
                ft.Icon(ft.icons.STAR, color=ft.colors.AMBER),
                ft.Text(str(property.rating), style=styles["rating"]),
                ft.Text(f"({property.likes} curtidas)", style=styles["likes"]),
            ], spacing=5),
            ft.Text(property.description, style=styles["desc"]),
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.icons.STAR_BORDER, color=ft.colors.PINK),
                    ft.Icon(ft.icons.CHAT_BUBBLE_OUTLINE, color=ft.colors.PINK),
                    ft.Text(str(property.rating), weight=ft.FontWeight.BOLD)
                ],
                spacing=8,
                alignment=ft.MainAxisAlignment.END),
                padding=ft.padding.symmetric(horizontal=16, vertical=8)
            ),
            ft.ElevatedButton("Contatar Corretor", width=400),
            ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/")),
            floating_buttons
        ]
        page.go("/details")

    # ===== FILTROS =====
    filter_chips = ft.Row(
        scroll="auto",
        controls=[
            ft.Chip(
                label=ft.Text(label),
                selected=selected,
                on_select=lambda e, lbl=label: filter_properties(lbl),
                selected_color=ft.colors.BLUE_100,
                check_color=ft.colors.BLUE_800
            ) for label, selected in [
                ("Todos", True),
                ("Curtidos", False),
                ("Favoritos", False),
                ("São Paulo", False),
                ("Rio", False),
                ("BH", False)
            ]
        ]
    )

    def filter_properties(filter_name):
        for chip in filter_chips.controls:
            chip.selected = (chip.label == filter_name)
        filter_chips.update()
        
        query = db_session.query(Property)
        if filter_name == "Curtidos":
            query = query.filter(Property.is_liked == True)
        elif filter_name == "Favoritos":
            query = query.filter(Property.is_favorite == True)
        elif filter_name in ["São Paulo", "Rio", "BH"]:
            query = query.filter(Property.location.like(f"%{filter_name}%"))
        
        update_feed(query.all())

    # ===== VIEWS =====
    home_view = ft.View(
        "/",
        [
            top_bar,
            ft.Row([search_field, ft.IconButton(ft.icons.SEARCH)]),
            filter_chips,
            feed  # Adiciona o feed à view
        ]
    )

    details_view = ft.View("/details", [])

    # ===== ROTEAMENTO =====
    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(home_view)
            load_initial_data()
            update_feed()
        elif page.route == "/details":
            page.views.append(details_view)
        page.update()

    page.on_route_change = route_change

    # ===== BARRA INFERIOR =====
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.WHITE,
        content=ft.Row(
            [
                ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go("/")),
                ft.IconButton(ft.icons.SEARCH),
                ft.IconButton(ft.icons.ADD_BOX_OUTLINED),
                ft.IconButton(ft.icons.FAVORITE, on_click=lambda _: filter_properties("Favoritos")),
                ft.IconButton(ft.icons.PERSON_OUTLINE)
            ],
            alignment="spaceAround"
        )
    )

    # Inicia a aplicação
    page.go("/")

ft.app(target=main, view=ft.WEB_BROWSER)