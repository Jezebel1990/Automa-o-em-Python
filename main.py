import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc32faebd0cc44e60470a18ef013f7114"
# Your Auth Token from twilio.com/console
auth_token = "119a69253948ae9eb0d82c5c02b74e4f"
client = Client(account_sid, auth_token)

#Abrirá 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511957333990",
            from_="+18125671805",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)