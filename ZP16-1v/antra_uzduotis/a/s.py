import argparse
import json
import random
from operator import itemgetter
itemtable = {}
pirkejai = {}

with open("edvardas_pirkejai.json", 'r') as fout:
	tmp = fout.read()
	pirkejai = json.loads(tmp)

with open("edvardas_inventorius.json", 'r') as fout:
	tmp = fout.read()
	inventorius = json.loads(tmp)

for parduotuve in inventorius:
	for preke in inventorius[parduotuve]:
		inventorius[parduotuve][preke]['p'] = parduotuve
		itemtable[preke] = itemtable.get(preke,[]) + [inventorius[parduotuve][preke]]

for tosort in itemtable:
	itemtable[tosort] = sorted(itemtable[tosort],key=lambda l:l['kaina'])

for pirkejas in pirkejai:
	for prekes in pirkejai[pirkejas]:
		for preke in itemtable[prekes]:
			kiek = min(pirkejai[pirkejas][prekes], preke['kiekis'])
			if(kiek==0):
				break
			preke['kiekis'] -= kiek
			pirkejai[pirkejas][prekes] -= kiek
			print(pirkejas + " nusipirko " + str(kiek) + " " + prekes + " is " + preke['p'] + " uz " + str(kiek*preke['kaina']) + "(" + str(preke['kaina']) + ")")