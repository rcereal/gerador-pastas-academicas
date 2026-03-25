import os
import shutil
def criar_estrutura_materia(pasta_raiz, nome_materia, caminho_modelo):
    maior_numero = 0

    if not os.path.exists(pasta_raiz):
        os.makedirs(pasta_raiz)

    for item in os.listdir(pasta_raiz):

        caminho_completo = os.path.join(pasta_raiz, item)

        if os.path.isdir(caminho_completo):
            partes_do_nome = item.split()

            if partes_do_nome and partes_do_nome[0].isdigit():
                numero_atual = int(partes_do_nome[0])

                if numero_atual > maior_numero:
                    maior_numero = numero_atual

    proximo_numero = maior_numero + 1
    numero_formatado = f"{proximo_numero:02d}"

    nome_pasta_principal = f"{numero_formatado} {nome_materia}"
    caminho_principal = os.path.join(pasta_raiz, nome_pasta_principal)

    os.makedirs(caminho_principal)

    subpastas = ['Ava 1', 'Ava 2']

    for subpasta in subpastas:
        caminho_subpasta = os.path.join(caminho_principal, subpasta)
        os.makedirs(caminho_subpasta)

        if os.path.exists(caminho_modelo):
            shutil.copy(caminho_modelo, caminho_subpasta)

    return caminho_principal
