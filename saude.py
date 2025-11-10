import os
import time
from tabulate import tabulate
from datetime import datetime


class pacientes:
    lista = []

class medicos:
    lista = []


# Definindo a classe das cores e etc pra ficar bonitinho
class bcolors:
    CROXO = '\033[95m'
    CAZUL = '\033[94m'
    CCIANO = '\033[96m'
    CVERDE = '\033[92m'
    ENTRADA = '\033[93m'
    ERRO = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



# Limpa o terminal antes do uso
def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')



# Obtem a hora e minuto atual do sistema
def obter_hora():
    agora = datetime.now()
    agora_hora = agora.strftime("%H:%M")
    return agora_hora


# Obtem a data e hora atual do sistema
def obter_data():
    agora = datetime.now()
    agora_data = agora.strftime("%d/%m/%Y (%H:%M)")
    return agora_data


# Mostra dados do paciente atual
def mostrar_dadosPaciente(paciente_atual):
    print(bcolors.ENDC + "   " +bcolors.CAZUL + "ID "+str(pacientes.lista[paciente_atual].get("id")) + ": " + pacientes.lista[paciente_atual].get("nome") + "   <" + str(pacientes.lista[paciente_atual].get("medico")) + ">")
    print(bcolors.ENDC + "   " +bcolors.CAZUL + "Urgência "+str(pacientes.lista[paciente_atual].get("urgencia")) + "   <" + pacientes.lista[paciente_atual].get("data")+">")


# Menu inicial do programa
def menu_inicial():
    clear_console()

    print(bcolors.CROXO + """
=========================================
    Bem-vindo(a) ao sistema de saúde!
=========================================
""" + bcolors.ENDC + "          Horário atual: " + obter_hora() + """

    """ + bcolors.UNDERLINE + "1" + bcolors.ENDC +""": Gerenciamento de Pacientes
    """ + bcolors.UNDERLINE + "2" + bcolors.ENDC +""": Gerenciamento de Medicos
    """ + bcolors.UNDERLINE + "3" + bcolors.ENDC +""": Gerenciamento de Doencas
        
    """)
    menu = input(bcolors.ENTRADA + "> Selecione uma opção do menu: ")
    
    # Menu
    match menu:
        case "1":
            menu_pacientes()

        case "2":
            menu_medicos()

        # Fallback para caso seja digitado alguma opcao nao valida
        case _:
            print (bcolors.ERRO + "\n[!!!] Opção nao é válida!\n")
            input(bcolors.ENTRADA + "> Pressione qualquer tecla para voltar. ")
            menu_inicial()


# Menu de medicos
def menu_medicos():
    clear_console()

    print(bcolors.CROXO + """
=========================================
         Gerenciador de Medicos
=========================================
""" + bcolors.ENDC + "          Horário atual: " + obter_hora() + """

    """ + bcolors.UNDERLINE + "1" + bcolors.ENDC +""": Listar Medicos
    """ + bcolors.UNDERLINE + "2" + bcolors.ENDC +""": Adicionar Medico

    """ + bcolors.UNDERLINE + "v" + bcolors.ENDC +""": Voltar para o Menu Principal
        
    """)
    menu = input(bcolors.ENTRADA + "> Selecione uma opção do menu: ")

    # Teclado
    match menu:
        case "1":
            medico_listar()

        case "2":
            medico_adicionar()

        case "v":
            menu_inicial()

        # Fallback para caso seja digitado alguma opcao nao valida
        case _:
            print (bcolors.ERRO + "\n[!!!] Opção nao é válida!\n")
            input(bcolors.ENTRADA + "> Pressione qualquer tecla para voltar. ")
            menu_pacientes()


# Menu de pacientes
def menu_pacientes():
    clear_console()

    print(bcolors.CROXO + """
=========================================
         Gerenciador de Pacientes
=========================================
""" + bcolors.ENDC + "          Horário atual: " + obter_hora() + """

    """ + bcolors.UNDERLINE + "1" + bcolors.ENDC +""": Listar Pacientes
    """ + bcolors.UNDERLINE + "2" + bcolors.ENDC +""": Adicionar Paciente

    """ + bcolors.UNDERLINE + "v" + bcolors.ENDC +""": Voltar para o Menu Principal
        
    """)
    menu = input(bcolors.ENTRADA + "> Selecione uma opção do menu: ")

    # Teclado
    match menu:
        case "1":
            paciente_listar()

        case "2":
            paciente_adicionar()

        case "v":
            menu_inicial()

        # Fallback para caso seja digitado alguma opcao nao valida
        case _:
            print (bcolors.ERRO + "\n[!!!] Opção nao é válida!\n")
            input(bcolors.ENTRADA + "> Pressione qualquer tecla para voltar. ")
            menu_pacientes()


# Gera a lista de Pacientes com o tabulate
def pacientes_gerar_lista():
    table = tabulate(
        pacientes.lista,
        headers={"id":"ID", "nome":"Nome", "idade":"Idade", "urgencia":"Urgencia", "medico":"Médico Atribuído", "data":"Data de Entrada"},
        tablefmt="simple_grid")
    return table

# Gera a lista de Medicos com o tabulate
def medicos_gerar_lista():
    table = tabulate(
        medicos.lista,
        headers={"id":"ID", "nome":"Nome", "atuacao":"Atuação", "pacientes":"Pacientes", "data":"Data de Entrada"},
        tablefmt="simple_grid")
    return table
    

# Painel de listagem de pacientes
def paciente_listar():

    # Mostrar as açoes de paciente
    def paciente_acoesLista():
        clear_console()

        print(bcolors.CROXO + """
=========================================
         Gerenciador de Pacientes
=========================================
""" + bcolors.ENDC + "          Horário atual: " + obter_hora() + """
    """)

        mostrar_dadosPaciente(paciente_atual)

        print(bcolors.ENDC + "\n\n   " +bcolors.ENDC + bcolors.UNDERLINE + "1" + bcolors.ENDC + ": Atribuir Médico")
        print(bcolors.ENDC + "   " +bcolors.UNDERLINE + "2" + bcolors.ENDC + ": Agendar Consulta")
        print(bcolors.ENDC + "   " +bcolors.UNDERLINE + "3" + bcolors.ENDC + ": Remover da lista")
        print(bcolors.ENDC + "\n   " +bcolors.UNDERLINE + "v" + bcolors.ENDC + ": Voltar para o Gerenciador de Pacientes")

        menu = input(bcolors.ENTRADA + "\n\n> Selecione uma opção do menu: ")

        # Teclado
        match menu:
            case "1":
                pacientes_atriburMedico(paciente_atual)

            case "2":
                pacientes_agendarConsulta()
            
            case "3":
                pacientes_removerLista(paciente_atual)

            case "v":
                menu_pacientes()

            # Fallback para caso seja digitado alguma opcao nao valida
            case _:
                print (bcolors.ERRO + "\n[!!!] Opção nao é válida!\n")
                input(bcolors.ENTRADA + "> Pressione qualquer tecla para voltar. ")
                paciente_listar()


    clear_console()

    print(bcolors.CROXO + """
=========================================
         Gerenciador de Pacientes
=========================================
""" + bcolors.ENDC + "          Horário atual: " + obter_hora() + """

    """)

     # Caso há pacientes no banco de dados, mostre a lista e as açoes disponiveis
    if len(pacientes.lista) > 0:
        print(pacientes_gerar_lista())
        print(bcolors.CAZUL + " Listado todos os " + str(len(pacientes.lista)) + " pacientes.")

        print(bcolors.ENDC + "\n\n   " + bcolors.UNDERLINE + "ID" + bcolors.ENDC + ": Ações de paciente")
        print(bcolors.ENDC + "   " + bcolors.UNDERLINE + "v" + bcolors.ENDC + ": Voltar para o Gerenciador de Pacientes")

        menu = input(bcolors.ENTRADA + "\n\n> Selecione uma opção do menu: ")


        match menu:

            # Volta pro menu anterior
            case "v":
                menu_pacientes()
            
            case _:

                # Se paciente for valido abre as açoes do paciente
                if menu.isdigit() and int(menu) < len(pacientes.lista):
                    paciente_atual = int(menu)
                    paciente_acoesLista()

                # Se nao for valido, mostra um erro
                else:
                    print (bcolors.ERRO + "\n[!!!] Erro de entrada!\n")
                    input(bcolors.ENTRADA + "> Pressione qualquer tecla para voltar. ")

                    menu_pacientes()

    # Caso não há ninguem na lista, mostre a opçao de voltar ao menu anterior
    else:
        print(bcolors.CAZUL + "Não há pacientes no banco de dados!")
        input(bcolors.ENTRADA + "\n\n> Pressione qualquer tecla para voltar. ")
        menu_pacientes()


# Painel de adicioar pacientes
def paciente_adicionar():

    # Checa se o nome tem mais de 2 caracteres
    def paciente_checaNome(nome):
        return len(str(nome)) >= 2

    # Checa se a idade é maior que 0
    def paciente_checaIdade(idade):
        return idade.isdigit() and int(idade) >= 0
    
    # Checa se a urgencia esta entre 1 e 5
    def paciente_checaUrgencia(urgencia):
        return urgencia.isdigit() and int(urgencia) >= 1 and int(urgencia) <= 5
    
    # Em caso de erro, gera uma mensagem e volta para o menu anterior.
    def paciente_gerarError():
        print (bcolors.ERRO + "\n[!!!] Erro de entrada!\n")
        input(bcolors.ENTRADA + "> Pressione qualquer tecla para voltar. ")

        menu_pacientes()
    

    clear_console()

    print(bcolors.CROXO + """
=========================================
         Gerenciador de Pacientes
=========================================
""" + bcolors.ENDC + "          Horário atual: " + obter_hora() + """

    """)

    # Entrada dos dados do novo paciente
    paciente_nome = input(bcolors.ENTRADA + "> Nome do Paciente: ")
    if not paciente_checaNome(paciente_nome):
        paciente_gerarError()

    paciente_idade = input(bcolors.ENTRADA + "> Idade do Paciente: ")
    if not paciente_checaIdade(paciente_idade):
        paciente_gerarError()

    paciente_urgencia = input(bcolors.ENTRADA + "> Urgencia: ")
    if not paciente_checaUrgencia(paciente_urgencia):
        paciente_gerarError()

    # Se todos os dados estao OK, adicionar a lista
    pacientes.lista.append({"id":len(pacientes.lista),"nome":paciente_nome.title(),"idade":paciente_idade,"urgencia":paciente_urgencia,"medico":"Não Atribuído","data":obter_data()})

    print(bcolors.CAZUL + "Paciente adicionado com sucesso.")
    input(bcolors.ENTRADA + "\n\n> Pressione qualquer tecla para voltar. ")

    menu_pacientes()


# Atribuir medico
def pacientes_atriburMedico(paciente_atual):
    clear_console()

    print(bcolors.CROXO + """
=========================================
         Gerenciador de Pacientes
=========================================
""" + bcolors.ENDC + "          Horário atual: " + obter_hora() + """
    """)

    mostrar_dadosPaciente(paciente_atual)

    print("")
    if len(medicos.lista) > 0:
        for item in range(len(medicos.lista)):
            print("[" + str(item) + "] " + str(medicos.lista[item].get("nome")))
    else:
        print(bcolors.ERRO + "\n[!!!] Não há médicos no banco de dados!" + bcolors.ENDC)
    
    input(bcolors.ENTRADA + "\n\n> Pressione qualquer tecla para voltar. ")

    menu_pacientes()


# Agendar consulta
def pacientes_agendarConsulta():
    pass


# Remover paciente da lista de pacientes
def pacientes_removerLista(paciente_atual):
    clear_console()

    print(bcolors.CROXO + """
=========================================
         Gerenciador de Pacientes
=========================================
""" + bcolors.ENDC + "          Horário atual: " + obter_hora() + """
    """)

    mostrar_dadosPaciente(paciente_atual)

    print("")

    print(bcolors.ERRO + "\nVocê está prestes a apagar   \'" + pacientes.lista[paciente_atual].get("nome") + "\'   do banco de dados!" + bcolors.ENDC)
    
    print(bcolors.ENDC + "\n   " + bcolors.UNDERLINE + "1"+ bcolors.ENDC + ": Apagar paciente selecionado" + bcolors.ENDC)
    print(bcolors.ENDC + "   " + bcolors.UNDERLINE + "v" + bcolors.ENDC + ": Voltar ao menu anterior sem apagar." + bcolors.ENDC)

    menu = input(bcolors.ENTRADA + "\n\n> Selecione uma opção do menu: ")


    # Confirma se o usuario deseja remover o paciente
    match menu:
        case "1":
            paciente_apagado = pacientes.lista[paciente_atual].get("nome")
            del pacientes.lista[paciente_atual]
        case _:
            menu_pacientes()

            clear_console()

    print(bcolors.CROXO + """
=========================================
         Gerenciador de Medicos
=========================================
""" + bcolors.ENDC + "          Horário atual: " + obter_hora())
    print(bcolors.ERRO + "\n\n[!!!] \'" + paciente_apagado + "\' foi apagado do banco de dados!" + bcolors.ENDC)
    
    input(bcolors.ENTRADA + "\n\n> Pressione qualquer tecla para voltar. ")

    menu_pacientes()


# Painel de listagem de medicos
def medico_listar():

    # Mostrar as açoes de medicos
    def medico_acoesLista():
        clear_console()

        print(bcolors.CROXO + """
=========================================
         Gerenciador de Medicos
=========================================
""" + bcolors.ENDC + "          Horário atual: " + obter_hora() + """
    """)

        mostrar_dadosMedico(medico_atual)

        print(bcolors.ENDC + "\n\n   " +bcolors.ENDC + bcolors.UNDERLINE + "1" + bcolors.ENDC + ": Atribuir Médico")
        print(bcolors.ENDC + "   " +bcolors.UNDERLINE + "2" + bcolors.ENDC + ": Agendar Consulta")
        print(bcolors.ENDC + "   " +bcolors.UNDERLINE + "3" + bcolors.ENDC + ": Remover da lista")
        print(bcolors.ENDC + "\n   " +bcolors.UNDERLINE + "v" + bcolors.ENDC + ": Voltar para o Gerenciador de Pacientes")

        menu = input(bcolors.ENTRADA + "\n\n> Selecione uma opção do menu: ")

        # Teclado
        match menu:
            case "1":
                pacientes_atriburMedico(paciente_atual)

            case "2":
                pacientes_agendarConsulta()
            
            case "3":
                pass
                # medicos_removerLista(medico_atual)

            case "v":
                menu_medicos()

            # Fallback para caso seja digitado alguma opcao nao valida
            case _:
                print (bcolors.ERRO + "\n[!!!] Opção nao é válida!\n")
                input(bcolors.ENTRADA + "> Pressione qualquer tecla para voltar. ")
                medico_listar()


    clear_console()

    print(bcolors.CROXO + """
=========================================
         Gerenciador de Medicos
=========================================
""" + bcolors.ENDC + "          Horário atual: " + obter_hora() + """

    """)

     # Caso há pacientes no banco de dados, mostre a lista e as açoes disponiveis
    if len(pacientes.lista) > 0:
        print(medicos_gerar_lista())
        print(bcolors.CAZUL + " Listado todos os " + str(len(medicos.lista)) + " medicos.")

        print(bcolors.ENDC + "\n\n   " + bcolors.UNDERLINE + "ID" + bcolors.ENDC + ": Ações de medico")
        print(bcolors.ENDC + "   " + bcolors.UNDERLINE + "v" + bcolors.ENDC + ": Voltar para o Gerenciador de Medicos")

        menu = input(bcolors.ENTRADA + "\n\n> Selecione uma opção do menu: ")


        match menu:

            # Volta pro menu anterior
            case "v":
                menu_medicos()
            
            case _:

                # Se paciente for valido abre as açoes do paciente
                if menu.isdigit() and int(menu) < len(medicos.lista):
                    medico_atual = int(menu)
                    medico_acoesLista()

                # Se nao for valido, mostra um erro
                else:
                    print (bcolors.ERRO + "\n[!!!] Erro de entrada!\n")
                    input(bcolors.ENTRADA + "> Pressione qualquer tecla para voltar. ")

                    menu_medicos()

    # Caso não há ninguem na lista, mostre a opçao de voltar ao menu anterior
    else:
        print(bcolors.CAZUL + "Não há médicos no banco de dados!")
        input(bcolors.ENTRADA + "\n\n> Pressione qualquer tecla para voltar. ")
        menu_medicos()


# Painel de adicioar medicos
def medico_adicionar():

    # Checa se o nome tem mais de 2 caracteres
    def medico_checaNome(nome):
        return len(str(nome)) >= 2

    # Checa se a idade é maior que 0
    def medico_checaAtuacao(nome):
        return len(str(nome)) >= 2
    
    # Em caso de erro, gera uma mensagem e volta para o menu anterior.
    def medico_gerarError():
        print (bcolors.ERRO + "\n[!!!] Erro de entrada!\n")
        input(bcolors.ENTRADA + "> Pressione qualquer tecla para voltar. ")

        menu_medicos()
    

    clear_console()

    print(bcolors.CROXO + """
=========================================
         Gerenciador de Medicos
=========================================
""" + bcolors.ENDC + "          Horário atual: " + obter_hora() + """

    """)

    # Entrada dos dados do novo paciente
    medico_nome = input(bcolors.ENTRADA + "> Nome do Medico: ")
    if not medico_checaNome(medico_nome):
        medico_gerarError()

    # Entrada dos dados do novo paciente
    medico_atuacao = input(bcolors.ENTRADA + "> Atua em: ")
    if not medico_checaAtuacao(medico_atuacao):
        medico_gerarError()


    # Se todos os dados estao OK, adicionar a lista
    medicos.lista.append({"id":len(medicos.lista),"nome":medico_nome.title(),"atuacao":medico_atuacao,"pacientes":str(pacientes.lista.index),"data":obter_data()})

    print(bcolors.CAZUL + "Medico adicionado com sucesso.")
    input(bcolors.ENTRADA + "\n\n> Pressione qualquer tecla para voltar. ")

    menu_medicos()


# Chamar menu inical após definir todas as funçoes
menu_inicial()