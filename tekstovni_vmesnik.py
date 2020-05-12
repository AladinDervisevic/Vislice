import model
import json

def izpis_igre(igra):
    besedilo = f'''GESLO : {igra.pravilni_del_gesla()}
Nepravilne črke: {igra.nepravilni_del_gesla()}
Zmotiš se lahko le še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()} ugibov.'''
    return besedilo

def izpis_zmage(igra):
    return f'\nČestitke, uganil/a si geslo: {igra.geslo} v {len(igra.crke)} ugibih.'

def izpis_poraza(igra):
    return f'\nŽal si izgubil/a igro. Geslo je bilo: {igra.geslo}'

def zahtevaj_vnos():
    vnos = input('Ugibaj: ')
    if len(vnos) == 1:
        return vnos
    else:
        return None

def pozeni_vmesnik():
    while True:
        igra = model.nova_igra()
        while True:
            print(izpis_igre(igra))

            crka = zahtevaj_vnos()
            while crka is None:
                print('Nepravilen vnos')
                crka = zahtevaj_vnos()

            stanje = igra.ugibaj(crka)

            if stanje == model.ZMAGA:
                print(izpis_zmage(igra))
                break
            elif stanje == model.PORAZ:
                print(izpis_poraza(igra))
                break
        print('Ali bi še enkrat igral/a?  (da / ne)')
        odgovor = input().lower()
        if odgovor == 'ne':
            break
        print('')

pozeni_vmesnik()