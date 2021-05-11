import bottle, model

SECRET = 'SKRIVNOSTNA KODA'

vislice = model.Vislice()

@bottle.get('/')
def zacetna_stran():
    return bottle.template('views/index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    id = vislice.nova_igra()
    bottle.response.set_cookie('id_igre', id, path='/', secret=SECRET)
    return bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    id = bottle.request.get_cookie('id_igre', secret=SECRET)
    igra, stanje = vislice.igre[id]
    return bottle.template('views/igra.tpl', igra=igra, stanje=stanje)

@bottle.post('/igra/')
def ugibaj():
    id = bottle.request.get_cookie('id_igre', secret=SECRET)
    crka = bottle.request.forms.get('crka')
    vislice.ugibaj(id, crka)
    return bottle.redirect(f'/igra/')

@bottle.get('/img/<picture>')
def pokazi_sliko(picture):
    return bottle.static_file(picture, root='img/')

bottle.run(reloader=True, debug=True)