import func

# les 19 - sets

eenlist = ('bier', 'sla', 'melk', 'bier', 'koffie')
eenset = {'bier', 'sla', 'melk', 'bier', 'koffie'}

print(eenlist)
print(eenset)

# les 20 - Dictionary
carbrands={'Mark': 'Opel', 'Jan': 'Ford', 'Piet': 'Volvo'}
print(carbrands)
print(carbrands['Jan'])
for k, v in carbrands.items():
    print(k, v)

func.write_logrecord("INFO", "Dit is een logrecord weggeschreven om te testen")

