import json
import os

repertoire = '/home/daugustin/PycharmProjects/git_fil_rouge/FilRouge_indus/fil_rouge_json/'


for nom in os.listdir(repertoire):
    if nom == '*.json':
        with open('/home/daugustin/PycharmProjects/git_fil_rouge/FilRouge_indus/fil_rouge_json/' + nom, "r") as f:
            fichier = f.read()
            game = json.loads(fichier)
            print(game)
