import json
import os

repertoire = '/home/daugustin/PycharmProjects/git_fil_rouge/FilRouge_indus/fil_rouge/game/'
games = []

for nom in os.listdir(repertoire):
    with open('/home/daugustin/PycharmProjects/git_fil_rouge/FilRouge_indus/fil_rouge/game/' + nom, "r") as f:
        fichier = f.read()
        game = json.loads(fichier)
        print(game)
        games.append(game)

nb_party = {}

for element in games:
    date = element["Start time"][:8]
    if date in nb_party.keys():
        nb_party[date] += 1
    else:
        nb_party[date] = 1
print(nb_party)


for element in games:
    type_jeu = element['Machine name']
    tps_jeu_depA = int(element["Start time"][5:])
    tps_jeu_arriveA = int(element["End time"][5:])
    tps_jeu_depB = element["Start time"][5:]
    tps_jeu_arriveB = element["End time"][5:]
    if type_jeu is 'A':
        temps_moy_jeu1 = tps_jeu_arriveA - tps_jeu_depA
        print(temps_moy_jeu1)
