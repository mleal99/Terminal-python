import requests

# 1. Define o URL do endpoint de monitorização
url = 'http://localhost:3000/api/v1/cluster/status'

# 2. Configura os headers com a API Key exigida pela infraestrutura
headers = {
    'X-API-Key': 'popcorn-clusters-sec-999'
}

try:
    # 3. Faz o pedido GET passando os headers corretos
    response = requests.get(url, headers=headers)

    # 4. Verifica o status code da resposta
    if response.status_code == 200:
        # Extrai os dados em formato JSON
        dados = response.____()
        
        # Verifica se a saúde do cluster está verde
        if dados.get('cluster_health') == 'GREEN':
            print("🟢 Sucesso: O cluster de produção está a operar normalmente!")
        else:
            print("🟡 Alerta: O cluster respondeu, mas o estado não é GREEN.")
            
    elif response.status_code == 401:
        print("🔴 Erro Crítico: Falha de autenticação! A API Key é inválida.")
    else:
        print(f"🟠 Aviso: O servidor respondeu com o código de estado: {response.____}")

except requests.exceptions.RequestException as e:
    print(f"❌ Erro de Ligação: Não foi possível contactar o servidor. Detalhes: {e}")

    