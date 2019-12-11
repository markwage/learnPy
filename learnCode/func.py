from datetime import datetime
# ==============================================================================
# Functions
# ==============================================================================
# ==============================================================================
# Write logrecord to logfile
# ==============================================================================
def write_logrecord(loglevel, logrecord):
    current_time = datetime.now()
    with open("application.log", "w") as log_file:
        log_file.write("%s %s %s" % (current_time, loglevel, logrecord))

# ==============================================================================
# Connect to the database
# ==============================================================================
def conndb(parm1):
    print("\nDeze parm is aan functie doorgegeven:", parm1)

def bereken(a, b):
    print('\n', a, b)
    uitkomst_verm = a * b
    return uitkomst_verm

def defaultValue(waarde='deDefaultWaarde'):
    if waarde is 'eenWaarde':
        print('Dit is niet de default')
    else:
        print('Dit is de default:', waarde)

def keywordsArgs(name='Mark', favfood='pasta', car='Peugeot'):
    print('Naam:', name, 'Favoriete voedsel', favfood, 'Automerk', car)

def varArgs(*allArgs):
    total = 0
    for nbr in allArgs:
        total += nbr
    print(total)

def healthCalculator(age, apples_ate, cigs_smoked):
    maxAge = (100 - age) + (apples_ate * 3.5) - (cigs_smoked * 2.5)
    print(maxAge)