# Text 4 // Same algorithm as in Text 1

# Time period: 1866

import random

emperor_name = ['Yuri-Ivan the III', 'Elizaveta the II', 'Anna Ionovna']
war_state = ['Japanese Empire', 'Chinese Empire', 'Prussia', 'Austrian Empire']
profit = ['water', 'oil', 'crops', 'animals', 'organs', 'marriages', 'land', 'debt']


print("In the end of the nineteenth century, most of the land was under the %s's rule." % random.choice(emperor_name), end = " ")
print("It was also the time when the war with the %s had begun." % random.choice(war_state), end = " ")
print("The people of the nation have mainly profitted out of %s." % random.choice(profit))
