import sqlite3
from database import (
    create_tables,
    add_setor,
    update_setor,
    get_setores,
    add_demanda,
    update_demanda,
    get_demandas,
    add_veiculo,
    update_veiculo,
    get_veiculos,
    add_solicitacao,
    organizar_solicitacoes,
)

def exibir_menu_principal():
    while True:
        print("\nSistema de Solicitação de Transporte")
        print("1 - Gerenciar Setores")
        print("2 - Gerenciar Veículos")
        print("3 - Solicitar Transporte e Ver Solicitações")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            exibir_menu_setores()
        elif opcao == 2:
            exibir_menu_veiculos()
        elif opcao == 3:
            exibir_menu_solicitacoes()
        elif opcao == 0:
            break
        else:
            print("Opção inválida! Tente novamente.")

def exibir_menu_setores():
    while True:
        print("\nSetores")
        print("1 - Adicionar setor")
        print("2 - Editar setor")
        print("3 - Listar setores")
        print("4 - Gerenciar demandas")
        print("0 - Voltar")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            nome = input("Digite o nome do setor: ")
            add_setor(nome)
        elif opcao == 2:
            id_setor = int(input("Digite o ID do setor que deseja editar: "))
            novo_nome = input("Digite o novo nome do setor: ")
            update_setor(id_setor, novo_nome)
        elif opcao == 3:
            setores = get_setores()
            print("\nSetores:")
            for id_setor, nome in setores:
                print(f"{id_setor}: {nome}")
        elif opcao == 4:
            setor_id = int(input("Digite o ID do setor para gerenciar demandas: "))
            exibir_menu_demandas(setor_id)
        elif opcao == 0:
            break
        else:
            print("Opção inválida! Tente novamente.")

def exibir_menu_demandas(setor_id):
    while True:
        print("\nDemandas")
        print("1 - Adicionar demanda")
        print("2 - Editar demanda")
        print("3 - Listar demandas")
        print("0 - Voltar")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            descricao = input("Digite a descrição da demanda: ")
            prioridade = input("Digite a prioridade da demanda (Muito Urgente, Urgente, Normal): ")
            add_demanda(setor_id, descricao, prioridade)
        elif opcao == 2:
            demanda_id = int(input("Digite o ID da demanda que deseja editar: "))
            nova_descricao = input("Digite a nova descrição da demanda: ")
            nova_prioridade = input("Digite a nova prioridade da demanda (Muito Urgente, Urgente, Normal): ")
            update_demanda(demanda_id, setor_id, nova_descricao,            nova_prioridade)
        elif opcao == 3:
            demandas = get_demandas(setor_id)
            print("\nDemandas:")
            for id_demanda, descricao, prioridade in demandas:
                print(f"{id_demanda}: Descrição: {descricao}, Prioridade: {prioridade}")
        elif opcao == 0:
            break
        else:
            print("Opção inválida! Tente novamente.")

def exibir_menu_veiculos():
    while True:
        print("\nVeículos")
        print("1 - Adicionar veículo")
        print("2 - Editar veículo")
        print("3 - Listar veículos")
        print("0 - Voltar")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            placa = input("Digite a placa do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            tipo = input("Digite o tipo do veículo (Pickup, Convencional, Van): ")
            lotacao = int(input("Digite a lotação do veículo: "))
            motorista = input("Digite o nome do motorista: ")
            add_veiculo(placa, modelo, tipo, lotacao, motorista)
        elif opcao == 2:
            id_veiculo = int(input("Digite o ID do veículo que deseja editar: "))
            nova_placa = input("Digite a nova placa do veículo: ")
            novo_modelo = input("Digite o novo modelo do veículo: ")
            novo_tipo = input("Digite o novo tipo do veículo (Pickup, Convencional, Van): ")
            nova_lotacao = int(input("Digite a nova lotação do veículo: "))
            novo_motorista = input("Digite o novo nome do motorista: ")
            update_veiculo(id_veiculo, nova_placa, novo_modelo, novo_tipo, nova_lotacao, novo_motorista)
        elif opcao == 3:
            veiculos = get_veiculos()
            print("\nVeículos:")
            for id_veiculo, placa, modelo, tipo, lotacao, motorista in veiculos:
                print(f"{id_veiculo}: Placa: {placa}, Modelo: {modelo}, Tipo: {tipo}, Lotação: {lotacao}, Motorista: {motorista}")
        elif opcao == 0:
            break
        else:
            print("Opção inválida! Tente novamente.")

def exibir_menu_solicitacoes():
    while True:
        print("\nSolicitações de Transporte")
        print("1 - Solicitar transporte")
        print("2 - Ver solicitações organizadas")
        print("0 - Voltar")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            setor_id = int(input("Digite o ID do setor: "))
            demanda_id = int(input("Digite o ID da demanda: "))
            grande_volume = input("Haverá um grande volume? (s/n): ").lower() == 's'
            horario = input("Digite o horário da solicitação (HH:MM): ")
            tempo_estimado = int(input("Digite o tempo estimado em minutos para concluir a demanda: "))
            add_solicitacao(setor_id, demanda_id, grande_volume, horario, tempo_estimado)
        elif opcao == 2:
            solicitacoes_organizadas = organizar_solicitacoes()
            print("\nSolicitações de Transporte Organizadas:")
            for id_solicitacao, setor, demanda, prioridade, grande_volume, horario, tempo_estimado, placa, modelo, tipo, lotacao, motorista in solicitacoes_organizadas:
                print(f"{id_solicitacao}: Setor: {setor}, Demanda: {demanda}, Prioridade: {prioridade}, Grande Volume: {grande_volume}, Horário: {horario}, Tempo Estimado: {tempo_estimado} min, Veículo: {placa} ({modelo}, {tipo}, Lotação: {lotacao}), Motorista: {motorista}")
        elif opcao == 0:
            break
        else:
            print("Opção inválida! Tente novamente.")

def main():
    create_tables()
    exibir_menu_principal()

if __name__ == "__main__":
    main()