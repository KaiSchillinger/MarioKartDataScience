import pandas as pd

data = {
    'Strecke': ['Mario Kart-Stadion', 'Marios Piste', 'Sonnenflughafen', 'Wolkenstraße', 'Kuhmuh-Weide (Wii)',
                'Staubtrockene Wüste (GCN)', 'Wario-Arena (DS)', 'Ticktack-Trauma (DS)', 'Yoshis Piste (GCN)',
                'Warios Goldmine (Wii)', 'Baby-Park (GCN)', 'Koopa-Großstadtfieber (3DS)', 'Wasserpark',
                'Toads Hafenstadt', 'Delfinlagune', 'Knochentrockene Dünen', 'Marios Piste (GBA)',
                'Donut-Ebene 3 (SNES)', 'Sorbet-Land (GCN)', 'Röhrenraserei (3DS)', 'Excitebike-Stadion',
                'Regenbogen-Boulevard (SNES)', 'Käseland (GBA)', 'Party-Straße (GBA)',
                'Zuckersüßer Canyon', 'Gruselwusel-Villa', 'Discodrom', 'Bowsers Festung', 'Cheep-Cheep-Strand (DS)',
                'Königliche Rennpiste (N64)', 'Instrumentalpiste (3DS)', 'Vulkangrollen (Wii)', 'Große Drachenmauer',
                'Polarkreis-Parcours', 'Wilder Wipfelweg', 'Marios Metro', 'Steinblock-Ruinen', 'Shy Guys Wasserfälle',
                'Wario-Abfahrt', 'Regenbogen-Boulevard', 'Toads Autobahn (N64)', 'DK Dschungel (3DS)', 'Yoshi-Tal (N64)',
                'Regenbogen-Boulevard (N64)', 'Mute City', 'Hyrule-Piste', 'Animal Crossing-Dorf', 'Big Blue',
                "Paris-Parcours (Tour)", "Toads Piste (3DS)", "Schoko-Sumpf (N64)", "Kokos-Promenade (Wii)",
                "Tokio-Tempotour (Tour)", "Pilz-Pass (DS)", "Wolkenpiste (GBA)", "Ninja-Dojo (Tour)",
                "New-York-Speedway (Tour)", "Marios Piste 3 (SNES)", "Kalimari-Wüste (N64)", "Waluigi-Flipper (DS)",
                "Sydney-Spritztour (Tour)", "Schneeland (GBA)", "Pilz-Schlucht (Wii)", "Eiscreme-Eskapade",
                "London-Tour (Tour)", "Buu-Huu-Tal (GBA)", "Gebirgspfad (3DS)", "Blätterwald (Wii)",
                "Pflaster von Berlin (Tour)", "Peachs Schlossgarten (DS)", "Bergbescherung (Tour)",
                "Regenbogen-Boulevard (3DS)", "Ausfahrt Amsterdam (Tour)", "Flussufer-Park (GBA)", "DK Skikane (Wii)",
                "Yoshis Eiland","Bangkok-Abendrot (Tour)", "Marios Piste (DS)", "Waluigi-Arena (GCN)",
                "Überholspur Singapur (Tour)","Athen auf Abwegen (Tour)", "Daisys Dampfer (GCN)",
                "Mondblickstraße (Wii)", "Bad-Parcours","Los-Angeles-Strandpartie (Tour)",
                "Sonnenuntergangs-Wüste (GBA)", "Koopa-Kap (Wii)", "Vancouver-Wildpfad (Tour)",
                "Rom-Rambazamba (Tour)", "DK-Bergland (GCN)", "Daisys Piste (Wii)", "Piranha-Pflanzen-Bucht (Tour)",
                "Stadtrundfahrt Madrid (Tour)", "Rosalinas Eisplanet (3DS)", "Bowsers Festung 3 (SNES)",
                "Regenbogen-Boulevard (Wii)"],

    'Cup': ['Pilz-Cup', 'Blumen-Cup', 'Stern-Cup', 'Spezial-Cup', 'Panzer-Cup', 'Bananen-Cup', 'Blatt-Cup',
            'Blitz-Cup', 'Ei-Cup', 'Triforce-Cup', 'Crossing-Cup', 'Glocken-Cup', 'Pilz-Cup', 'Blumen-Cup', 'Stern-Cup',
            'Spezial-Cup', 'Panzer-Cup', 'Bananen-Cup', 'Blatt-Cup', 'Blitz-Cup', 'Ei-Cup', 'Triforce-Cup',
            'Crossing-Cup', 'Glocken-Cup', 'Pilz-Cup', 'Blumen-Cup', 'Stern-Cup', 'Spezial-Cup', 'Panzer-Cup',
            'Bananen-Cup', 'Blatt-Cup', 'Blitz-Cup', 'Ei-Cup', 'Triforce-Cup', 'Crossing-Cup', 'Glocken-Cup',
            'Pilz-Cup', 'Blumen-Cup', 'Stern-Cup', 'Spezial-Cup', 'Panzer-Cup', 'Bananen-Cup', 'Blatt-Cup',
            'Blitz-Cup', 'Ei-Cup', 'Triforce-Cup', 'Crossing-Cup', 'Glocken-Cup', "Goldener Turbo-Cup",
            "Goldener Turbo-Cup", "Goldener Turbo-Cup", "Goldener Turbo-Cup",
            "Glückskatzen-Cup", "Glückskatzen-Cup", "Glückskatzen-Cup", "Glückskatzen-Cup",
            "Rüben-Cup", "Rüben-Cup", "Rüben-Cup", "Rüben-Cup", "Propeller-Cup", "Propeller-Cup", "Propeller-Cup",
            "Propeller-Cup", "Fels-Cup", "Fels-Cup", "Fels-Cup", "Fels-Cup", "Mond-Cup", "Mond-Cup", "Mond-Cup",
            "Mond-Cup", "Frucht-Cup", "Frucht-Cup", "Frucht-Cup", "Frucht-Cup", "Bumerang-Cup", "Bumerang-Cup",
            "Bumerang-Cup", "Bumerang-Cup", "Feder-Cup", "Feder-Cup", "Feder-Cup", "Feder-Cup", "Doppelkirschen-Cup",
            "Doppelkirschen-Cup", "Doppelkirschen-Cup", "Doppelkirschen-Cup", "Eichel-Cup", "Eichel-Cup", "Eichel-Cup",
            "Eichel-Cup", "Stachi-Cup", "Stachi-Cup", "Stachi-Cup", "Stachi-Cup"]
}
score = {'platz':[1,2,3,4,5,6,7,8,9,10,11,12],
         'punkte': [15,12,10,9,8,7,6,5,4,3,2,1]}

df_strecken = pd.DataFrame(data)
df_score = pd.DataFrame(score)

# CSV-Datei speichern
df_strecken.to_csv('strecken_cups.csv', index=False)
df_score.to_csv('scores.csv', index=False)

# print
print('Stecken:')
print(df_strecken)
print('Score:')
print(df_score)