import speedtest as st  # Importa a biblioteca speedtest para medir velocidades de download, upload e ping

def Speed_Test():
    # Cria uma instância do Speedtest para realizar os testes
    test = st.Speedtest()

    # Mede a velocidade de download em bits por segundo, converte para Mbps e arredonda para 2 casas decimais
    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print("Download speed in Mbps: ", down_speed)  # Exibe a velocidade de download

    # Mede a velocidade de upload em bits por segundo, converte para Mbps e arredonda para 2 casas decimais
    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print("Upload speed in Mbps: ", up_speed)  # Exibe a velocidade de upload

    # Obtém o valor do ping (latência em ms) dos resultados do teste
    ping = test.results.ping
    print("Ping: ", ping)  # Exibe o ping

# Chama a função Speed_Test para executar os testes de velocidade
Speed_Test()
