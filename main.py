import repository
import time
from os import system, name
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

ad_saved_list = {}

#     OPTION 1 - Buscar conselhos
def search_for_advice(qnt):
    for i in range(qnt):
        id_ad, txt_ad = repository.get_translated_advice()
        print(f"\nConselho recebido: {txt_ad}\n")
        salvar = input("Deseja salvar esse conselho? (s/n): ").lower()
        if salvar == "s":
            save_ad(id_ad, txt_ad)

# adciona na lista da memoria
def save_ad(id_ad, txt_ad):
    try:
        if id_ad not in ad_saved_list:
            ad_saved_list[id_ad] = txt_ad
            print("Conselho salvo com sucesso!")
        else:
            print("Conselho já salvo.")
    except Exception as erro:
        print(f'Erro encontrado: {erro}')


#    OPTION 2 Mostrar conselhos
def show_saved_ads(choice):
    if choice == 1:
        show_ad_from_list()
    elif choice == 2:
        show_ad_from_file()
    else:
        print("Numero invalido!")

# mostra na lista da memoria
def show_ad_from_list():
    if ad_saved_list:
        print("\nConselhos salvos:\n")
        print_ads(ad_saved_list.items())
    else:
        print("\nNenhum conselho salvo.\n")

# pego do arquivo e printa
def show_ad_from_file():
    try:
        ads = repository.read_advice_from_file()
        if ads:
            print("\nConselhos salvos:\n")
            print_ads(ads.items())
        else:
            print("\nNenhum conselho salvo.\n")
    except Exception as erro:
        print(f'Erro encontrado: {erro}')

def print_ads(ads):
    for id_ad, txt_ad in ads:
        print(f"ID: {id_ad} - Conselho: {txt_ad}")

#   OPTION 3 - Traduzir conselhos
def show_translated_ads(choice):
    if choice == 1:
        translate_ad_from_list()
    elif choice == 2:
        translate_ad_from_file()
    else:
        print("Numero invalido!")

# Pega o que esta na memoria e traduz
def translate_ad_from_list():
    if not ad_saved_list:
        return print("\nNenhum conselho salvo\n")
    traduzidos = repository.translate_advice(ad_saved_list.items())
    for tras_txt in traduzidos:
        print(tras_txt)

# pega do arquivo e traduz
def translate_ad_from_file():
    try:
        from_file = repository.read_advice_from_file()
        if not from_file:
            return print("\nNenhum conselho salvo\n")

        result = repository.translate_advice(from_file.items())
        for adv_trans in result:
            print(adv_trans)
    except Exception as e:
        print(f'Erro encontrado: {e}')


#   OPTION 4 - Guardar conselhos em arquivo
def save_ads_to_file():
    if not ad_saved_list:
        return print("\nNenhum conselho salvo na lista para guardar. \n")
    try:
        repository.write_advice_to_file(ad_saved_list.items())
        print(f'Conselhos guardados no arquivo com sucesso')
        ad_saved_list.clear()
    except Exception as e:
        print(f'Erro ao salvar arquivo: {e}')

if __name__ == '__main__':
    print('\n========> Inicio do Programa <========\n')

    opcao = -1
    while opcao != 0:
        clear()
        print("\n Menu:")
        print("1. Buscar conselhos")
        print("2. Mostrar conselhos")
        print("3. Traduzir conselhos")
        print("4. Guardar conselhos em arquivo")
        print("0. Sair")
        opcao = int(input("\n Escolha uma opção: "))

        match opcao:
            case 1:
                print('\n==== Buscar conselho ====')
                qtd = int(input('Quantos conselhos deseja receber? :  '))
                search_for_advice(qtd)
                print('-------------------------')
            case 2:
                print('\n==== Mostrar conselhos salvos ====')
                escolha = int(input(
                    "Gostaria que seja mostrado os conselhos que estão: "
                    "\n 1- Salvos no Programa  "
                    "\n 2- Guardados no Arquivo? \n"))
                show_saved_ads(escolha)
                print('----------------------------------')
            case 3:
                print('\n==== Traduzir conselho salvo ====')
                escolha = int(input(
                    "Gostaria que seja traduzido os conselhos que estão: "
                    "\n 1- Salvos no Programa  "
                    "\n 2- Guardados no Arquivo? \n"))
                show_translated_ads(escolha)
                print('---------------------------------')
            case 4:
                print('\n==== Salvar conselhos em arquivo de texto ====')
                save_ads_to_file()
                print('----------------------------------------------')
            case 0:
                print('\n========> Fim do Programa <========\n')
            case _:
                print('Opção invalida')