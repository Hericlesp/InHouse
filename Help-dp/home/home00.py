import flet as ft
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do SQLAlchemy (SQLite)
Base = declarative_base()
engine = create_engine('sqlite:///imoveis.db')
Session = sessionmaker(bind=engine)
session = Session()

# Modelo de Dados para Imóveis
class Imovel(Base):
    __tablename__ = 'imoveis'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    preco = Column(Float)
    localizacao = Column(String)
    descricao = Column(String)
    imagem_url = Column(String)

# Cria as tabelas no banco (execute uma vez)
Base.metadata.create_all(engine)

def main(page: ft.Page):
    page.title = "App de Imóveis"
    page.theme_mode = ft.ThemeMode.LIGHT  # Pode ser alterado nas configurações

    # Dados de Exemplo (adicione via código ou interface)
    if session.query(Imovel).count() == 0:
        session.add_all([
            Imovel(
                titulo="Casa com Piscina",
                preco=2500,
                localizacao="São Paulo",
                descricao="3 quartos, 2 banheiros, área gourmet.",
                imagem_url="https://exemplo.com/casa1.jpg"
            ),
            # Adicione mais imóveis...
        ])
        session.commit()

    # ---------------------
    # Controladores de Interface
    # ---------------------
    def navigate(e):
        page.views.clear()
        if e.control.selected_index == 0:
            page.views.append(home_view)
        elif e.control.selected_index == 1:
            page.views.append(pesquisa_view)
        elif e.control.selected_index == 2:
            page.views.append(chat_view)
        elif e.control.selected_index == 3:
            page.views.append(config_view)
        page.update()

    # ---------------------
    # Página Home (Imóveis)
    # ---------------------
    def build_imovel_card(imovel: Imovel):
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Image(src=imovel.imagem_url, height=150, fit=ft.ImageFit.COVER),
                    ft.ListTile(
                        title=ft.Text(imovel.titulo),
                        subtitle=ft.Text(f"R$ {imovel.preco}/mês - {imovel.localizacao}"),
                    ),
                    ft.Text(imovel.descricao, size=12),
                    ft.ElevatedButton("Ver Detalhes"),
                ]),
                padding=10,
            )
        )

    imoveis = session.query(Imovel).all()
    home_view = ft.View(
        route="/",
        controls=[
            ft.AppBar(title=ft.Text("Imóveis Disponíveis")),
            ft.GridView(
                controls=[build_imovel_card(imovel) for imovel in imoveis],
                runs_count=2,  # 2 colunas
                max_extent=400,  # Largura máxima dos cards
            ),
        ],
    )

    # ---------------------
    # Página de Pesquisa
    # ---------------------
    pesquisa_view = ft.View(
        route="/pesquisa",
        controls=[
            ft.AppBar(title=ft.Text("Pesquisar Imóveis")),
            ft.TextField(label="Localização", hint_text="Ex: São Paulo"),
            ft.RangeSlider(
                label="Preço (R$)",
                min=0,
                max=10000,
                divisions=10,
                start_value=1000,
                end_value=5000,
            ),
            ft.Dropdown(
                label="Tipo",
                options=[
                    ft.dropdown.Option("Casa"),
                    ft.dropdown.Option("Apartamento"),
                ]
            ),
            ft.ElevatedButton("Filtrar"),
        ],
    )

    # ---------------------
    # Página de Chat
    # ---------------------
    chat_mensagens = ft.Column()
    campo_mensagem = ft.TextField(hint_text="Digite uma mensagem...", expand=True)

    def enviar_mensagem(e):
        if campo_mensagem.value:
            chat_mensagens.controls.append(ft.Text(f"Você: {campo_mensagem.value}"))
            campo_mensagem.value = ""
            page.update()

    chat_view = ft.View(
        route="/chat",
        controls=[
            ft.AppBar(title=ft.Text("Chat com Clientes")),
            chat_mensagens,
            ft.Row([campo_mensagem, ft.ElevatedButton("Enviar", on_click=enviar_mensagem)]),
        ],
    )

    # ---------------------
    # Página de Configurações
    # ---------------------
    config_view = ft.View(
        route="/config",
        controls=[
            ft.AppBar(title=ft.Text("Configurações")),
            ft.Switch(label="Modo Escuro", on_change=lambda e: page.theme_mode_update()),
            ft.TextField(label="Nome do Usuário"),
            ft.ElevatedButton("Salvar"),
        ],
    )

    # ---------------------
    # Barra de Navegação Inferior
    # ---------------------
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationDestination(icon=ft.icons.SEARCH, label="Pesquisa"),
            ft.NavigationDestination(icon=ft.icons.CHAT, label="Chat"),
            ft.NavigationDestination(icon=ft.icons.SETTINGS, label="Configurações"),
        ],
        on_change=navigate,
        selected_index=0,
    )

    page.add(home_view)

ft.app(target=main)