from Jatekos import Jatekos

class Jatekter:
    def __init__(self) -> None:
        self.kor=1
        self.harcos=Jatekos("Pöröly Pisti",0,"harcos","🤺")
        self.varazslo=Jatekos("Zúzós Zoltán",2,"varazslo","🧙‍♀️")
        self.lista=["_","_","_"]
        self.lista[self.harcos.poz]=self.harcos.emo
        self.lista[self.varazslo.poz]=self.varazslo.emo
        self.kor = 1
        self.kiir()

    def kiir(self):
        print(f"{self.kor}. kör")
        print("*"*15,"  ","-"*23,"  ","-"*25,"  ")
        print(f"* {self.list[0]:<3} {self.list[1]:^3} {self.list[2]:>3} *   | A {self.harcos.nev} életereje: {self.harcos.eletero} |  | A {self.varazslo.nev} életereje: {self.varazslo.eletero} |")
        print("*"*15,"  ","-"*23,"  ","-"*25,"  ")
        print("")

    def jatekmenet(self):
        while (self.harcos.hp>0 and self.varazslo.hp >0): 
            self.harcos.set_poz() # lepett a harcos
            self.varazslo.set_poz() # lepett a varazslo
            self.lista=["_","_","_"]
            self.lista[self.harcos.poz]=self.harcos.emo
            self.lista[self.varazslo.poz]=self.varazslo.emo
            if(self.harcos.poz == self.varazslo.poz):
                self.lista[self.varazslo.poz]="⚔"
                self.harcos.set_hp()
                self.varazslo.set_hp()
            n+=1
            self.kiir(n)
            input()