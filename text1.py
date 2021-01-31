# Text 1
# Time period: 200 BC

import random

country_list = ['K*zakh-stan', 'K@z@kh-land', 'Qaz*qStepp*']
country_description = ['big', 'empty', 'large', 'enourmous', 'abanoded']
human_adjective = ['bold', 'crazy', 'creative', 'primitive']
country_name = random.choice(country_list)
group_name = ['Saka', 'Skythian', 'Massagetae']

print("Once upon a time, a country named %s was born..." % country_name)
print("The land so %s, only the %s could explore." % (random.choice(country_description), random.choice(human_adjective)))
print("Nevertheless, the %s people persisted." % random.choice(group_name))
