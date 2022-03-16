import banco
import uinterface

class player_register:
    def __init__(self, number_card, player_name, adress_player, start_date, number_choice_index, score, lucky_number):
        self.number_card = int(number_card)
        self.player_name = player_name
        self.adress_player = adress_player
        self.date = start_date
        self.number_choice_index = number_choice_index
        self.score = score
        self.lucky_number = lucky_number

# get lucky_number
    def get_lucky_number():
        drawn_number = get.drawn_number()

# calcula o score
    def calcule_score(list_index, score):
        for entry in list_index:
            if(entry == "lucky_number"):
                score += 1
    
    pass

#passar a classe ex: car_number = player_register()


# get pra pegar o dados do usuário do banco de dados, setar eles na variáveis da classe, processar os dados do usuário nas funções, depois que calcular
# deletar os dados antigos e inserir os novos com os dados atualizados