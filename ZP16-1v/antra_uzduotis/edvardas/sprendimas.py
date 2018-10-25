import json
from collections import namedtuple

Sarasas = namedtuple("Sarasas",["parduotuve","preke","kiekis","kaina"])

with open("ZP16-1v/antra_uzduotis/edvardas_inventorius.json",'r',encoding='utf-8') as failas:
    inventorius = json.load(failas)

with open("ZP16-1v/antra_uzduotis/edvardas_pirkėjai.json",'r',encoding='utf-8') as failas:
    pirkėjai = json.load(failas)

sarasas = []
for parduotuve, pard_duom in inventorius.items():
    for preke, prekes_info in pard_duom.items():
        sarasas.append(Sarasas(parduotuve,preke,prekes_info['kiekis'],prekes_info['kaina']))