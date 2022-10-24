class medic:
    def __init__(self,nume,prenume,post):
        self.nume=nume
        self.prenume=prenume
        self.post=post
    def modifNume(self,nume):
        self.nume=nume;
        
class spital:
    def __init__(self,nume,numar_medici,specializare,medici):
        self.nume=nume
        self.numar_medici=numar_medici
        self.specializare=specializare
        self.medici=medici
    def afisMedici(self):
        for m in medici:
            print(m.nume+" "+m.prenume)
        
medici=[medic("Popa","Gigi","chirurg"),medic("Ciobanu","Nelu","oftalmolog")]

s=spital("SPJT",2,"chirurgie",medici)

print(s.nume)
s.afisMedici();
s.medici[1].modifNume("Chirila")
s.afisMedici()
