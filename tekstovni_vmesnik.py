import model

def izpis_igre(igra):
    return f'''
{igra.pravilni_del_gesla()}
    
Nepravilni ugibi: {igra.nepravilni_del_gesla()}
Zmotite se lahko še: {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}-krat'''

def izpis_zmage(igra):
    return f'Čestitke, uganili ste geslo {igra.geslo}!'

def izpis_poraza(igra):
    return f'Žal niste uganili gesla {igra.geslo}, več sreče drugič.'

def zahtevaj_vnos():
    return input('Ugibaj črko: ')

def pozeni_vmesnik():
    igra = model.nova_igra()

    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break
        elif stanje == model.PRAVILNA_CRKA:
            pass
        elif stanje == model.NAPACNA_CRKA:
            pass

pozeni_vmesnik()