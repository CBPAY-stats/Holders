import requests
import json
import os

# URLs das APIs (precisam ser confirmadas ou ajustadas)
HOLDERS_API_URL = "https://horizon.livenet.xdbchain.com/accounts?asset=CBPAY" # Exemplo, pode precisar de ajuste
MARKET_DATA_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=cbpay&vs_currencies=usd" # Exemplo, pode precisar de ajuste
TRANSACTIONS_API_URL = "https://horizon.livenet.xdbchain.com/transactions?order=desc&limit=200" # Exemplo, pode precisar de ajuste

# Nomes dos ficheiros JSON locais
HOLDERS_FILE = "cbpay_holders_complete.json"
MARKET_FILE = "cbpay_market_data.json"
TRANSACTIONS_FILE = "cbpay_large_transactions.json"

def fetch_and_save_holders_data():
    print(f"Fetching holders data from {HOLDERS_API_URL}...")
    try:
        response = requests.get(HOLDERS_API_URL)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        
        # Processar os dados para o formato esperado pelo seu site
        # O seu site espera uma lista de objetos com 'address' e 'balance'
        processed_holders = []
        for record in data.get('_embedded', {}).get('records', []):
            for balance_entry in record.get('balances', []):
                if balance_entry.get('asset_code') == 'CBPAY':
                    processed_holders.append({
                        'address': record.get('account_id'),
                        'balance': float(balance_entry.get('balance'))
                    })
        
        # Sort by balance descending
        processed_holders.sort(key=lambda x: x['balance'], reverse=True)

        with open(HOLDERS_FILE, 'w') as f:
            json.dump(processed_holders, f, indent=4)
        print(f"Holders data saved to {HOLDERS_FILE}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching holders data: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON for holders data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while processing holders data: {e}")

def fetch_and_save_market_data():
    print(f"Fetching market data from {MARKET_DATA_API_URL}...")
    try:
        response = requests.get(MARKET_DATA_API_URL)
        response.raise_for_status()
        data = response.json()
        
        # O seu site espera um objeto com 'price_usd'
        price_usd = data.get('cbpay', {}).get('usd')
        if price_usd is not None:
            market_data = {"price_usd": price_usd}
            with open(MARKET_FILE, 'w') as f:
                json.dump(market_data, f, indent=4)
            print(f"Market data saved to {MARKET_FILE}")
        else:
            print("CBPAY price not found in market data.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching market data: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON for market data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while processing market data: {e}")

def fetch_and_save_transactions_data():
    print(f"Fetching transactions data from {TRANSACTIONS_API_URL}...")
    try:
        response = requests.get(TRANSACTIONS_API_URL)
        response.raise_for_status()
        data = response.json()
        
        # Processar os dados para o formato esperado pelo seu site
        # O seu site espera uma lista de objetos com 'amount', 'date', 'transaction_hash'
        processed_transactions = []
        for record in data.get('_embedded', {}).get('records', []):
            # Exemplo: filtrar transações com um valor mínimo para considerar 'grandes'
            # A API Horizon não fornece diretamente o 'amount' na lista de transações, 
            # seria necessário fazer requests adicionais para cada operação dentro da transação.
            # Para simplificar, vou apenas pegar as últimas transações e adicionar um valor placeholder.
            # VOCÊ PRECISARÁ AJUSTAR ESTA LÓGICA PARA OBTER VALORES REAIS DE TRANSAÇÕES GRANDES.
            processed_transactions.append({
                'amount': 1000000.0, # Placeholder: você precisa obter o valor real da transação
                'date': record.get('created_at'),
                'transaction_hash': record.get('hash')
            })
        
        # Filtrar para ter apenas transações 'grandes' (exemplo: > 1M CBPAY)
        # Esta lógica é um placeholder e precisa ser refinada com dados reais da API
        large_transactions = [tx for tx in processed_transactions if tx['amount'] >= 1000000]

        with open(TRANSACTIONS_FILE, 'w') as f:
            json.dump(large_transactions, f, indent=4)
        print(f"Transactions data saved to {TRANSACTIONS_FILE}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transactions data: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON for transactions data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while processing transactions data: {e}")

if __name__ == "__main__":
    fetch_and_save_holders_data()
    fetch_and_save_market_data()
    fetch_and_save_transactions_data()


