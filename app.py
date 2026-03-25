import flet as ft
import os
from backend import criar_estrutura_materia

def main(page: ft.Page):
    page.title = "Gerador de Pastas Academicas"
    page.window_width = 550
    page.window_height = 750
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(color_scheme_seed=ft.colors.BLUE)

    pasta_salva = page.client_storage.get("pasta_raiz_salva")
    modelo_salvo = page.client_storage.get("arquivo_modelo_salvo")

    titulo = ft.Text('Nova Matéria', size=32, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    def alterar_tema(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            botao_tema.icon = ft.icons.BRIGHTNESS_7
            titulo.color = ft.colors.WHITE
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            botao_tema.icon = ft.icons.BRIGHTNESS_4
            titulo.color = ft.colors.BLUE_GREY_900
        
        page.update()

    botao_tema = ft.IconButton(
        icon=ft.icons.BRIGHTNESS_7,
        on_click=alterar_tema
    )

    page.appbar = ft.AppBar(
        bgcolor=ft.colors.TRANSPARENT,
        actions=[botao_tema, ft.Container(width=10)]
    )

    campo_nome = ft.TextField(
        label='Nome da matéria (Ex: Banco de Dados)',
        width=450,
        autofocus=True,
        border_radius=10,
        text_size=16
    )

    texto_pasta_escolhida = ft.Text(
        pasta_salva if pasta_salva else 'Nenhuma pasta escolhida ainda.', 
        color=ft.colors.GREEN_600 if pasta_salva else ft.colors.RED_400,
        size=12
    )
    
    texto_modelo_escolhido = ft.Text(
        modelo_salvo if modelo_salvo else 'Nenhum arquivo modelo escolhido ainda.', 
        color=ft.colors.GREEN_600 if modelo_salvo else ft.colors.RED_400,
        size=12
    )

    def ao_escolher_pasta(e: ft.FilePickerResultEvent):
        if e.path:
            texto_pasta_escolhida.value = e.path
            texto_pasta_escolhida.color = ft.colors.GREEN_600
            page.client_storage.set("pasta_raiz_salva", e.path)
            page.update()

    def ao_escolher_modelo(e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            caminho_arquivo = e.files[0].path
            texto_modelo_escolhido.value = caminho_arquivo
            texto_modelo_escolhido.color = ft.colors.GREEN_600
            page.client_storage.set("arquivo_modelo_salvo", caminho_arquivo)
            page.update()

    selecionador_pasta = ft.FilePicker(on_result=ao_escolher_pasta)
    selecionador_modelo = ft.FilePicker(on_result=ao_escolher_modelo)
    page.overlay.extend([selecionador_pasta, selecionador_modelo])

    botao_pasta = ft.ElevatedButton(
        'Escolher Pasta Raiz',
        icon=ft.icons.FOLDER_OPEN,
        on_click=lambda _: selecionador_pasta.get_directory_path(),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
    )

    botao_modelo = ft.ElevatedButton(
        'Escolher Arquivo Modelo',
        icon=ft.icons.DESCRIPTION,
        on_click=lambda _: selecionador_modelo.pick_files(allowed_extensions=["docx", "doc"]),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
    )

    def acao_botao_clicado(e):
        nome_digitado = campo_nome.value
        pasta_raiz = texto_pasta_escolhida.value
        caminho_modelo = texto_modelo_escolhido.value

        if not nome_digitado:
            page.snack_bar = ft.SnackBar(ft.Text('Erro: Digite o nome da materia!'), bgcolor=ft.colors.RED)
            page.snack_bar.open = True
            page.update()
            return
        
        if pasta_raiz == "Nenhuma pasta escolhida ainda.":
            page.snack_bar = ft.SnackBar(ft.Text('Erro: Escolha a pasta raiz primeiro!'), bgcolor=ft.colors.RED)
            page.snack_bar.open = True
            page.update()
            return
            
        if caminho_modelo == "Nenhum arquivo modelo escolhido ainda.":
            page.snack_bar = ft.SnackBar(ft.Text('Erro: Escolha o arquivo modelo!'), bgcolor=ft.colors.RED)
            page.snack_bar.open = True
            page.update()
            return

        try:
            caminho_criado = criar_estrutura_materia(pasta_raiz, nome_digitado, caminho_modelo)
            page.snack_bar = ft.SnackBar(
                ft.Text(f'Sucesso! Pasta criada em: {caminho_criado}'), 
                bgcolor=ft.colors.GREEN
            )
            page.snack_bar.open = True
            campo_nome.value = ''

            botao_abrir_pasta.data = caminho_criado
            botao_abrir_pasta.visible = True
        except Exception as erro:
            page.snack_bar = ft.SnackBar(ft.Text(f'Ops! Algo deu errado: {erro}'), bgcolor=ft.colors.RED)
            page.snack_bar.open = True

        page.update()

    botao_criar = ft.ElevatedButton(
        text='Criar Estrutura de Pastas', 
        icon=ft.icons.CREATE_NEW_FOLDER, 
        on_click=acao_botao_clicado
    )

    botao_abrir_pasta = ft.ElevatedButton(
        text='Abrir Pasta Criada',
        icon=ft.icons.FOLDER_SPECIAL,
        visible=False,
        on_click=lambda e: os.startfile(botao_abrir_pasta.data) if botao_abrir_pasta.data else None 
    )

    layout_principal = ft.Column(
        controls=[
            titulo,
            ft.Divider(height=10, color=ft.colors.TRANSPARENT),
            botao_pasta,
            texto_pasta_escolhida,
            ft.Divider(height=5, color=ft.colors.TRANSPARENT),
            botao_modelo,
            texto_modelo_escolhido,
            ft.Divider(height=15, color=ft.colors.TRANSPARENT),
            campo_nome,
            botao_criar,
            botao_abrir_pasta
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    page.add(layout_principal)

ft.app(target=main)