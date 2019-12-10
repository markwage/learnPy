import func

list1 = ('item1', 'item2', 'item3', 'item4')
print('1 - ', list1[:])
print('2 - ', list1)
print('3 - ', list1[0], " - en laatste twee items -", list1[2:4])
#
func.conndb("Parameter")
#
vermenigvuldig = func.bereken(3, 3)
print('Uitkomst: ', vermenigvuldig)
#
func.defaultValue('eenWaarde')

func.keywordsArgs(car='Opel')
func.keywordsArgs('Jan', 'Chinees', 'Ford')
func.keywordsArgs(name='Joop')

func.varArgs(3)
func.varArgs(3, 18, 327)
func.varArgs(12, 36, 9786, 22453)

dataIn = [59, 6, 12]
func.healthCalculator(dataIn[0], dataIn[1], dataIn[2])
func.healthCalculator(*dataIn)