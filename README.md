# WhatsApp Group Chatbox API on Selenium

<div style="text-align: justify;">

> **Status:** Em Desenvolvimento ⚠️  
> Este repositório fornece uma API para automação do WhatsApp utilizando Selenium. A API é projetada para interagir com grupos do WhatsApp por meio do navegador web, permitindo o envio e recebimento de mensagens, busca de contatos, e integração com chatbots personalizados.

---

## Funcionalidades Implementadas

### **Controle de Grupos**
- **Obter contatos de um grupo:**  
  Recupera uma lista de números de telefone de todos os membros do grupo.
  ```python
  from whatsapp_api import WhatsApp
  wp = WhatsApp()
  print(wp.get_group_numbers())
  ```

- **Pesquisar contato:**  
  Localiza contatos em um grupo com base em um número de telefone ou nome.
  ```python
  wp.search_contact('+55000000000')
  ```

- **Parser de números:**  
  Uniformiza números de telefone para permitir operações em conjuntos (ex.: verificar quais contatos não estão no grupo).
  ```python
  group_numbers = wp.get_group_numbers()
  parsed_numbers = wp.parser(group_numbers[:-1])  # Remove o contato 'Você'
  ```

---

### **Envio e Recebimento de Mensagens**
- **Enviar mensagens para o grupo:**  
  Escreve e envia mensagens para o grupo selecionado.
  ```python
  wp.send_message('Olá, grupo! Esta é uma mensagem automática.')
  ```

- **Escrever mensagens sem enviar:**  
  Escreve a mensagem no campo de texto, mas não a envia (útil para revisão manual).
  ```python
  wp.write_message('Esta mensagem foi escrita, mas não enviada.')
  ```

- **Receber a última mensagem:**  
  Obtém a mensagem mais recente do grupo.
  ```python
  last_message = wp.get_last_message()
  print(last_message)
  ```

- **Obter todas as mensagens:**  
  Recupera todas as mensagens do grupo, permitindo análises ou ações baseadas em texto.
  ```python
  all_messages = wp.get_all_messages()
  print(all_messages)
  ```

---

### **Chatbot Personalizado**
- **Interação automatizada:**  
  Crie um loop de interação para responder automaticamente com base no conteúdo das mensagens recebidas.
  ```python
  while True:
      last_message = wp.get_last_message()
      if "Olá" in last_message:
          wp.send_message("Olá! Como posso ajudar?")
  ```

---

## Requisitos

1. **Dependências do Python:**  
   Instale o Selenium:
   ```bash
   pip install selenium
   ```

2. **ChromeDriver:**  
   Baixe o ChromeDriver compatível com a versão do seu navegador em: [ChromeDriver](http://chromedriver.chromium.org/).  
   Adicione o executável do ChromeDriver a uma pasta acessível no PATH do sistema.

3. **QRCode do WhatsApp Web:**  
   A API exige que o usuário escaneie o QR Code para acessar o WhatsApp Web no início da sessão.

---

## Estrutura do Projeto

```plaintext
whatsapp-group-api/
│
├── src/
│   ├── whatsapp_api.py    # Código principal da API
│   ├── chatbot.py         # Exemplo de chatbot personalizado
│   └── utils.py           # Funções auxiliares (ex.: parsing de números)
│
├── requirements.txt       # Lista de dependências
├── README.md              # Documentação do projeto
└── chromedriver.exe       # Executável do ChromeDriver (se necessário)
```

---

## Instruções de Uso

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/whatsapp-group-api.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure o ChromeDriver no PATH do sistema.

4. Execute um exemplo:
   ```python
   from whatsapp_api import WhatsApp

   wp = WhatsApp()
   wp.send_message('Olá, grupo! Esta é uma mensagem automática.')
   ```

---

## Limitações e Considerações

1. **Restrições do WhatsApp Web:**  
   - O WhatsApp pode bloquear sua conta se detectar uso indevido de automação.
   - Evite enviar mensagens em massa ou realizar operações de spam.

2. **Sessão expirada:**  
   - Caso o QR Code expire, reinicie a aplicação para escanear novamente.

3. **Compatibilidade com Navegador:**  
   - Certifique-se de que sua versão do Chrome e do ChromeDriver sejam compatíveis.

---

## Próximos Passos

- Implementar suporte para múltiplos grupos simultaneamente.
- Adicionar persistência de sessões para evitar reescanear o QR Code.
- Melhorar o tratamento de erros e logs.

---

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar um **pull request**.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

</div>
