import os
import logging
import requests

# 1. Configuração centralizada de logs (padrão ISO 8601 para Cloud/Docker)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()]
)

# 2. Constantes e leitura segura de configuração via ambiente
COINS = ["bitcoin", "ethereum", "solana"]
CURRENCY = "eur"
REQUEST_TIMEOUT = 10
API_KEY = os.getenv("CRYPTO_API_KEY")


def fetch_prices(coins_list):
    """Consulta a API da CoinGecko e devolve um dicionário com os preços atuais."""
    ids = ",".join(coins_list)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies={CURRENCY}"

    headers = {
        "Accept": "application/json"
    }
    if API_KEY:
        headers["x-cg-demo-api-key"] = API_KEY

    try:
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()  # Lança exceção se o código HTTP for 4xx ou 5xx
        return response.json()

    except requests.exceptions.RequestException as err:
        logging.error(f"Erro ao aceder à API: {err}")
        return None


# 3. Ponto de entrada da aplicação
if __name__ == "__main__":
    logging.info("A iniciar recolha de preços na CoinGecko...")
    prices = fetch_prices(COINS)

    if prices:
        logging.info(f"Dados recebidos com sucesso: {prices}")
    else:
        logging.warning("Não foi possível obter os preços nesta tentativa.")

    print("A minha primeira alteração com Git!")