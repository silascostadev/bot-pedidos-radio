# 📻 WhatsApp Music Bot - Automação para Rádios

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-Web%20Scraping-green.svg)
![Status](https://img.shields.io/badge/Status-MVP%20Concluído-success.svg)

Um bot desenvolvido em Python para automatizar o fluxo de pedidos musicais de ouvintes. O script monitora um grupo ou chat específico no WhatsApp Web, identifica o comando do ouvinte, busca a música no YouTube e faz o download automático do arquivo MP3 para uma pasta local.

[cite_start]Este projeto foi construído como parte do Projeto de Extensão do curso de Análise e Desenvolvimento de Sistemas[cite: 1, 4]. [cite_start]O objetivo principal é a digitalização de processos operacionais, reduzindo o trabalho manual de locutores e operadores de áudio[cite: 19, 20].

## 🚀 Funcionalidades

* **Monitoramento em Tempo Real:** Lê as mensagens do WhatsApp Web através de automação de navegador (Selenium).
* **Download Automático:** Identifica o comando `!toca [nome da música]` e utiliza o `yt-dlp` para baixar o áudio do YouTube.
* **Conversão de Áudio:** Extrai e converte o arquivo diretamente para `.mp3` utilizando o FFmpeg.
* **Sessão Persistente:** Salva o perfil do Google Chrome localmente para que o usuário não precise escanear o QR Code a cada nova execução.

## 🛠️ Pré-requisitos

Para rodar este projeto na sua máquina, você precisará instalar:

1. **Python 3.8** ou superior.
2. **Google Chrome** (atualizado).
3. **FFmpeg:** Essencial para a conversão do áudio. 
   * Baixe o FFmpeg, extraia a pasta e adicione o caminho da pasta `bin` na variável de ambiente `PATH` do seu sistema operacional.

## ⚙️ Instalação e Configuração

1. Clone este repositório:
   ```bash
   git clone [https://github.com/silascostadev/bot-pedidos-radio.git](https://github.com/silascostadev/bot-pedidos-radio.git)
   cd bot-pedidos-radio

```

2. Instale as bibliotecas necessárias:
```bash
pip install selenium yt-dlp

```


3. Abra o arquivo `bot_radio.py` e configure a variável principal com o nome exato do chat ou grupo do WhatsApp que o bot deverá monitorar:
```python
NOME_CHAT_ALVO = "Nome do Grupo Aqui"

```



## 💻 Como usar

1. Execute o script no terminal:
```bash
python bot_radio.py

```


2. Na primeira execução, uma janela do Chrome será aberta pedindo para escanear o QR Code do WhatsApp Web.
3. Após o login, o bot aguardará as mensagens.
4. Envie uma mensagem no grupo configurado com o formato:
> `!toca System of a Down Chop Suey`


5. O bot fará o download da música e a salvará automaticamente na pasta `Musicas_Baixadas`, criada na raiz do projeto.

## 📂 Estrutura de Pastas Gerada

Após a execução, o projeto criará automaticamente os seguintes diretórios (ignorados pelo `.gitignore` para segurança):

* `/Musicas_Baixadas`: Onde os arquivos `.mp3` finais serão salvos.
* `/chrome_profile`: Onde os dados de sessão do WhatsApp ficam armazenados.

## 👨‍💻 Autor

Projeto desenvolvido por **Silas Costa** como MVP para resolução de demandas tecnológicas reais em ambientes de radiodifusão.