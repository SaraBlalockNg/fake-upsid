# storage for inventories of individual languages
# each phoneme is a dictionary key, and its value is a list containing
# the correct possible diacritic set

atlantean = ['p','b','t','d','k','g','m','n','r','s','S','x','j','l','w',
             'i','I','e','o','"@','E','O','a','ai','ei','oi']#done w/ ASCII

aui = ['p','b','t','d','k','g','m','n',
       'r','f','v','s','z','S','Z','x',
       'h','l','w', 'i','i{~}','y','y{~}','u','u{~}','I','I{~}',
       'U','U{~}','e','e{~}','o','o{~}','E','E{~}','E)','O','O{~}',
       'a','a{~}','aa{~}'] # done - found acceptable replacement -
      							 #missing a centralized, and a centralized & nasal

barsoomian = ['i','i:','u','u:','e','e:','o','o:','a','a:','p','p:',
	'b','b:','t','t:','d','d:','k','k:','g','g:','m','m:',
	'n','n:','f','f:','v','v:','0D','0D:','s','s:','z','z:',
	'x','x:','gF','gF:','h','h:','rA','rA:','j','j:','w','w:',
	'tS','tS:'] # done with ASCII

brithenig = ['p','b','t','d','k','g',
	'm','n','r','f','v','0D','6D',
	's','z','S','X','h','hlF','tS','dZ',
	'i','i_cen','I','U','"@','E','O','O:',
	'aa','a','a:','aI','aU','EI','aE','EU','iU','OE',
             'OI','uI'] # done with ASCII

dni = ['"@','?','v','b','t','s','S','dZ','g','j',
		'x','k','a_','aI','f','p','I','i','E','eI',
		'rA','m','6D','0D','d','h','oU','OI','tS','w',
		'"@','u','ts','l','aa','z','n']#done with ASCII + dipthongs


dothraki = ['a','tS','d','e','f','g','h',
            'i','dZ','k','x','lD','m','nD',
            'o','q','v','w','tD','0D','s',
            'z','r','r[','S','Z','j','H',
            'E','O','a_','u'] # done with ASCII

draconic = ['p','ph','b','f','f:','v','m','hw','w',
            't','th','d','0D','s','s:','sW','sW:','z','hlF',
            'S','S:','Z','n','l','rA','C','C:','jF',
            'nj','kx','i','i:','e','e:','u','u:',
            'j','k','kh','kW','g','x','gF','N',
            'q','qh','?','RF','h','R','dZ','o','o:',
            'a','a:','@','aa','I','I:','E','E:'] #  done with ASCII

eskayan = ['p','b','m','w','t','d','s','n','w','rA','tS','dz',
			'k','g','N','?','h','i','a','"@']#done with ASCII (no dipthongs)

esperanto =['m','n','p','b','d','ts','dz','f','s','v','z','Z','l','r','tS',
			'S','j','x','k','g','x','h','i','e','u','o','a','ai','oi','ei',
			'au','eu'] #done with ASCII & dipthongs

furbish = ['i','a','u','o','e','w','t','k',
			'l','n','d','b','m','j'] # with ASCII

golic_volcan = ['m','n','N','p','b','f','v',
                't','d','l','r[','s','z','0D',
                'S','Z','ts','tS','dZ','k',
                'g','X','h','?','"@','j',
                'w','i','i:','I','I:','u','u:','o','o:',
                'a','a:','O','E','E:','E9','4'] # done

interlingua = ['p', 'b','m','f','v','t','d','s','ts','tS','n','r[','z',
				'l','S','dZ','Z','j','w','k','g','h','i','e','a','u','o',
				'ai','au','ei','eu','oi']


ithkuil_revised = ['nD','dD','tD','tDh','tD\'','m','b','p','p\'',
		    'ph','v','6D','0D','dz','ts','tsh','ts\'','z','s',
		    'hlF','l','r.[','dZ','tS','tSh','tS\'','Z','S','C',
		    'j','N','g','k','kh','k\'','x','w','q','qh','q\'',
		    'X','RA','h','?\'','i','I','e','o/','3','"@','u+',
		    'a','u','U','o','O','a_','aI','3I','"@I','OI','E)I',
		    'UI','aU','3U','"@U','IU','OU','E)U'] #done with ASCII + dipthongs

klingon = ['ph','b','v','m','w','n','r','tlF','d.','l','s.',
			'tS','dZ','j','x','gF','N','qh','qX','?','a_','E',
			'I','o','u','a_j','Ej','Ij','oj','uj','a_w','Ew',
			'Iw']#done with ASCII + dipthongs

laadan = ['a_','3','I','o','u','m','b','w','n','d','0D','rA',
			'hlF','l','S','Z','j','h']#done with ASCII (no dipthongs)

loglan = ['a','e','i','o','u','j','w','E',
          'O','"@','b','S','Z','d','f','g',
          'h','k','l','m','n','p',
          'rA','s','t','v','z',
          'tS','dZ','0D','y','x'] # done with ASCII

lojban = ['m','n','p','b','f','v','m','t','d','s','z','l','S','Z',
		'r','k','g','x','?','h','i','E','a','"@','a','u','o',
		'ai','au','Ei','oi','ia','ie','ii','io','ua','u','ui'
		]#done with ASCII + dipthongs

navi = ['aU','aI','EU','EI''i','u','U','I','o','E','aa','a',
	'l','r','p',"p'",'t',"t'",'k',"k'",'?','f',
	's','v','z','h','m','n','ts','N',
	'r[','j','w'] # done with ASCII


quenya = ['m','p','b','f','v','hw','w','iu','eu','ai','au','oi','ui',
          'n','t','d','s','l','r','C',
          'j','N','k','g','x','h',
          'hlF','i','i:','u','u:','a','a:','e:','o:','E',
          'O'] # done, with ASCII for standard variety

sindarin = ['p','b','m','f','v','0D','6D',
	't','d','n','s','r','hlF','l','j',
	'k','g','N','x','w','h','hw','i','i:',
	'y','y:','a','y:','u','u:','E','E:','I','U','I:','U:',
	'O','O:','ai','Ei','ui','au','aE','OE'] # done with ASCII



old_sindarin = ['p','b','m','f','v','0D','6D',
	't','d','n','s','r','hlF','l','j',
	'k','g','N','x','w','h','hw','i','i:',
	'y','y:','a','y:','u','u:','E','E:','I','U','I:','U:',
	'O','O:','ai','Ei','ui','au','aE','OE','E)'] # done with ASCII


syldavian = ['i','I','e','aa','E','a','y','o/','u','U','o','O','m','p','b',
	'f','v','n','t','d','s','z','r','"rF','l','k','g','x','h','j',
	'B','ts','dz','S','Z','tS','dZ','gF']
	# done with ASCII

talossan = ['a','a_','e','i','o','i_','u','U','b','c','C','d','6D','f',
			'g','h','k','l','m','n','p','q','r','s','B','t','v','x','z',
			'0D']# done with ASCII

teonaht = ['ai','ou','ea','eI','eIa','eua','eo','ia','io','io:','oi',
           'o:y','ao','a','i','I','e','E','"@','o','u',
           'p','b','t','d','k','g','f','v',
           '0D','6D','s','z','S','Z','tS',
           'dZ','m','n','x','hlF','?',
           'N','w','l','j','r','rA.','rAW.'] # done with ASCII and dipthongs

toki_pona = ["m","p","w","n","t","s","l",
             "k",'j','a','e','i','o','u'] #done with ASCII

tsolyani = ['p','b','f','v','m','w','0D',
	'6D','t','d','s','z','n','r',
	'r[','hlF','S','l','s.','j','k','g',
	'x','gF','N','q','?','h','i','e',
	'y','uu','a','o','u','ps','bz',
	'ts','dz','thlF','dZ','tS','ks',
        'gz','aI','oI','aU'] #done with ASCII

valyrian = ['a','a:','b','d','e','e:','g','gF','h','i','i:','dZ','Z','j',
			'k','x','X','l','lj','m','n','nj','o','o:','p','q','r','r[',
			'hr','s','t','0D','u','u:','v','w','y','y:','z', 'a:e','ae',
			'ao','a:o','ia','ia:','io','io:','ie','ie:','ua','ua:','uo',
			'uo:','ue','ue:'] #done with ASCII + Dipthongs

verdurian = ['a','a:','e','i','o','u','I','j','E)','y','p','b',
			'f','v','6D','s','z','tD','d','tS','s','z','S','Z','m',
			'n','l','r','k','g','q','R','tS','r['] #done with ASCII + Dipthongs

volapuk = ['a','a_','E','aa','b','tS','dZ','d','e','f','g','h','i','S',
			'Z','k','l','m','n','o','O','o/','p','r','s','z','t','u',
			'y','v','w','j','ts','dz','6D','0D','N'] # done with ASCII

vulcan =['a','u','o','E','a_','I','U','O','ES','a_)','i:','u:','o:',
		'E:','a_:','oi','ei','ai','au','m','p','t','s','ts','k','j',
		'n','b','d','z','tS','g','w','N','f','l','0D','X','v','r[',
		'S','dZ','h'] #done with ASCII

wenedyk = ['i', 'E','a','u','O','i_','E{~}','O{~}','m','p','b',
			'f','v','nD','tD','dD','tsD','dzD','sD','zD','lD',
			'l','n','t','d','r','l','t.0','d.z','nj','tC,','dz',
			's,','z,','C,','z.','j','kj','gJ','xJ','gFJ','gF',
			'N','k','g','x','w']#same as Polish - Done with ASCII

# need to also look through the star wars languages

dictionaries = [atlantean,aui,barsoomian,brithenig,
                dothraki,dni,
                draconic,eskayan,esperanto,furbish,
                golic_volcan,interlingua,ithkuil_revised,klingon,
                laadan,loglan,lojban, navi,quenya,sindarin,
                old_sindarin,syldavian,talossan,teonaht,
                toki_pona,tsolyani,valyrian,verdurian,volapuk,
                vulcan,wenedyk]

languages = ['atlantean','aui','barsoomian', 'brithenig',
             'dothraki',"d'ni",
             'draconic','eskayan','esperanto', 'furbish',
             'golic volcan','interlingua', 'ithkuil','klingon','laadan',
             'loglan', 'lojban',"na'vi",  'quenya', 'sindarin',
             'old sindarin','syldavian','talossan','teonaht',
             'toki pona','tsolyani','valyrian','verdurian',
             'volapuk','vulcan','wenedyk']

classes = {'artistic':['atlantean','barsoomian','dothraki',
                       "d'ni",'draconic','furbish','golic volcan',
                       'klingon','old sindarin',"na'vi",'quenya',
                       'sindarin','syldavian','talossan','teonaht',
                       'tsolyani','valyrian','verdurian',
                       'vulcan'],
           'engineered':['brithenig','ithkuil','laadan','loglan','lojban',
                         'toki pona','wenedyk'],
           'auxiliary language':['aui','eskayan','esperanto','interlingua',
                        'volapuk']}

upper_languages = [i.upper() for i in languages]

all_segments = list(set(
    [item for sublist in dictionaries for item in sublist]))

frequencies = {}
num_langs = len(dictionaries)
for segment in all_segments:
    count = 0
    for dictionary in dictionaries:
        if segment in dictionary:
            count +=1
    frequencies[segment]=count/num_langs

# the frequency index of a lang is the sum of all frequencies of its
# segments divided by the number of segments
frequency_index ={}
for i in range(0,num_langs): # for each language
    the_sum = 0
    for segment in dictionaries[i]:
        the_sum += frequencies[segment]
    frequency_index[languages[i]]=the_sum/len(dictionaries[i])

least_to_greatest = sorted(frequency_index.values())

sorted_languages = []
for percent in least_to_greatest:
    sorted_languages.append(list(frequency_index.keys())[list(
        frequency_index.values()).index(percent)])

average_freq = sum(frequency for frequency in list(
    frequency_index.values()))/len(frequency_index.values())
    
