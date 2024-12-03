from deep_translator import GoogleTranslator
import requests as re
import time


URL = 'https://api.adviceslip.com/advice'
ad_list = {}

def ad_api():
    try:
        result = re.get(URL)
        id_ad = result.json()['slip']['id']
        ad_txt = result.json()['slip']['advice']
        return id_ad ,ad_txt


    except Exception as e:
        print(f'Error {e}')



def list_ad(id_ad, ad_txt):
    try:
        if id_ad not in ad_list:
            ad_list[id_ad] = ad_txt
            print("Conselho salvo com sucesso!")
        else:
            print("Conselho já salvo.")

    except Exception as erro:
        print(f'Erro encontrado: {erro}')



def show_ad():
    if ad_list:
        print("Conselhos salvos:")
        for id_ad, ad_txt in (ad_list.items()):
            print(f"ID: {id_ad} - Conselho: {ad_txt}")
    else:
        print("Nenhum conselho salvo. \n")

def save_txt():
    with open('advice.txt', 'a', encoding='UTF-8') as arquivo:
        for id_ad, ad_txt in (ad_list.items()):
            arquivo.write(f"ID: {id_ad} - Conselho: {ad_txt} \n")

def show_ad_from_txt():
    with open('advice.txt', 'r+', encoding='UTF-8') as arquivo:
        lines = arquivo.readlines()
        for i in lines:
            print(f'{i.strip()}')
            time.sleep(1)


def translate_ad_from_txt():
    with open('advice.txt', 'r+', encoding='UTF-8') as arquivo:
        shad = arquivo.readlines()
        for i in shad:
            frase = i.strip()
            traducao = GoogleTranslator(source='auto', target='portuguese').translate(frase)
            print(traducao)
            time.sleep(1)



def translate_ad():
    try:
        for id_ad, ad_txt in (ad_list.items()):
            traduzido = GoogleTranslator(source='en', target='pt').translate(ad_txt)
            print(f'Tradução:  Id: {id_ad} - {traduzido}')
    except Exception as e:
        print("Erro ao traduzir:", e)
        return None



if __name__ == '__main__':

    while True:
        print("\nMenu:")
        print("1. Buscar conselho")
        print("2. Mostrar conselhos salvos")
        print("3. Traduzir conselho salvo")
        print("4. Salvar conselhos em arquivo de texto")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_ad, ad_txt = ad_api()
            if id_ad and ad_txt:
                qtd = int(input('Quantos conselhos deseja receber? :  '))
                for i in range(qtd):
                    print(f"Conselho recebido: {ad_txt}")
                    salvar = input("Deseja salvar esse conselho? (s/n): \n").lower()
                    if salvar == "s":
                        list_ad(id_ad, ad_txt)
                    id_ad, ad_txt = ad_api()



        elif opcao == "2":
            escolha = int(input("Gostaria que seja mostrado os conselhos quem estão: \n 1- no Programa  \n 2- no Arquivo de texto? \n"))
            if escolha == 1:
                show_ad()
            elif escolha == 2:
                show_ad_from_txt()
            else:
                print("Numero invalido!")



        elif opcao == "3":
            op = int(input('Gostaria traduzir os conselhos da onde? : \n 1- no Programa  \n 2- no Arquivo de texto? \n'))
            if op == 1:
                show_ad()
                print('\n ~~~~~~~~~~~~ traduzido ~~~~~~~~~~ \n')
                translate_ad()
            elif op == 2:
                translate_ad_from_txt()
            else:
                print('Escolha inválida')


        elif opcao == "4":
            save_txt()
            print('Conselhos salvos com sucesso no arquivo "advices.txt" !')

        elif opcao == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida!")
