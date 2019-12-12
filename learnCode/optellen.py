uren = 0
input_uren = 0
while input_uren !=9999:
    input_uren = int(input('Geef het aantal uren (9999=stop)'))
    if input_uren != 9999:
        uren += input_uren
    print(uren)