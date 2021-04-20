STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+' 
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke = []):
        self.geslo = geslo.upper()
        self.crke = crke

    def napacne_crke(self):
        return [i.upper() for i in self.crke if i.upper() not in self.geslo]

    def pravilne_crke(self):
        return [i.upper() for i in self.crke if i.upper() in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return not self.poraz() and all(i in self.pravilne_crke() for i in self.geslo)

    def poraz(self):
        return STEVILO_DOVOLJENIH_NAPAK < self.stevilo_napak()

    def pravilni_del_gesla(self):
        geslo = ''
        for i in self.geslo:
            if i in self.crke:
                geslo += i
            else:
                geslo += '_'
        return geslo

    def nepravilni_del_gesla(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)        
        if crka in self.pravilne_crke():
            if self.zmaga():
                return ZMAGA
            return PRAVILNA_CRKA
        elif crka in self.nepravilni_del_gesla():
            if self.poraz():
                return PORAZ
            return NAPACNA_CRKA

with open('besede.txt', encoding='utf-8') as f:
    bazen_besed = f.read().split()

import random

def nova_igra():
    beseda = random.choice(bazen_besed)
    return Igra(beseda)