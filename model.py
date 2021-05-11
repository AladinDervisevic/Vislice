import random
import json

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+' 
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'
ZACETEK = 'Z'

class Igra:
    def __init__(self, geslo):
        self.geslo = geslo.upper()
        self.crke = []

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

class Vislice:
    datoteka_s_stanjem = 'stanje.json'

    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if not self.igre:
            return 0
        else:
            return max(self.igre) + 1

    def nova_igra(self):
        nov_id = self.prost_id_igre()
        self.igre[nov_id] = (nova_igra(), ZACETEK)
        return nov_id

    def ugibaj(self, id_igre, crka):
        igra, stanje = self.igre[id_igre]
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, stanje)

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, encoding='utf-8') as f:
            igre = json.load(f)
        for id_igre in igre:
            geslo = igre[id_igre]['geslo']
            crke = igre[id_igre]['crke']
            stanje = igre[id_igre]['stanje']
            igra = Igra(geslo)
            igra.crke = crke
            self.igre[int(id_igre)] = (igra, stanje)

    def zapisi_igre_v_datoteko(self):
        igre = {}
        for id_igre in self.igre:
            igra, stanje = self.igre[id_igre]
            igre[id_igre] = {'geslo': igra.geslo, 'crke': igra.crke, 'stanje': stanje}
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as f:
            json.dump(igre, f)

with open('besede.txt', encoding='utf-8') as f:
    bazen_besed = f.read().split()

def nova_igra():
    beseda = random.choice(bazen_besed)
    return Igra(beseda)