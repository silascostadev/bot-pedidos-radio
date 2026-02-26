import os
import time
import yt_dlp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==========================================
#        CONFIGURAÇÕES DO AMBIENTE
# ==========================================

# Nome EXATO do grupo ou contato no WhatsApp que o bot vai monitorar
NOME_CHAT_ALVO = "NOME_DO_SEU_GRUPO_AQUI" 

# Cria uma pasta 'Musicas_Baixadas' no mesmo local onde o script está rodando
PASTA_DESTINO = os.path.join(os.getcwd(), "Musicas_Baixadas")

# Cria uma pasta para salvar a sessão do WhatsApp e não pedir QR Code toda vez
CAMINHO_PERFIL_CHROME = os.path.join(os.getcwd(), "chrome_profile")

# ==========================================


def baixar_musica(nome_musica):
    print(f"\n[DOWNLOAD] Buscando: '{nome_musica}'...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(PASTA_DESTINO, '%(title)s.%(ext)s'),
        'default_search': 'ytsearch1:', 
        'noplaylist': True,
        'quiet': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([nome_musica])
        print(f"[DOWNLOAD] Sucesso! MP3 salvo em: {PASTA_DESTINO}")
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao processar: {e}")
        return False

def iniciar_whatsapp():
    print("Iniciando navegador...")
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={CAMINHO_PERFIL_CHROME}")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")
    
    print("Aguardando o WhatsApp Web carregar (escaneie o QR Code se for a primeira vez)...")
    
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )
    print("WhatsApp carregado!")
    return driver

def monitorar_pedidos(driver):
    try:
        chat = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f"//span[@title='{NOME_CHAT_ALVO}']"))
        )
        chat.click()
        print(f"Monitorando o chat: {NOME_CHAT_ALVO}")
    except Exception as e:
        print(f"Erro ao encontrar o chat '{NOME_CHAT_ALVO}'. Verifique o nome inserido nas configurações. Erro: {e}")
        return

    ultima_mensagem_processada = ""

    while True:
        try:
            # Captura mensagens recebidas e enviadas, usando o padrão de cópia de texto do WhatsApp
            mensagens = driver.find_elements(By.XPATH, "//div[contains(@class, 'message-in') or contains(@class, 'message-out')]//span[contains(@class, 'copyable-text')]//span")
            
            if mensagens:
                texto_ultima_msg = mensagens[-1].text
                
                if texto_ultima_msg != ultima_mensagem_processada and texto_ultima_msg.lower().startswith("!toca"):
                    ultima_mensagem_processada = texto_ultima_msg
                    
                    nome_musica = texto_ultima_msg[6:].strip()
                    
                    if nome_musica:
                        print(f"\n[WHATSAPP] Novo pedido recebido: {nome_musica}")
                        baixar_musica(nome_musica)
            
            time.sleep(3)
            
        except Exception as e:
            print(f"Erro durante o monitoramento: {e}")
            time.sleep(5)

if __name__ == "__main__":
    if not os.path.exists(PASTA_DESTINO):
        os.makedirs(PASTA_DESTINO)
    
    driver = iniciar_whatsapp()
    monitorar_pedidos(driver)