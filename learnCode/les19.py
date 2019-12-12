import func

# les 19 - sets

een_list = ('bier', 'sla', 'melk', 'bier', 'koffie')
een_set = {'bier', 'sla', 'melk', 'bier', 'koffie'}

print(een_list)
print(een_set)

# les 20 - Dictionary
car_brands = {'Mark': 'Opel', 'Jan': 'Ford', 'Piet': 'Volvo', 'Karel': 'Skoda'}
print(car_brands)
print(car_brands['Jan'])
for k, v in car_brands.items():
    if v is 'Volvo':
        print('We hebben een Volvo-rijder:', k)
    else:
        print(k, v)

func.write_logrecord("INFO", "Dit is een logrecord weggeschreven om te testen")

