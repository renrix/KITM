import argparse
import json
import random

parser = argparse.ArgumentParser()
parser.add_argument("-f", help="Inventoriaus failo pavadinimas", required=True)
args = parser.parse_args()

prekės = ['obuoliai', 'kriaušės', 'bulvės', 'pomidorai', "mandarinai", "vyšnios", 'apelsinai']
inventoriai = {}
pirkėjai = {}

for i in range(1, 11):
    parduotuvės_pavadinimas = f"parduotuvė_{i}"
    inventoriai[parduotuvės_pavadinimas] = {}

    atsitiktinės_prekės = random.choices(prekės, k=4)
    for prekė in atsitiktinės_prekės:
        inventoriai[parduotuvės_pavadinimas][prekė] = {"kiekis": random.randint(3, 100),
                                                       "kaina": random.randint(100, 300) / 100.0}

with open(f"{args.f}_inventorius.json", 'w', encoding='utf-8') as fout:
    fout.write(json.dumps(inventoriai, indent=2, ensure_ascii=False))

for i in range(1,4):
    pirkėjai[f"pirkėjas_{i}"] = {
        prekė: kiekis
        for prekė, kiekis in zip(random.choices(prekės, k=3), [random.randint(1, 10) for _ in range(3)])
    }

with open(f"{args.f}_pirkėjai.json", 'w', encoding='utf-8') as fout:
    fout.write(json.dumps(pirkėjai, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    pass
