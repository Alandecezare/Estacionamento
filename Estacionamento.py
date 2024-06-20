def exibir_menu():
    """
    Função que exibe o menu de opções para o usuário.
    """
    # Imprime as opções do menu
    print("\nMenu:")
    print("1 - Estacionar veículo")
    print("2 - Retirar veículo")
    print("3 - Veículos estacionados")
    print("4 - Está estacionado?")
    print("0 - Sair")

def adicionar_veiculo(estacionamento):
    """
    Função para adicionar um veículo ao estacionamento.
    
    Args:
        estacionamento (dict): Dicionário contendo os veículos estacionados.
    """
    # Solicita a placa do veículo
    numero_placa = input("Digite a placa do veículo: ")
    # Verifica se a placa já está no dicionário de veículos
    if numero_placa in estacionamento:
        print("Este veículo já está estacionado.")
    else:
        # Solicita outras informações do veículo
        marca_veiculo = input("Digite a marca do veículo: ")
        modelo_veiculo = input("Digite o modelo do veículo: ")
        cor_veiculo = input("Digite a cor do veículo: ")
        nome_proprietario = input("Digite o nome do proprietário: ")
        # Adiciona o veículo ao dicionário
        estacionamento[numero_placa] = {
            "marca": marca_veiculo,
            "modelo": modelo_veiculo,
            "cor": cor_veiculo,
            "proprietario": nome_proprietario
        }
        print(f"Veículo de placa {numero_placa} estacionado com sucesso.")

def remover_veiculo(estacionamento):
    """
    Função para remover um veículo do estacionamento.
    
    Args:
        estacionamento (dict): Dicionário contendo os veículos estacionados.
    """
    # Solicita a placa do veículo a ser retirado
    numero_placa = input("Digite a placa do veículo a ser retirado: ")
    # Verifica se a placa está no dicionário de veículos
    if numero_placa in estacionamento:
        # Remove o veículo do dicionário
        del estacionamento[numero_placa]
        print(f"Veículo de placa {numero_placa} retirado com sucesso.")
    else:
        print("Veículo não encontrado.")

def listar_veiculos(estacionamento):
    """
    Função que lista todos os veículos atualmente estacionados.
    
    Args:
        estacionamento (dict): Dicionário contendo os veículos estacionados.
    """
    # Verifica se há veículos no dicionário
    if estacionamento:
        print("\nVeículos estacionados:")
        # Itera sobre os veículos no dicionário e imprime as informações
        for numero_placa, detalhes in estacionamento.items():
            print(f"Placa: {numero_placa}, Marca: {detalhes['marca']}, Modelo: {detalhes['modelo']}, Cor: {detalhes['cor']}, Proprietário: {detalhes['proprietario']}")
    else:
        print("Não há veículos estacionados.")

def verificar_veiculo(estacionamento):
    """
    Função que verifica se um veículo com uma determinada placa está estacionado.
    
    Args:
        estacionamento (dict): Dicionário contendo os veículos estacionados.
    """
    # Solicita a placa do veículo
    numero_placa = input("Digite a placa do veículo: ")
    # Verifica se a placa está no dicionário de veículos
    if numero_placa in estacionamento:
        print(f"O veículo de placa {numero_placa} está estacionado.")
    else:
        print(f"O veículo de placa {numero_placa} não está estacionado.")

def principal():
    """
    Função principal que inicializa o sistema de estacionamento e controla o loop principal.
    """
    # Dicionário para armazenar os veículos, já inicializado com um veículo
    estacionamento = {
        "AKL3720": {
            "marca": "Chevrolet",
            "modelo": "Monza",
            "cor": "Preto",
            "proprietario": "Alan De Cezare"
        }
    }

    # Loop principal do programa
    while True:
        # Exibe o menu de opções
        exibir_menu()
        # Solicita ao usuário que escolha uma opção
        opcao = input("Escolha uma opção: ")
        
        # Verifica a opção escolhida pelo usuário
        if opcao == '1':
            # Chama a função para estacionar um veículo
            adicionar_veiculo(estacionamento)
        elif opcao == '2':
            # Chama a função para retirar um veículo
            remover_veiculo(estacionamento)
        elif opcao == '3':
            # Chama a função para listar os veículos estacionados
            listar_veiculos(estacionamento)
        elif opcao == '4':
            # Chama a função para verificar se um veículo está estacionado
            verificar_veiculo(estacionamento)
        elif opcao == '0':
            # Encerra o programa
            print("Saindo do programa.")
            break
        else:
            # Informa que a opção escolhida é inválida
            print("Opção inválida. Tente novamente.")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    principal()
