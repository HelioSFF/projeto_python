import service
FILE_NAME = "advices.txt"

def get_translated_advice():
    id_ad, txt_ad = service.get_advice_api()
    trans_txt_ad = service.get_translated_api(txt_ad)
    if id_ad and trans_txt_ad:
        return id_ad, trans_txt_ad
    else:
        return -1, "Ocorreu um erro ao obter o conselho"

def write_advice_to_file(ad_list):
    with open(FILE_NAME, 'a', encoding='UTF-8') as file:
        for id_ad, ad_txt in ad_list:
            file.write(f"ID: {id_ad} - Conselho: {ad_txt} \n")
        file.close()

def read_advice_from_file():
    adv_from_file = {}
    with open(FILE_NAME, 'r', encoding='UTF-8') as file:
        read = file.readlines()
        for line in read:
            adv_line = line.replace("ID:", "").replace("Conselho:","").strip().split(" - ")
            adv_from_file[adv_line[0]] = adv_line[1]
        file.close()
    return adv_from_file

def translate_advice(adv_list):
    result_list = []
    for id_ad, txt_ad in adv_list:
        result = service.get_original_api(txt_ad)
        if result:
            result_list.append(f'Tradução:  Id: {id_ad} - {result}')
        else:
            result_list.append(f'Tradução:  Id: {id_ad} - Erro ao traduzir')
    return result_list