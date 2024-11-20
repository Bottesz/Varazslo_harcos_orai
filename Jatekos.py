import random

class Jatekos:
    def __init__(self,nev:str="Jatekos",poz:int=0,kaszt:str="Harcos",emo:str="H"):
        
        self.emo=emo
        self.nev=nev
        self.hp=3+random.randint(1,6)
        self.kaszt=kaszt
        self.poz=poz



    def set_poz(self):
        self.poz=random.randint(0,2)


    def set_hp(self):
        self.hp=self.hp-random.randint(0,2)

    def __str__(self):
        return f"Játékos neve: {self.nev}"f" Életerő: {self.hp} "f" Kaszt: {self.kaszt} "f" Pozíció: {self.poz} "f" Emoji: {self.emo} "
              