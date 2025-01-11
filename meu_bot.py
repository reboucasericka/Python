from time import sleep
from whatsapp_api import WhatsApp
# Inicializar o WhatsApp
wp = WhatsApp()
# Aguardar o login
input("Pressione ENTER após escanear o QR Code")
# Buscar todos os contatos disponíveis na agenda do WhatsApp
agenda = wp.get_all_contacts()  # Supondo que a API tenha esse método
# Lista de produtos a ser enviada
lista_produtos = ['1', '2', '3', '4', '4', '5']
# Verificar se a lista de produtos é menor ou igual à quantidade de contatos
if len(lista_produtos) > len(agenda):
    print("A {lista de produtos} excede o número de contatos na agenda!")
    exit()
# Loop para enviar mensagens
for contato, produto in zip(agenda, lista_produtos):
    # Nome do contato
    primeiro_nome = contato.split(' ')[0]  # Pegando o primeiro nome, se aplicável
    # Pesquisar pelo contato
    wp.search_contact(contato)
    sleep(2)
    # Mensagem personalizada
    mensagem = f"Olá {primeiro_nome}! Obrigado por comprar o produto {produto}!"
    wp.send_message(mensagem)
# Aguardar antes de fechar o driver
sleep(10)
wp.driver.close()
