from payment import Payment

class Card(Payment):
    card_number = int
    card_date = str
    cvv = int

    def __init__(self, id, card_number, card_date, cvv):
        super().__init__(id)
        self.card_number = card_number
        self.card_date = card_date
        self.cvv = cvv