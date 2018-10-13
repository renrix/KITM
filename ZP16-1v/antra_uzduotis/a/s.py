import argparse
import json
import random
from operator import itemgetter
itemtable = {}
pirkejai = {}
purchasebuffer = {}

translationtable = {
'obuoliai':'obuolius',
'kriauses':'kriauses',
'bulves':'bulves', 
'pomidorai':'pomidorus',
"mandarinai":'mandarinus',
"vysnios":'vysnias',
'apelsinai':'apelsinus'
}

with open("povilas_pirkejai.json", 'r') as fout:
	tmp = fout.read()
	pirkejai = json.loads(tmp)

with open("povilas_inventorius.json", 'r') as fout:
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
			if (pirkejai[pirkejas][prekes] > 0): #neexhaustinus loopo prasideda iteratoriaus nesamones :)
				kiek = min(pirkejai[pirkejas][prekes], preke['kiekis'])
				if(preke['kiekis']==0):
					continue
				preke['kiekis'] -= kiek
				pirkejai[pirkejas][prekes] -= kiek
				purchasebuffer[preke['p'] + prekes] = (preke['p'] + " nusipirko " + str(kiek) + " " + translationtable[prekes] + " po " + str(preke['kaina']))
	print(pirkejas + ":")
	for tmp in purchasebuffer:
		print(purchasebuffer[tmp])
	purchasebuffer = {}
