import tkinter as tk
import requests
import time

root = tk.Tk()
root.geometry("720x350")
root.title("Envio de mensagem via API")

# Cria um rótulo para a API
api_label = tk.Label(root, text="Insira a URL da API:")
api_label.pack()

# Cria uma caixa de texto para a API
api_entry = tk.Entry(root)
api_entry.pack()

# Cria um rótulo para o token
token_label = tk.Label(root, text="Insira o token de acesso:")
token_label.pack()

# Cria uma caixa de texto para o token
token_entry = tk.Entry(root)
token_entry.pack()

# Cria um botão para salvar as informações
save_button = tk.Button(root, text="Salvar", command=lambda: save_info(api_entry.get(), token_entry.get()))
save_button.pack()

# Cria um rótulo para a mensagem
message_label = tk.Label(root, text="Insira a mensagem a ser enviada:")
message_label.pack()

# Cria uma caixa de texto para a mensagem
message_entry = tk.Entry(root)
message_entry.pack()

# Cria um botão para enviar a mensagem
send_button = tk.Button(root, text="Enviar", command=lambda: send_message(message_entry.get()))
send_button.pack()

# Cria um rótulo para exibir o status de envio
status_label = tk.Label(root, text="")
status_label.pack()

url = ""
headers = {}

# Define a função para salvar as informações
def save_info(api, token):
    global url, headers
    url = api
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    with open("api_info.txt", "w") as f:
        f.write(f"URL: {url}\nToken: {token}")
    print("Informações salvas em api_info.txt")


# Cria um rótulo para o número de telefone
number_label = tk.Label(root, text="Insira o número de telefone do cliente:")
number_label.pack()

# Cria uma caixa de texto para o número de telefone
number_entry = tk.Entry(root)
number_entry.pack()
# Cria uma lista vazia para armazenar os números de telefone
numbers = []

# Cria uma função para adicionar números à lista
def add_number():
    number = number_entry.get()
    numbers.append(number)
    number_list.config(text=numbers)

# Cria um botão para adicionar números
add_number_button = tk.Button(root, text="Adicionar número", command=add_number)
add_number_button.pack()

# Cria um rótulo para exibir a lista de números
number_list = tk.Label(root, text="")
number_list.pack()



def send_message(message):
    global message_count
    message_count = 0
    for number in numbers:
        data = {
            "number": number,
            "body": message
        }
        response = requests.post(url, headers=headers, json=data)
        status_label.config(text=f"Mensagem enviada para {number}. Status: {response.status_code}")
        message_count += 1
        if message_count % 4 == 0:
            time.sleep(60)



root.mainloop()
