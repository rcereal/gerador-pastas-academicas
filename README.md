# 📁 Gerador de Pastas Acadêmicas
![demo](https://github.com/user-attachments/assets/89507149-de35-4c4e-a701-8907eef9d59e)

Um aplicativo desktop leve e prático para automatizar a criação de estruturas de diretórios e arquivos de estudo.

Em vez de criar manualmente dezenas de pastas a cada novo semestre, basta digitar o nome da matéria e o sistema monta toda a estrutura, copiando os modelos de arquivos necessários.

## 🎯 O Problema que este projeto resolve

O processo de organizar arquivos no início de um novo ciclo de estudos é repetitivo. Criar a pasta da matéria, criar as subpastas de avaliações (AVA 1, AVA 2) e copiar um documento de Word `.docx` em branco para cada uma delas consome tempo. Este projeto transforma um processo de vários cliques em apenas um.

## ✨ Funcionalidades

- **Interface Gráfica Moderna:** Desenvolvida em Flet, com suporte nativo a Tema Claro e Escuro.
- **Persistência de Dados:** O sistema salva localmente a última pasta raiz e o último arquivo modelo escolhidos, agilizando os próximos usos.
- **Navegação Integrada:** Abre automaticamente o explorador de arquivos do sistema na pasta recém-criada após o sucesso da operação.
- **Tratamento de Erros:** Validações de campos vazios e caminhos inválidos com feedback visual (SnackBars).
- **Standalone:** Pode ser empacotado em um arquivo `.exe` para rodar no Windows sem necessidade de instalar o Python.

## 🛠️ Tecnologias Utilizadas

- **Python 3.13** - Lógica principal e manipulação de arquivos do sistema operacional (`os` e `shutil`).
- **Flet** - Framework para construção da interface de usuário (UI).
- **PyInstaller** - Utilizado sob o capô pelo Flet para empacotamento do executável.

## 🚀 Como testar o projeto

### Pré-requisitos

Você precisa ter o Python instalado na sua máquina.

1. Clone este repositório:

```bash
git clone https://github.com/rcereal/gerador-pastas-academicas.git
```

2. Entre na pasta do projeto:

```bash
cd gerador-pastas-academicas
```

3. Instale o Flet:

```bash
pip install flet
```

4. Execute o aplicativo:

```bash
python app.py
```

📦 Como gerar o arquivo .exe
Caso queira usar o sistema sem precisar abrir o terminal, você pode gerar um executável para Windows rodando o seguinte comando na raiz do projeto:

```Bash
flet pack app.py --name "Gerador_Pastas_Academicas" --icon "gpa.ico"
O arquivo final ficará disponível dentro da pasta dist.
```

Projeto desenvolvido para fins de estudos práticos de Engenharia de Software, automação e interfaces gráficas.
