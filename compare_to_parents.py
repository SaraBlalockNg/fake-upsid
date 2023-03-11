from inventories import *

import numpy as np
percents_in = []
percents_not_in = []
for language,parent in parents.items():
	c_inventory = set(dictionaries[dict_keys.index(language)])

	

	if type(parent) == list:
		p_inventory = set([sound for p in parent for sound in parent_inventories[p]])
	elif parent == 'n/a':
		continue
	else:
		p_inventory = set(parent_inventories[parent])

	c_in_parent = c_inventory.intersection(p_inventory)
	percent_in = len(c_in_parent)/len(c_inventory)
	print(f'{language}: {percent_in*100:.3f}% shared')
	percents_in.append(percent_in)
	percents_not_in.append(1-percent_in)
print(f'Average shared:{np.mean(percents_in)*100:.3f}%')
print(f'Average unique:{np.mean(percents_not_in)*100:.3f}%')
print(f'Min shared:{np.min(percents_in)*100:.3f}%')

