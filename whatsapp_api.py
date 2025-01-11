from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Parâmetros
WP_LINK = 'https://web.whatsapp.com'

# XPATHs
CONTACTS = '//*[@id="main"]/header/div[2]/div[2]/span'
MESSAGE_BOX = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
SEND = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'
NEW_CHAT = '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[3]/div'
FIRST_CONTACT = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]/div'
SEARCH_CONTACT = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/div/div[2]/div/div[2]'

class WhatsApp:
    def __init__(self):
        """
        Inicializa a instância do driver do Chrome, configura o WhatsApp Web e solicita o escaneamento do QR Code.
        """
        self.driver = self._setup_driver()
        self.driver.get(WP_LINK)
        print("Por favor, escaneie o QR Code para conectar ao WhatsApp Web.")

    @staticmethod
    def _setup_driver():
        """
        Configura o ChromeDriver utilizando o WebDriver Manager para evitar erros de compatibilidade.
        """
        print('Carregando...')
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--start-maximized")
        # Configuração correta do driver com `options` em vez de `chrome_options`
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver

    def _get_element(self, xpath, attempts=5, _count=0):
        """
        Localiza um elemento da página com múltiplas tentativas para lidar com atrasos de carregamento.
        """
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            return element
        except Exception:
            if _count < attempts:
                sleep(1)
                return self._get_element(xpath, attempts=attempts, _count=_count + 1)
            else:
                print(f"Elemento não encontrado: {xpath}")

    def _click(self, xpath):
        """
        Realiza um clique em um elemento identificado pelo XPATH.
        """
        el = self._get_element(xpath)
        el.click()

    def _send_keys(self, xpath, message):
        """
        Envia texto para um campo de entrada identificado pelo XPATH.
        """
        el = self._get_element(xpath)
        el.send_keys(message)

    def write_message(self, message):
        """
        Escreve uma mensagem no campo de texto, mas não a envia.
        """
        self._click(MESSAGE_BOX)
        self._send_keys(MESSAGE_BOX, message)

    def send_message(self, message):
        """
        Escreve e envia uma mensagem no WhatsApp.
        """
        self.write_message(message)
        self._click(SEND)

    def get_group_numbers(self):
        """
        Retorna uma lista com os números de telefone dos membros de um grupo.
        """
        try:
            el = self.driver.find_element(By.XPATH, CONTACTS)
            return el.text.split(',')
        except Exception:
            print("Cabeçalho do grupo não encontrado.")

    def search_contact(self, keyword):
        """
        Pesquisa um contato e abre o chat correspondente.
        """
        self._click(NEW_CHAT)
        self._send_keys(SEARCH_CONTACT, keyword)
        sleep(1)
        try:
            self._click(FIRST_CONTACT)
        except Exception:
            print("Contato não encontrado.")

    def get_all_messages(self):
        """
        Retorna todas as mensagens do chat atual.
        """
        messages_element = self.driver.find_elements(By.CLASS_NAME, '_21Ahp')  # Ajuste o CLASS_NAME conforme necessário
        messages_text = [el.text for el in messages_element]
        return messages_text

    def get_last_message(self):
        """
        Retorna a última mensagem recebida no chat atual.
        """
        all_messages = self.get_all_messages()
        if all_messages:
            return all_messages[-1]
        return None

    def zap_to_list(self, contact_list, message):
        """
        Envia uma mensagem padrão para uma lista de contatos.
        """
        for contact in contact_list:
            self.search_contact(contact)
            self.send_message(message)


# Exemplo de uso
if __name__ == "__main__":
    wp = WhatsApp()
    sleep(10)  # Aguarda o usuário escanear o QR Code

    # Teste de envio de mensagem
    wp.send_message("Olá do Selenium!")

    # Teste de envio de mensagem para uma lista de contatos
    contact_list = ["+5511999999999", "+5511888888888"]
    wp.zap_to_list(contact_list, "Mensagem automatizada para múltiplos contatos!")
