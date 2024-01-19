import numpy as np

class Deck_of_Truco():
    cards = ['CA', 'C2', 'C3', 'C4', 'CJ', 'CQ', 'CK',
             'HA', 'H2', 'H3', 'H7', 'HJ', 'HQ', 'HK',
             'DA', 'D2', 'D3', 'D7', 'DJ', 'DQ', 'DK',
             'SA', 'S2', 'S3', 'SJ', 'SQ', 'SK']
    
    
    def __init__(self):
        self.__cards = Deck_of_Truco.cards
        self.shuffle_cards()
          
        
    def shuffle_cards(self):    
        if self.__cards:
            np.random.shuffle(self.__cards)
     
    
    def draw_hand(self):
        if self.__cards == []:
            print("All cards were drawn!")
            return
        else:
            hand_draw = np.random.choice(self.__cards, 3, replace = False) 
            
            self.__cards = [card for card in self.__cards
                            if card not in hand_draw]
            self.shuffle_cards()
            
            return hand_draw
    
    
    def reset_cards(self):
        self.__cards = Deck_of_Truco.cards