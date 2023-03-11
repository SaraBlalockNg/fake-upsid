import pandas as pd

mapping = pd.read_csv('upsid_mapping.tsv',sep='\t')


# TODO ejectives may be an issue
languages = {
	'yiddish':['p','b','t','d',['t','ʲ'],['d','ʲ'],'k','ɡ','ʔ',
				'm','n',['n','ʲ'],'ŋ',
				'r','ɾ','ʀ',
				'f','v','s','z','ʃ','ʒ',['s','ʲ'],['z','ʲ'],'x','ɣ','h',
				'j','l','ʎ', # consonants
				['t','s'],['t','ʃ'],['t','s','ʲ'],['t','ʃ','ʲ'],
				['d','z'],['d','ʒ'],['d','z','ʲ'],['d','ʒ','ʲ'], # affricates
				'ɪ','ɛ','ɜ','a','ʊ','ɔ',['a','ɛ'],['ɛ','ɪ'],['ɔ','ɜ']
			],
	'english':['p','b','t','d','k','ɡ','m','n','ŋ',
			['t','ʃ'],['d','ʒ'],
			'f','v','s','z','ʃ','ʒ','χ','h','w','j','l','ɹ','θ','ð', # consonants
			'i','ɪ','e','ɛ','æ','ə','ɑ','ʌ','ʊ','o','u','ɚ', # plain vowels
			['a','ɪ'],['ɔ','ɪ'],['a','ʊ'], # diphthongs
		],
	'dutch':['p','b','t','d','c','k','ʔ','m','n','ɲ',
			'f','v','s','z','ʃ','ʒ','χ','ɦ','ɾ','j','l','ʋ', # consonants
			 'ɪ','ʏ','ɛ','ə','ɑ','ɔ','i','y','u', # plain vowels
			['i','ː'],['e','ː'],['a','ː'],['o','ː'],['y','ː'],
			['ø','ː'],['ɛ','ː'],['œ','ː'], # long vowels
			['ɛ','i'],['œ','y'],['ʌ','u'], # diphthongs
		]
}


def lookup(sound):
	try:
		return mapping.loc[mapping.IPA.eq(sound),'UPSID'].values[0]
	except Exception:
		import pdb;pdb.set_trace()

for language,inventory in languages.items():
	new_inventory = []
	# import pdb;pdb.set_trace()
	for sound in inventory:
		if type(sound) == list:
			# look up sounds individually and then concatenate
			temp = ''
			for s in sound:
				temp += lookup(s)
		else:
			temp = lookup(sound)
		new_inventory.append(temp)
	# import pdb;pdb.set_trace()
	instr = "','".join(new_inventory)
	print(f'{language}=[\'{instr}\']')
