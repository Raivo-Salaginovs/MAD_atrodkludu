# Uzraksti programmu, kurā  dators izvēlas 100 skaitļus robežās
#  no  101 līdz 500. Izvēlētie skaitļi tiek izvadīti terminālī.

import random

# cik skaitļi jāizvēlas?
skaitlis=100

# kādas ir robežas?
min_rob=100
max_rob=501
# jāizveido cikls, jo jāģenerē 100 skaitļi

for i in range(100):
    random_skaitlis=random.randint(min_rob, max_rob)
    print(random_skaitlis)






