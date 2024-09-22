#gry
#demontracja tworzenia modulu

class Player(object):
    """uczestnik gry"""
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
        
    def __str__ (self):
        rep = self.name + ":\t" + str(self.score)
        return rep
    
def ask_yes_no(question):
    """zadaj pytanie na ktore mozna odpowiedziec tak lub nie"""
    response = None
    while response not in ("t", "n"):
        response = input(question.lower())
        return response

def ask_number(question, low, high):
    """popros o numer z okreslonego zakresu"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
    
if __name__=="__main__":
    print("uruchomiles ten modul bezposrednio zamiast go zimportowac")
    input("aby zakonczyc program nacisnij enter")