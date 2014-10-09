import urlparse

FILTER_PARTIALS = True

FILTER = [
    '.DS_Store',
    'webassets-cache/*',
    '.webassets-cache',
    'layout.html',
]

INCLUDE = [

]

currency = '&euro;'

_hotels = [
    {'name': 'Hotel Trentina',
     'stars': 2,
     'price': (50, 90),
     'phone': '+39 02 2361208',
     'fax': '+39 02 2361297',
     'address': 'Via Filippino Lippi, 50',
     'url': 'http://www.htrentina.it/'},

    {'name': 'Hotel Lombardia',
     'stars': 3,
     'address': 'Viale Lombardia 74',
     'phone': '+39 02 2892515',
     'fax': '+39 02 2893430',
     'url': 'http://www.hotellombardia.com',
     'price': (60, 90)},

    {'name': 'Oasi Village Hotel Resort',
     'stars': 3,
     'price': (90, 100),
     'phone': '+39 02 23951472',
     'fax': '+39 02 70606666',
     'address': 'Viale Lombardia, 20',
     'url': 'http://www.oasivillagehotel.it/'},

    {'name': 'Hotel Sanpi',
     'stars': 4,
     'price': (130, 160),
     'phone': '+39 02 29513341',
     'fax': '+39 02 29402451',
     'address': 'Via Lazzaro Palazzi, 18',
     'url': 'http://www.hotelsanpimilano.it/'},

    {'name': 'Hotel San Francisco',
     'stars': 3,
     'address': 'Viale Lombardia, 55',
     'phone': '+39 02 2360302',
     'price': (90, 100),
     'url': 'http://www.hotel-sanfrancisco.it/'},

    {'name': 'Hotel Lugano',
     'stars': 3,
     'address': 'Via Astolfo, 6',
     'phone': '+39 02 266 3000',
     'price': (60, 70),
     'url': 'http://luganohotel.net/en/index.asp'},

    {'name': 'Hotel Gamma',
     'stars': 3,
     'price': (80, 100),
     'phone': '+39 02 26413152',
     'fax': '+39 02 2640255',
     'address': 'Via Valvassori Peroni 85',
     'url': 'http://hotelgammamilano.it/en/'},

    {'name': 'Hotel Dieci',
     'stars': 4,
     'price': (90, 170),
     'address': 'Largo Rio de Janeiro, 12',
     'phone': '+39 02 70608180',
     'fax': '+39 02 26684206',
     'url': 'http://www.hoteldieci.it/site_en.html'},

    {'name': 'Hotel Radisson',
     'stars': 4,
     'price': (100, 150),
     'address': 'Via Villapizzone 24',
     'phone': '+39 02 3631 8044',
     'fax': '+39 02 3631 8049',
     'url': 'http://www.radissonblu.com'},

    {'name': 'Best Western Hotel Galles',
     'stars': 4,
     'price': (150, 250),
     'address': 'Piazza Lima 2',
     'phone': '+39 02 204841',
     'fax': '+39 02 2048422',
     'url': 'http://www.galles.it/en/home-page.aspx'},

    {'name': 'Zefiro Hotel',
     'price': (90, 180),
     'stars': 4,
     'address': 'Via G. Gallina, 12',
     'phone': '+39 02 70005654',
     'fax': '+39 02 713811',
     'url': 'http://www.hotelzefiro.it/english/contact/'},

    {'name': 'Hotel Palazzo delle Stelline',
     'stars': 3,
     'address': 'Corso Magenta 61',
     'phone': '+39 02 4818431',
     'fax': '+39 0248194281',
     'url': 'http://hotelpalazzostelline.it',
     'price': (90, 160)},

    {'name': 'Hotel Mediolanum',
     'stars': 4,
     'price': (130, 160),
     'phone': '+39 02 6705312',
     'fax': '+39 02 66981921',
     'address': 'Via Mauro Macchi, 1',
     'url': 'http://www.mediolanumhotel.it'},

    {'name': 'Ibis Milano Centro',
     'stars': 3,
     'address': 'Via Camillo Finocchiaro Aprile, 2',
     'phone': '+30 02 63151',
     'price': (70, 90),
     'url': 'http://www.ibis.com/gb/hotel-0933-ibis-milano-centro/index.shtml'},

    {'name': 'Hotel NH Milano Machiavelli',
     'stars': 4,
     'address': 'Via Lazzaretto, 5',
     'phone': '+39 02 631141',
     'price': (120, 140),
     'url': 'http://www.nh-hotels.it/hotel/nh-milano-machiavelli'},

    {'name': 'NH Milano Touring',
     'stars': 4,
     'address': 'Via Ugo Tarchetti, 2',
     'phone': '+39 02 63351',
     'price': (140, 180),
     'url': 'http://www.nh-hotels.com/nh/en/hotels/italy/milan/nh-milano-touring.html'},

    {'name': 'Best Western Hotel Madison Milano',
     'stars': 4,
     'price': (100, 130),
     'address': 'Via Leopoldo Gasparotto, 8',
     'phone': '+39 02 6707 4150',
     'url': 'http://www.madisonhotelmilano.com/'},

    {'name': 'Hotel Albert',
     'stars': 3,
     'price': (80, 110),
     'phone': '+39 02 66985446',
     'fax': '+39 02 66985624',
     'address': 'Via Tonale 2',
     'url': 'http://www.alberthotel.it/en/'},
]

hotels = []
for h in _hotels:
    c = h.copy()
    c.update({'domain': urlparse.urlparse(h['url']).hostname})
    hotels.append(c)
