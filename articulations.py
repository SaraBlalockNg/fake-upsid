from inventories import *

#classification of phonemes as obstruent or sonorant
#phonemes taken from UPSID

vowel =             ['"@','"@)','"@)S','"@.','"@:','"@S','"@~','"e','"e*','"e9','"e:','"eS','"e_','"e~','"e~*','"he','"ho','"o','"o(','"o(+~','"o(:','"o(~','"o*',
                    '"o+','"o/','"o/9','"o/:','"o9','"o9:','"o9~','"o:','"oS','"o~','"o~*','3','3)','0.125','3~','4','4)S','4)_','49','4S','4_','@','@)','@)~','@:',
                    '@~','@~:','E','E)','E)~','E*','E:','ES','Eh','E~','E~:','I','I9','IS','I_','I_~','I~','O','O*','O9','O9~:','O:','OS','Oh','O~',
                    'O~:','U','U+','U9','U:','US','UU','UUS','U~','Y','^','^h','^~','a','a*','a+','a+:','a+~','a.','a9','a9:','a9~','a9~:','a:','aS',
                    'a_','a_)','a_):','a_)S','a_)h','a_)~','a_:','a_~','a_~:','aa','aa9','aa:','aa~','ah','a~','a~*','a~:','e','e*','e:','e_','eh','e~','e~:','ha',
                    'hi','hu','i','i*','i-','i9','i9:','i:','iF','iS','i_','i_.','i_:','i_S','i_~','i_~:','ih','i~','i~*','i~-','i~:','o','o(','o(+','o(h',
                    'o*','o+','o/','o/:','o/S','o/_','o:','oS','oh','o~','o~:','u','u*','u+','u+:','u+S','u9','u9:','u:','uF','uS','uh','uu','uu:','uuF',
                    'uuh','uu~','u~','u~:','y','y:','y~']

dipthong =          ['3i','@i','@u','@uu','EO~','Ei','Eo','Euu','Ie','Oi','Oih','Oi~','Oy','Ui','a+i','a+i~','aE','a_O~','aai','aau+','ae','ae9','ae9~','ai',
                    'ai_','aih','ai~','ao','ao9','ao9~','au','auh','auu','auuh','e@','ea','ei','ei~','eo','eu','eu~','i@','i@h','iE','iEh','i^','i_@','i_a','i_i',
                    'i_i~','ia','ia+','iah','ie','ie~','io','iu','iuh','o(i','o(ih','o/y','oa','oa9','oa9~','oa~','oe','oi','oi9','oi9~','oih','oi~','ou','ou~','u@',
                    'u@h','u^','ua','uah','ui','uih','ui~','uo','uu@','uu@h','uu^','uua','uui','uuih','yo/']

approximant =       ['"hl','"hrA','"l','"l*','"l-','"l9','"lJ','"lh','"rA','BA','BA-','BA:','BAJ','L','PA','RA','RAW','RAW*','dlD','gA','gA*','hj','hl','hl-',
                    'hl.','hlD','hlJ','hw','j','j*','j_','j~','l','l*','l-','l.','l9','lD','lD-','lD:','lDJ','lJ','l_','l_h','lj','l~','r.A','rA','vA',
                    'w','w*','wj','w~']

nasal =             ['"hn','"n','"n*','"n:','"nJ','"nW','"nh','N','N*','N9','NJ','NW','Nh','Nm','hN','hNJ','hNW','hNm','hm','hn','hn-','hn.','hnD','hnJ',
                    'hn_','hnj','m','m*','m:','mD','mJ','mW','mW-','mh','n','n*','n-','n.','n:','nD','nD*','nDJ','nDh','nJ','nU','n_','n_h','nj','nj*',
                    'nj:','njW']

tapflap =          ['"l[','"r[','"r[J','hr[-','hr[J','l.[','l.[*','l[','l[J','r.[','r.[~','rDT','rDT*','rD[','rT','r[','r[*','r[-','r[F','r[J','r_[','v[']

trill =             ['"hr','"r','"r*','"r-','"r9','"rF','"rJ','R','d.r','hr','nr','r','r.','rD','rDJ','rJ','rj','t.r']


ejectivestop =      ['"t\'','b\'','c\'','d\'',"g'","k'","kJ'","kW'",'p\'','q\'','q9\'','qW\'','qW9\'','t\'','tD\'']

ejectivefricative = ['"s\'',"C,'","P'","S'","X'","XW'","f'","hlDFJ'","s'","s.'","sD'","x'","xW'"]

ejectiveaffricate = ['"tlF\'',"\"tlF':","\"tlFW'","\"ts'","\"ts':","\"tsW'","cC,\'","dZ'","dz'","klF'","kx':","pf'","qX'","qX':","qX9'","qX9':","qXW'",
                    "qXW9'","t.s'","tD0'","tDs'","tS'","tS':","tSW'","tlF'","ts'"]

implosive =         ["\"d<","b<","bJ<","d.<","d<","dD<","d_<","dj<","g<","p<","q<","t<",]
plosive =           ['"d','"d*','"d9','"dJ','"dW','"dh','"nd','"ndJ','"ndW','"nt','"t','"t*','"t-h','"t9','"t:','"tJ','"tJh','"tW','"tWh','"th','"thh','99','?','?9',
                    '??','?W','G','G9','GW','GW9','Ng','NgW','Nk','NkJ','NkW','Nkh','Nmgb','Nq','Nqh','b','b*','b:','bD','bJ','bJh','bW','bW-','bh','bm',
                    'c','c:','ch','d','d*','d-','d.','d.*','d.h','d.n','dD','dD*','dD9','dDJ','dDh','dDn','dJ','d_','d_*','d_n','dj','dj*','dj:','dn','g',
                    'gJ','gL','gW','gWh','gb','gbW','gh','gn','hk','hp','ht','k','k*','k9','k:','kJ','kJh','kW','kW*','kW:','kWh','kh','khh','klF','kp',
                    'kpW','kph','mb','mbJ','mbW','mp','mph','nc','nd','nd.','ndD','ndJ','nd_','ndj','nt','nt.','ntD','ntDh','nt_','p','p*','p:','pJ','pJh','pW',
                    'pW-h','ph','phh','q','q*','q9h','q:','qW','qW*','qW9h','qW:','qWh','qh','t','t-','t.','t.*','t.h','t:','tD','tD*','tD9','tDJ','tDh','tDhh',
                    'tJ','t_','t_h','th','thh']


affricate =         ['"dlF','"dz','"dzJ','"dzh','"nts','"tlF','"tlF*','"tlF:','"tlFWh','"tlFh','"ts','"ts*','"ts:','"tsJ','"tsW:','"tsWh','"tsh','"tshh','bv','cC','cC,','cC,h','cCW','cCh',
                    'd.z','dD6','dDz','dZ','dZ-','dZJ','dZW','dZh','djjF','djjFW','djz,','dlF','dz','dz-','dzh','htS','kx','kx:','kxWh','kxh','ncC,','nd.z','ndDz','ndZ','ndjjF',
                    'ndjz,','ndz','nt.s','nt.sh','ntDs','ntDsh','ntS','ntSh','pf','pfh','qX','qX9','qX:','qXW','qXW9','t.0','t.s','t.sh','t0','t0h','tD0','tD0h','tDs','tDsJ','tDsh',
                    'tS','tS*','tS-','tS:','tSJ','tSJh','tSW','tSW:','tSWh','tSh','tlF','tlFh','ts','ts*','ts-','tsh','tshh']

fricative =         ['"6','"hlF','"hlF:','"hlFJ','"hlFW','"hlFW:','"hs','"lF','"ns','"nz','"rF','"s','"s9','"s:','"sJ','"sW','"sW:','"sh','"z','"z9','"zJ','"zW','0','0D',
                    '0_','6','6','6D','6DJ','6_','9','B','BJ','C','C,','CW','H','P','PJ','PW','PW-','RF','RF9','RFW','RFW9','S','S-','S:','SJ',
                    'SW','SW:','X','X9','X9:','X:','XW','XW9','XW9:','XW:','Z','Z-','ZJ','ZW','Zh','f','f:','fJ','fW','gF','gF*','gFJ','gFW','h','h*',
                    'hJ','hLF','hS','hW','hh','hlDF','hlDF:','hlDFJ','hlF','hlFJ','hxlF','jF','klF','l.F','lDF','lDFJ','lF','lFJ','mv','nZ','nz','nzD','r[F','s','s*',
                    's.','s9','s:','sD','sD*','sD9','sDJ','sJ','v','vJ','vW','vh','x','x:','xJ','xW','xW:','z','z,','z.','z.*','zD','zD9','zDJ']

sonorant = vowel + dipthong + nasal + approximant + trill + tapflap
obstruent = ejectivestop + ejectiveaffricate + ejectivefricative + implosive + plosive + affricate + fricative
all_features = sonorant + obstruent

features={}
features['-any length-'] = sonorant + obstruent
features['-any modifier-'] = sonorant + obstruent
features['-any voicing-'] = sonorant + obstruent
features['-any height-'] = sonorant + obstruent
features['-any backness-'] = sonorant + obstruent
features['-any rounding-'] = sonorant + obstruent
features['-any vowel-'] = vowel + dipthong
features['-any aspiration, etc.-'] = sonorant + obstruent
features['-any sec. articulation-'] = sonorant + obstruent
features['-any place-'] = sonorant + obstruent
features['-any manner-'] = sonorant + obstruent
features['-any release-'] = sonorant + obstruent

#

features['overshort'] = ['"@)S','"@S','"eS','"oS','4)S','4S','ES','IS','OS','US',
                        'UUS','aS','a_)S','iS','i_S','o/S','oS','u+S','uS']
features['short'] =     ['"@','"@)','"@.','"@~','"e','"e*','"e9','"e_','"e~','"e~*','"he','"ho','"o','"o(','"o(+~','"o(~','"o*','"o+','"o/','"o/9','"o9','"o9~',
                        '"o~','"o~*','3','3)','3i','3~','4','4)_','49','4_','@','@)','@)~','@i','@u','@uu','@~','E','E)','E)~','E*','EO~','Eh','Ei','Eo',
                        'Euu','E~','I','I9','I_','I_~','Ie','I~','O','O*','O9','Oh','Oi','Oih','Oi~','Oy','O~','U','U+','U9','UU','Ui','U~','Y','^',
                        '^h','^~','a','a*','a+','a+i','a+i~','a+~','a.','a9','a9~','aE','a_','a_)','a_)h','a_)~','a_O~','a_~','aa','aa9','aai','aau+','aa~','ae','ae9',
                        'ae9~','ah','ai','ai_','aih','ai~','ao','ao9','ao9~','au','auh','auu','auuh','a~','a~*','e','e*','e@','e_','ea','eh','ei','ei~','eo','eu',
                        'eu~','e~','ha','hi','hu','i','i*','i-','i9','i@','i@h','iE','iEh','iF','i^','i_','i_.','i_@','i_a','i_i','i_i~','i_~','ia','ia+','iah',
                        'ie','ie~','ih','io','iu','iuh','i~','i~*','i~-','o','o(','o(+','o(h','o(i','o(ih','o*','o+','o/','o/_','o/y','oa','oa9','oa9~','oa~','oe',
                        'oh','oi','oi9','oi9~','oih','oi~','ou','ou~','o~','u','u*','u+','u9','u@','u@h','uF','u^','ua','uah','uh','ui','uih','ui~','uo','uu',
                        'uu@','uu@h','uuF','uu^','uua','uuh','uui','uuih','uu~','u~','y','yo/','y~',
#vowels above consonants below
                        '!','!?','!h','!xh','"6','"d','"d*','"d9','"d<','"dJ','"dW','"dh','"dlF','"dz','"dzJ','"dzh','"hl','"hlF','"hlF\'','"hlFJ','"hlFW','"hn','"hr','"hrA',
                        '"hrr','"hs','"l','"l*','"l-','"l9','"lF','"lJ','"l[','"lh','"n','"n*','"nJ','"nW','"nd','"ndJ','"ndW','"nh','"ns','"nt','"nts','"nz','"r','"r*','"r-',
                        '"r9','"rA','"rF','"rJ','"r[','"r[J','"rr','"rr*','"s','"s\'','"s9','"sJ','"sW','"sh','"t','"t\'','"t*','"t-h','"t9','"tJ','"tJh','"tW','"tWh','"th',
                        '"thh','"tlF','"tlF\'','"tlF*','"tlFW\'','"tlFWh','"tlFh','"ts','"ts\'','"ts*','"tsJ','"tsW\'','"tsWh','"tsh','"tshh','"z','"z9','"zJ','"zW','#','#?','#h','#j','#jh','#jx',
                        '#xh','/','/=','/=h','/=x','/h','/s','/x','/xh','0','0D','0_','6','6','6D','6DJ','6_','9','99','?','?9','??','?W','B','BA','BA-',
                        'BAJ','BJ','C','C,','C,\'','CW','G','G9','GW','GW9','H','L','N','N*','N9','NJ','NW','Ng','NgW','Nh','Nk','NkJ','NkW','Nkh','Nm',
                        'Nmgb','Nq','Nqh','P','P\'','PA','PJ','PW','PW-','R','RA','RAW','RAW*','RF','RF9','RFW','RFW9','S','S\'','S-','SJ','SW','X','X\'',
                        'X9','XW','XW\'','XW9','Z','Z-','ZJ','ZW','Zh','b','b\'','b*','b<','bD','bJ','bJ<','bJh','bW','bW-','bh','bm','bv','c','c\'',
                        'cC','cC,','cC,\'','cC,h','cCW','cCh','ch','d','d\'','d*','d-','d.','d.*','d.<','d.h','d.n','d.r','d.z','d<','dD','dD*','dD6','dD9','dD<',
                        'dDJ','dDh','dDn','dDz','dJ','dZ','dZ\'','dZ-','dZJ','dZW','dZh','d_','d_*','d_<','d_n','dj','dj*','dj<','djjF','djjFW','djz,','dlD','dlF','dn','dz',
                        'dz\'','dz-','dzh','f','f\'','fJ','fW','g','g!','g#','g#j','g#jh','g#jx','g#jx?','g\'','g/','g/=','g/=h','g/=x','g/=x?','g/h','g/x','g/x?','g<',
                        'gA','gA*','gF','gF*','gFJ','gFW','gJ','gL','gW','gWh','gb','gbW','gh','gn','g|','g|h','g|x','g|x?','h','h*','hJ','hLF','hN','hNJ','hNW',
                        'hNm','hS','hW','hh','hj','hk','hl','hl-','hl.','hlD','hlDF','hlDFJ','hlDFJ\'','hlF','hlFJ','hlJ','hm','hn','hn!?','hn!h','hn#?','hn#h','hn#j?','hn#jh',
                        'hn#jx?','hn-','hn.','hn/=?','hn/=h','hn/=x?','hn/?','hn/h','hn/x?','hnD','hnJ','hn_','hnj','hn|?','hn|h','hn|x?','hp','hr','hr[-','hr[J','ht','htS','hw','hxlF','j',
                        'j*','jF','j_','j~','k','k\'','k*','k9','kJ','kJ\'','kJh','kW','kW\'','kW*','kWh','kh','khh','klF','klF\'','kp','kpW','kph','kx','kxWh',
                        'kxh','l','l*','l-','l.','l.F','l.[','l.[*','l9','lD','lD-','lDF','lDFJ','lDJ','lF','lFJ','lJ','l[','l[J','l_','l_h','lj','l~','m','m*',
                        'mD','mJ','mW','mW-','mb','mbJ','mbW','mh','mp','mph','mv','n','n!','n#','n#j','n#jh','n*','n-','n.','n/','n/=','n/=h','n/h','nD','nD*',
                        'nDJ','nDh','nJ','nU','nZ','n_','n_h','nc','ncC,','nd','nd.','nd.z','ndD','ndDz','ndJ','ndZ','nd_','ndj','ndjjF','ndjz,','ndz','nj','nj*','njW','nr',
                        'nt','nt.','nt.s','nt.sh','ntD','ntDh','ntDs','ntDsh','ntS','ntSh','nt_','nz','nzD','n|','n|h','p','p\'','p*','p<','pJ','pJh','pW','pW-h','pf',
                        'pf\'','pfh','ph','phh','q','q\'','q*','q9\'','q9h','q<','qW','qW\'','qW*','qW9\'','qW9h','qWh','qX','qX\'','qX9','qX9\'','qXW','qXW\'','qXW9',
                        'qXW9\'','qh','r','r.','r.A','r.[','r.[~','rA','rD','rDJ','rDT','rDT*','rD[','rJ','rT','r[','r[*','r[-','r[F','r[J','r_[','rj','rr','rrD',
                        'rrJ','s','s\'','s*','s.','s.\'','s9','sD','sD\'','sD*','sD9','sDJ','sJ','t','t\'','t-','t.','t.*','t.0','t.h','t.r','t.s','t.s\'',
                        't.sh','t0','t0h','t<','tD','tD\'','tD*','tD0','tD0\'','tD0h','tD9','tDJ','tDh','tDhh','tDs','tDs\'','tDsJ','tDsh','tJ','tS','tS\'','tS*','tS-','tSJ',
                        'tSJh','tSW','tSW\'','tSWh','tSh','t_','t_h','th','thh','tlF','tlF\'','tlFh','ts','ts\'','ts*','ts-','tsh','tshh','v','vA','vJ','vW','v[','vh',
                        'w','w*','wj','w~','x','x\'','xJ','xW','xW\'','z','z,','z.','z.*','zD','zD9','zDJ','|','|?','|h','|x','|xh'] # for both v & c

features['long'] = ['"@:','"e:','"o(:','"o/:','"o9:','"o:','3:','@:','@~:','E:','E~:','O9~:','O:','O~:','U:','a+:','a9:','a9~:','a:','a_):','a_:','a_~:',
                    'aa:','a~:','e:','e~:','i9:','i:','i_:','i_~:','i~:','o/:','o:','o~:','u+:','u9:','u:','uu:','u~:','y:',

                    '"hlF:','"hlFW:','"n:','"s:','"sW:','"t:','"tlF\':','"tlF:','"ts\':','"ts:','"tsW:','BA:','S:','SW:','X9:','X:','XW9:','XW:','b:','c:','dj:','f:','hlDF:','k:',
                    'kW:','kx\':','kx:','lD:','m:','n:','nj:','p:','q:','qW:','qX\':','qX9\':','qX:','s:','t:','tS\':','tS:','tSW:','x:','xW:',] # for both v & c

features['no modifier'] = ['"@','"@)','"@)S','"@:','"@S','"e','"e:','"eS','"e_','"he','"ho','"o','"o(','"o(:',
                            '"o+','"o/','"o/:','"o:','"oS','3','3)','3:','3i','4','4)S','4)_','4S','4_','@','@)','@:','@i','@u','@uu','E','E)','E:','ES','Eh',
                            'Ei','Eo','Euu','I','IS','I_','Ie','O','O:','OS','Oh','Oi','Oih','Oy','U','U+','U:','US','UU','UUS','Ui','Y','^','^h','a',
                            'a+','a+:','a+i','a:','aE','aS','a_','a_)','a_):','a_)S','a_)h','a_:','aa','aa:','aai','aau+','ae','ah','ai','ai_','aih','ao','au','auh','auu',
                            'auuh','e','e:','e@','e_','ea','eh','ei','eo','eu','ha','hi','hu','i','i-','i:','i@','i@h','iE','iEh','iS','i^','i_','i_:','i_@',
                            'i_S','i_a','i_i','ia','ia+','iah','ie','ih','io','iu','iuh','o','o(','o(+','o(h','o(i','o(ih','o+','o/','o/:','o/S','o/_','o/y','o:','oS',
                            'oa','oe','oh','oi','oih','ou','u','u+','u+:','u+S','u:','u@','u@h','uS','u^','ua','uah','uh','ui','uih','uo','uu','uu:','uu@','uu@h',
                            'uu^','uua','uuh','uui','uuih','y','y:','yo/',

                            '!','!?','!h','!xh','"6','"d','"d*','"d9','"d<','"dJ','"dW','"dh','"hn','"hr','"hrA','"hrr','"n','"n*','"n:','"nJ','"nW','"nd','"ndJ','"ndW','"nh',
                            '"nt','"r','"r*','"r-','"r9','"rA','"rF','"rJ','"r[','"r[J','"rr','"rr*','"t','"t\'','"t*','"t-h','"t9','"t:','"tJ','"tJh','"tW','"tWh','"th','"thh',
                            '/','/=','/=h','/=x','/h','/s','/x','/xh','0','0D','0_','6','6','6D','6DJ','6_','9','99','?','?9','??','?W','B','BA','BA-',
                            'BA:','BAJ','BJ','C','CW','G','G9','GW','GW9','H','N','N*','N9','NJ','NW','Ng','NgW','Nh','Nk','NkJ','NkW','Nkh','Nm','Nmgb','Nq',
                            'Nqh','P','P\'','PA','PJ','PW','PW-','R','RA','RAW','RAW*','RF','RF9','RFW','RFW9','X','X\'','X9','X9:','X:','XW','XW\'','XW9','XW9:',
                            'XW:','b','b\'','b*','b:','b<','bD','bJ','bJ<','bJh','bW','bW-','bh','bm','bv','c','c\'','c:','cC','cCW','cCh','ch','d','d\'',
                            'd*','d-','d.','d.*','d.<','d.h','d.n','d.r','d<','dD','dD*','dD6','dD9','dD<','dDJ','dDh','dDn','dJ','d_','d_*','d_<','d_n','dj','dj*','dj:',
                            'dj<','djjF','djjFW','dn','f','f\'','f:','fJ','fW','g','g!','g\'','g/','g/=','g/=h','g/=x','g/=x?','g/h','g/x','g/x?','g<','gA','gA*','gF',
                            'gF*','gFJ','gFW','gJ','gL','gW','gWh','gb','gbW','gh','gn','g|','g|h','g|x','g|x?','h','h*','hJ','hN','hNJ','hNW','hNm','hW','hh','hj','hk',
                            'hm','hn','hn!?','hn!h','hn-','hn.','hn/=?','hn/=h','hn/=x?','hn/?','hn/h','hn/x?','hnD','hnJ','hn_','hnj','hn|?','hn|h','hn|x?','hp','hr','hr[-','hr[J','ht','hw','j',
                            'j*','jF','j_','j~','k','k\'','k*','k9','k:','kJ','kJ\'','kJh','kW','kW\'','kW*','kW:','kWh','kh','khh','kp','kpW','kph','kx','kx\':',
                            'kx:','kxWh','kxh','m','m*','m:','mD','mJ','mW','mW-','mb','mbJ','mbW','mh','mp','mph','mv','n','n!','n*','n-','n.','n/','n/=','n/=h',
                            'n/h','n:','nD','nD*','nDJ','nDh','nJ','nU','n_','n_h','nc','nd','nd.','ndD','ndJ','nd_','ndj','ndjjF','nj','nj*','nj:','njW','nr','nt','nt.',
                            'ntD','ntDh','nt_','n|','n|h','p','p\'','p*','p:','p<','pJ','pJh','pW','pW-h','pf','pf\'','pfh','ph','phh','q','q\'','q*','q9\'','q9h',
                            'q:','q<','qW','qW\'','qW*','qW9\'','qW9h','qW:','qWh','qX','qX\'','qX\':','qX9','qX9\'','qX9\':','qX:','qXW','qXW\'','qXW9','qXW9\'','qh','r',
                            'r.','r.A','r.[','r.[~','rA','rD','rDJ','rDT','rDT*','rD[','rJ','rT','r[','r[*','r[-','r[F','r[J','r_[','rj','rr','rrD','rrJ','t','t\'','t-',
                            't.','t.*','t.0','t.h','t.r','t0','t0h','t:','t<','tD','tD\'','tD*','tD0','tD0\'','tD0h','tD9','tDJ','tDh','tDhh','tJ','t_','t_h','th','thh',
                            'v','vA','vJ','vW','v[','vh','w','w*','wj','w~','x','x\'','x:','xJ','xW','xW\'','xW:','|','|?','|h','|x','|xh'] # for both v & c

features['fricative'] =     ['iF','uF','uuF']
features['retroflexed'] =   ['"@.','a.','i .']
features['pharyngealized'] =    ['"e9','"o/9','"o9','"o9:','"o9~','49','I9','O9','O9~:','U9','a9','a9:','a9~','a9~:','aa9','ae9','ae9~','ao9','ao9~','i9','i9:','oa9',
                                'oa9~','oi9','oi9~','u9','u9:','"d9','"l9','"r9','"s9','"t9','"z9','?9','G9','GW9','N9','RF9','RFW9','X9','X9:','XW9','XW9:','dD9','k9','l9',
                                'q9\'','q9h','qW9\'','qW9h','qX9','qX9\'','qX9\':','qXW9','qXW9\'','s9','sD9','tD9','zD9'] # for both v & c

features['laryngealized'] =     ['"d*','"l*','"n*','"r*','"rr*','"t*','"tlF*','"ts*','N*','RAW*','b*','d*','d.*','dD*','d_*','dj*','gA*','gF*','h*','j*','k*','kW*',
                                'l*','l.[*','m*','n*','nD*','nj*','p*','q*','qW*','rDT*','s*','sD*','t.*','tD*','tS*','ts*','w*','z.*','"e*','"e~*','"o*','"o~*','E*','O*','a*',
                                'a~*','e*','i*','i~*','o*','u*',] # for both v & c

features['nasalized'] =         ['"@~','"e~','"e~*','"o(+~','"o(~','"o9~','"o~','"o~*','3~','@)~','@~','@~:','E)~','EO~','E~','E~:','I_~','I~','O9~:','Oi~','O~','O~:',
                                'U~','^~','a+i~','a+~','a9~','a9~:','a_)~','a_O~','a_~','a_~:','aa~','ae9~','ai~','ao9~','a~','a~*','a~:','ei~','eu~','e~','e~:','i_i~',
                                'i_~','i_~:','ie~','i~','i~*','i~-','i~:','oa9~','oa~','oi9~','oi~','ou~','o~','o~:','ui~','uu~','u~','u~:','y~',]

features['breathy voicing'] =   ['Eh','Oh','Oih','^h','a_)h','ah','aih','auh','auuh','eh','i@h','iEh','iah','ih','iuh','o(h','o(ih','oh','oih','u@h','uah','uh',
                                'uih','uu@h','uuh','uuih',]
features["'normal' voicing"] =  ['"@','"@)','"@)S','"@.','"@:','"@S','"@~','"e','"e*','"e9','"e:','"eS','"e_','"e~','"e~*','"o','"o(','"o(+~','"o(:','"o(~','"o*','"o+',
                                '"o/','"o/9','"o/:','"o9','"o9:','"o9~','"o:','"oS','"o~','"o~*','3','3)','3:','3i','3~','4','4)S','4)_','49','4S','4_','@','@)','@)~','@:',
                                '@i','@u','@uu','@~','@~:','E','E)','E)~','E*','E:','EO~','ES','Ei','Eo','Euu','E~','E~:','I','I9','IS','I_','I_~','Ie','I~','O',
                                'O*','O9','O9~:','O:','OS','Oi','Oi~','Oy','O~','O~:','U','U+','U9','U:','US','UU','UUS','Ui','U~','Y','^','^~','a','a*','a+',
                                'a+:','a+i','a+i~','a+~','a.','a9','a9:','a9~','a9~:','a:','aE','aS','a_','a_)','a_):','a_)S','a_)~','a_:','a_O~','a_~','a_~:','aa','aa9','aa:','aai',
                                'aau+','aa~','ae','ae9','ae9~','ai','ai_','ai~','ao','ao9','ao9~','au','auu','a~','a~*','a~:','e','e*','e:','e@','e_','ea','ei','ei~','eo',
                                'eu','eu~','e~','e~:','i','i*','i-','i9','i9:','i:','i@','iE','iF','iS','i^','i_','i_.','i_:','i_@','i_S','i_a','i_i','i_i~','i_~','i_~:',
                                'ia','ia+','ie','ie~','io','iu','i~','i~*','i~-','i~:','o','o(','o(+','o(i','o*','o+','o/','o/:','o/S','o/_','o/y','o:','oS','oa','oa9',
                                'oa9~','oa~','oe','oi','oi9','oi9~','oi~','ou','ou~','o~','o~:','u','u*','u+','u+:','u+S','u9','u9:','u:','u@','uF','uS','u^','ua','ui',
                                'ui~','uo','uu','uu:','uu@','uuF','uu^','uua','uui','uu~','u~','u~:','y','y:','yo/','y~',]
features['voiceless'] =         ['"he','"ho','ha','hi','hu','!','!?','!h','!xh','"hl','"hlF','"hlF\'','"hlF:','"hlFJ','"hlFW','"hlFW:','"hn','"hr','"hrA','"hrr','"hs','"ns',
                                '"nt','"nts','"s','"s\'','"s9','"s:','"sJ','"sW','"sW:','"sh','"t','"t\'','"t*','"t-h','"t9','"t:','"tJ','"tJh','"tW','"tWh','"th','"thh','"tlF',
                                '"tlF\'','"tlF\':','"tlF*','"tlF:','"tlFW\'','"tlFWh','"tlFh','"ts','"ts\'','"ts\':','"ts*','"ts:','"tsJ','"tsW\'','"tsW:','"tsWh','"tsh','"tshh',
                                '#','#?','#h','#j','#jh','#jx','#xh','/','/=','/=h','/=x','/h','/s','/x','/xh','0','0D','0_','6_','?','?9','?W','C','C,',
                                'C,\'','CW','H','Nk','NkJ','NkW','Nkh','Nq','Nqh','P','P\'','PA','PJ','PW','PW-','S','S\'','S-','S:','SJ','SW','SW:','X',
                                'X\'','X9','X9:','X:','XW','XW\'','XW9','XW9:','XW:','c','c\'','c:','cC','cC,','cC,\'','cC,h','cCW','cCh','ch','f','f\'','f:','fJ',
                                'fW','h','h*','hJ','hLF','hN','hNJ','hNW','hNm','hS','hW','hj','hk','hl','hl-','hl.','hlD','hlDF','hlDF:','hlDFJ','hlDFJ\'','hlF','hlFJ','hlJ',
                                'hm','hn','hn!?','hn!h','hn#?','hn#h','hn#j?','hn#jh','hn#jx?','hn-','hn.','hn/=?','hn/=h','hn/=x?','hn/?','hn/h','hn/x?','hnD','hnJ','hn_','hnj',
                                'hn|?','hn|h','hn|x?','hp','hr','hr[-','hr[J','ht','htS','hw','hxlF','k','k\'','k*','k9','k:','kJ','kJ\'','kJh','kW','kW\'','kW*','kW:','kWh',
                                'kh','khh','klF','klF\'','kp','kpW','kph','kx','kx\':','kx:','kxWh','kxh','mp','mph','nc','ncC,','nt','nt.','nt.s','nt.sh','ntD','ntDh','ntDs','ntDsh',
                                'ntS','ntSh','nt_','p','p\'','p*','p:','p<','pJ','pJh','pW','pW-h','pf','pf\'','pfh','ph','phh','q','q\'','q*','q9\'','q9h','q:','q<',
                                'qW','qW\'','qW*','qW9\'','qW9h','qW:','qWh','qX','qX\'','qX\':','qX9','qX9\'','qX9\':','qX:','qXW','qXW\'','qXW9','qXW9\'','qh','s','s\'','s*',
                                's.','s.\'','s9','s:','sD','sD\'','sD*','sD9','sDJ','sJ','t','t\'','t-','t.','t.*','t.0','t.h','t.r','t.s','t.s\'','t.sh','t0','t0h',
                                't:','t<','tD','tD\'','tD*','tD0','tD0\'','tD0h','tD9','tDJ','tDh','tDhh','tDs','tDs\'','tDsJ','tDsh','tJ','tS','tS\'','tS\':','tS*','tS-',
                                'tS:','tSJ','tSJh','tSW','tSW\'','tSW:','tSWh','tSh','t_','t_h','th','thh','tlF','tlF\'','tlFh','ts','ts\'','ts*','ts-','tsh','tshh','x','x\'','x:',
                                'xJ','xW','xW\'','xW:','|','|?','|h','|x','|xh',] # both v & c

features['high'] =              ['3i','@i','@u','@uu','Ei','Euu','Oi','Oih','Oi~','Oy','a+i','a+i~','aai','aau+','ai','ai_','aih','ai~','au','auh','auu','auuh',
                                'ei','ei~','eu','eu~','hi','hu','i','i*','i-','i9','i9:','i:','i@','i@h','iE','iEh','iF','iS','i^','i_','i_.','i_:','i_@','i_S','i_a',
                                'i_i','i_i~','i_~','i_~:','ia','ia+','iah','ie','ie~','ih','io','iu','iuh','i~','i~*','i~-','i~:','o(i','o(ih','o/y','oi','oi9','oi9~','oih','oi~',
                                'ou','ou~','u','u*','u+','u+:','u+S','u9','u9:','u:','u@','u@h','uF','uS','u^','ua','uah','uh','ui','uih','ui~','uo','uu','uu:','uu@',
                                'uu@h','uuF','uu^','uua','uuh','uui','uuih','uu~','u~','u~:','y','y:','yo/','y~',]

features['lowered high'] =  ['I','I9','IS','I_','I_~','Ie','I~','U','U+','U9','U:','US','UU','UUS','Ui','U~','Y',]

features['higher mid'] =    ['@','@)','@)~','@:','@~','@~:','e','e*','e:','e_','eh','e~','e~:','o','o(','o(+','o(h','o(i','o(ih','o*','o+','o/',
                            'o/:','o/S','o/_','o/y','o:','oS','oh','oih','o~','o~:',]
features['mid'] =   ['"@','"@)','"@)S','"@.','"@:','"@S','"@~','"e','"e*','"e9','"e:','"eS','"e_','"e~','"e~*','"he','"ho','"o','"o(','"o(+~','"o(:','"o(~',
                    '"o*','"o+','"o/','"o/9','"o/:','"o9','"o9:','"o9~','"o:','"oS','"o~','"o~*','@i','@u','@uu','Ie','ae','ae9','ae9~','ao','ao9','ao9~','e@','ea','ei',
                    'ei~','eo','eu','eu~','i@','i@h','i_@','ie','ie~','io','oa','oa9','oa9~','oa~','oe','oi','oi9','oi9~','oi~','ou','ou~','u@','u@h','uo','uu@',
                    'uu@h','yo/',]
features['lower mid'] =     ['3','3)','3:','3i','3~','E','E)','E)~','E*','E:','EO~','ES','Eh','Ei','Eo','Euu','E~','E~:','O','O*','O9','O9~:',
                            'O:','OS','Oh','Oi','Oih','Oi~','Oy','O~','O~:','^','^h','^~','aE','a_O~','iE','iEh','i^','u^','uu^',]
features['raised low'] =    ['4','4)S','4)_','49','4S','4_','aa','aa9','aa:','aai','aau+','aa~',]
features['low'] =   ['a','a*','a+','a+:','a+i','a+i~','a+~','a.','a9','a9:','a9~','a9~:','a:','aE','aS','a_','a_)','a_):','a_)S','a_)h','a_)~','a_:',
                    'a_O~','a_~','a_~:','ae','ae9','ae9~','ah','ai','ai_','aih','ai~','ao','ao9','ao9~','au','auh','auu','auuh','a~','a~*','a~:','ea','ha',
                    'i_a','ia','ia+','iah','oa','oa9','oa9~','oa~','ua','uah','uua',]

features['front'] =     ['"e','"e*','"e9','"e:','"eS','"e~','"e~*','"he','"o/','"o/9','"o/:','3i','@i','E','E)','E)~','E*','E:','EO~','ES','Eh','Ei',
                        'Eo','Euu','E~','E~:','I','I9','IS','Ie','I~','Oi','Oih','Oi~','Oy','Ui','Y','a+','a+:','a+i','a+i~','a+~','aE','aa','aa9','aa:','aai',
                        'aau+','aa~','ae','ae9','ae9~','ai','aih','ai~','e','e*','e:','e@','ea','eh','ei','ei~','eo','eu','eu~','e~','e~:','hi','i','i*','i-',
                        'i9','i9:','i:','i@','i@h','iE','iEh','iF','iS','i^','i_i','i_i~','ia','ia+','iah','ie','ie~','ih','io','iu','iuh','i~','i~*','i~-','i~:',
                        'o(i','o(ih','o/','o/:','o/S','o/y','oe','oi','oi9','oi9~','oih','oi~','ui','uih','ui~','uui','uuih','y','y:','yo/','y~',]
features['retracted front'] =   ['"e_','e_','o/_',]
features['central'] =   ['"@','"@)','"@)S','"@.','"@:','"@S','"@~','3','3)','3:','3i','3~','4','4)S','49','4S','@','@)','@)~','@:','@i','@u',
                        '@uu','@~','@~:','I_','I_~','U+','a','a*','a.','a9','a9:','a9~','a9~:','a:','aE','aS','aau+','ae','ae9','ae9~','ah','ai','ai_','aih','ai~',
                        'ao','ao9','ao9~','au','auh','auu','auuh','a~','a~*','a~:','e@','ea','ha','i@','i@h','i_','i_.','i_:','i_@','i_S','i_a','i_i','i_i~','i_~','i_~:',
                        'ia','iah','oa','oa9','oa9~','oa~','u+','u+:','u+S','u@','u@h','ua','uah','uu@','uu@h','uua',]
features['fronted back'] =  ['"o(+~','"o+','o(+','o+',]
features['back'] =  ['"ho','"o','"o(','"o(:','"o(~','"o*','"o9','"o9:','"o9~','"o:','"oS','"o~','"o~*','4)_','4_','@u','@uu','EO~','Eo','Euu','O','O*',
                    'O9','O9~:','O:','OS','Oh','Oi','Oih','Oi~','Oy','O~','O~:','U','U9','U:','US','UU','UUS','Ui','U~','^','^h','^~','a_','a_)','a_):',
                    'a_)S','a_)h','a_)~','a_:','a_O~','a_~','a_~:','ao','ao9','ao9~','au','auh','auu','auuh','eo','eu','eu~','hu','i^','io','iu','iuh','o','o(','o(h',
                    'o(i','o(ih','o*','o:','oS','oa','oa9','oa9~','oa~','oe','oh','oi','oi9','oi9~','oih','oi~','ou','ou~','o~','o~:','u','u*','u9','u9:','u:',
                    'u@','u@h','uF','uS','u^','ua','uah','uh','ui','uih','ui~','uo','uu','uu:','uu@','uu@h','uuF','uu^','uua','uuh','uui','uuih','uu~','u~','u~:',]

features['unrounded'] =     ['"@','"@.','"@:','"@S','"@~','"e','"e*','"e9','"e:','"eS','"e_','"e~','"e~*','"he','"o(','"o(+~','"o(:','"o(~','3','3:','3i','3~',
                            '4','49','4S','4_','@','@:','@i','@u','@uu','@~','@~:','E','E*','E:','EO~','ES','Eh','Ei','Eo','Euu','E~','E~:','I','I9','IS',
                            'I_','I_~','Ie','I~','Oi','Oih','Oi~','UU','UUS','Ui','^','^h','^~','a','a*','a+','a+:','a+i','a+i~','a+~','a.','a9','a9:','a9~','a9~:',
                            'a:','aE','aS','a_','a_:','a_O~','a_~','a_~:','aa','aa9','aa:','aai','aau+','aa~','ae','ae9','ae9~','ah','ai','ai_','aih','ai~','ao','ao9','ao9~',
                            'au','auh','auu','auuh','a~','a~*','a~:','e','e*','e:','e@','e_','ea','eh','ei','ei~','eo','eu','eu~','e~','e~:','ha','hi','i','i*',
                            'i-','i9','i9:','i:','i@','i@h','iE','iEh','iF','iS','i^','i_','i_.','i_:','i_@','i_S','i_a','i_i','i_i~','i_~','i_~:','ia','ia+','iah',
                            'ie','ie~','ih','io','iu','iuh','i~','i~*','i~-','i~:','o(','o(+','o(h','o(i','o(ih','oa','oa9','oa9~','oa~','oe','oi','oi9','oi9~','oih','oi~',
                            'u@','u@h','u^','ua','uah','ui','uih','ui~','uu','uu:','uu@','uu@h','uuF','uu^','uua','uuh','uui','uuih','uu~',]
features['rounded'] =   ['"@)','"@)S','"ho','"o','"o*','"o+','"o/','"o/9','"o/:','"o9','"o9:','"o9~','"o:','"oS','"o~','"o~*','3)','4)S','4)_','@)','@)~',
                        '@u','E)','E)~','EO~','Eo','O','O*','O9','O9~:','O:','OS','Oh','Oi','Oih','Oi~','Oy','O~','O~:','U','U+','U9','U:','US','Ui','U~',
                        'Y','a_)','a_):','a_)S','a_)h','a_)~','a_O~','aau+','ao','ao9','ao9~','au','auh','eo','eu','eu~','hu','io','iu','iuh','o','o*','o+','o/','o/:',
                        'o/S','o/_','o/y','o:','oS','oa','oa9','oa9~','oa~','oe','oh','oi','oi9','oi9~','oih','oi~','ou','ou~','o~','o~:','u','u*','u+','u+:','u+S',
                        'u9','u9:','u:','u@','u@h','uF','uS','u^','ua','uah','uh','ui','uih','ui~','uo','u~','u~:','y','y:','yo/','y~',]
features['Monopthong'] =    ['"@','"@)','"@)S','"@.','"@:','"@S','"@~','"e','"e*','"e9','"e:','"eS','"e_','"e~','"e~*','"he','"ho','"o','"o(','"o(+~','"o(:','"o(~',
                            '"o*','"o+','"o/','"o/9','"o/:','"o9','"o9:','"o9~','"o:','"oS','"o~','"o~*','3','3)','3:','3~','4','4)S','4)_','49','4S','4_','@','@)','@)~',
                            '@:','@~','@~:','E','E)','E)~','E*','E:','ES','Eh','E~','E~:','I','I9','IS','I_','I_~','I~','O','O*','O9','O9~:','O:','OS','Oh',
                            'O~','O~:','U','U+','U9','U:','US','UU','UUS','U~','Y','^','^h','^~','a','a*','a+','a+:','a+~','a.','a9','a9:','a9~','a9~:','a:',
                            'aS','a_','a_)','a_):','a_)S','a_)h','a_)~','a_:','a_~','a_~:','aa','aa9','aa:','aa~','ah','a~','a~*','a~:','e','e*','e:','e_','eh','e~','e~:',
                            'ha','hi','hu','i','i*','i-','i9','i9:','i:','iF','iS','i_','i_.','i_:','i_S','i_~','i_~:','ih','i~','i~*','i~-','i~:','o','o(','o(+',
                            'o(h','o*','o+','o/','o/:','o/S','o/_','o:','oS','oh','o~','o~:','u','u*','u+','u+:','u+S','u9','u9:','u:','uF','uS','uh','uu','uu:',
                            'uuF','uuh','uu~','u~','u~:','y','y:','y~',]
features['Diphthong'] =     ['3i','@i','@u','@uu','EO~','Ei','Eo','Euu','Ie','Oi','Oih','Oi~','Oy','Ui','a+i','a+i~','aE','a_O~','aai','aau+','ae','ae9',
                            'ae9~','ai','ai_','aih','ai~','ao','ao9','ao9~','au','auh','auu','auuh','e@','ea','ei','ei~','eo','eu','eu~','i@','i@h','iE','iEh','i^','i_@',
                            'i_a','i_i','i_i~','ia','ia+','iah','ie','ie~','io','iu','iuh','o(i','o(ih','o/y','oa','oa9','oa9~','oa~','oe','oi','oi9','oi9~','oih',
                            'oi~','ou','ou~','u@','u@h','u^','ua','uah','ui','uih','ui~','uo','uu@','uu@h','uu^','uua','uui','uuih','yo/',]

features['voiced'] =    ['"6','"d','"d*','"d9','"d<','"dJ','"dW','"dh','"dlF','"dz','"dzJ','"dzh','"l','"l*','"l-','"l9','"lF','"lJ','"l[','"lh','"n','"n*',
                        '"n:','"nJ','"nW','"nd','"ndJ','"ndW','"nh','"nz','"r','"r*','"r-','"r9','"rA','"rF','"rJ','"r[','"r[J','"rr','"rr*','"z','"z9','"zJ','"zW','6','6',
                        '6D','6DJ','9','99','??','B','BA','BA-','BA:','BAJ','BJ','G','G9','GW','GW9','L','N','N*','N9','NJ','NW','Ng','NgW','Nh','Nm',
                        'Nmgb','R','RA','RAW','RAW*','RF','RF9','RFW','RFW9','Z','Z-','ZJ','ZW','Zh','b','b\'','b*','b:','b<','bD','bJ','bJ<','bJh','bW','bW-',
                        'bh','bm','bv','d','d\'','d*','d-','d.','d.*','d.<','d.h','d.n','d.r','d.z','d<','dD','dD*','dD6','dD9','dD<','dDJ','dDh','dDn','dDz','dJ',
                        'dZ','dZ\'','dZ-','dZJ','dZW','dZh','d_','d_*','d_<','d_n','dj','dj*','dj:','dj<','djjF','djjFW','djz,','dlD','dlF','dn','dz','dz\'','dz-',
                        'dzh','g','g!','g#','g#j','g#jh','g#jx','g#jx?','g\'','g/','g/=','g/=h','g/=x','g/=x?','g/h','g/x','g/x?','g<','gA','gA*','gF','gF*','gFJ','gFW','gJ',
                        'gL','gW','gWh','gb','gbW','gh','gn','g|','g|h','g|x','g|x?','hh','j','j*','jF','j_','j~','l','l*','l-','l.','l.F','l.[','l.[*','l9',
                        'lD','lD-','lD:','lDF','lDFJ','lDJ','lF','lFJ','lJ','l[','l[J','l_','l_h','lj','l~','m','m*','m:','mD','mJ','mW','mW-','mb','mbJ','mbW',
                        'mh','mv','n','n!','n#','n#j','n#jh','n*','n-','n.','n/','n/=','n/=h','n/h','n:','nD','nD*','nDJ','nDh','nJ','nU','nZ','n_','n_h','nd',
                        'nd.','nd.z','ndD','ndDz','ndJ','ndZ','nd_','ndj','ndjjF','ndjz,','ndz','nj','nj*','nj:','njW','nr','nz','nzD','n|','n|h','r','r.','r.A','r.[','r.[~',
                        'rA','rD','rDJ','rDT','rDT*','rD[','rJ','rT','r[','r[*','r[-','r[F','r[J','r_[','rj','rr','rrD','rrJ','v','vA','vJ','vW','v[','vh','w',
                        'w*','wj','w~','z','z,','z.','z.*','zD','zD9','zDJ',]

features['no aspiration, etc.'] =   ['!','!?','"6','"d','"d*','"d9','"d<','"dJ','"dW','"dlF','"dz','"dzJ','"hl','"hlF','"hlF\'','"hlF:','"hlFJ','"hlFW','"hlFW:','"hn','"hr','"hrA',
                                    '"hrr','"l','"l*','"l-','"l9','"lF','"lJ','"l[','"n','"n*','"n:','"nJ','"nW','"r','"r*','"r-','"r9','"rA','"rF','"rJ','"r[','"r[J','"rr','"rr*','"s',
                                    '"s\'','"s9','"s:','"sJ','"sW','"sW:','"t','"t\'','"t*','"t9','"t:','"tJ','"tW','"tlF','"tlF\'','"tlF\':','"tlF*','"tlF:','"tlFW\'','"ts','"ts\'','"ts\':','"ts*',
                                    '"ts:','"tsJ','"tsW\'','"tsW:','"z','"z9','"zJ','"zW','#','#?','#j','#jx','/','/=','/=x','/s','/x','0','0D','0_','6','6','6D','6DJ','6_',
                                    '9','99','?','?9','??','?W','B','BA','BA-','BA:','BAJ','BJ','C','C,','C,\'','CW','G','G9','GW','GW9','H','L','N','N*','N9',
                                    'NJ','NW','Nm','P','P\'','PA','PJ','PW','PW-','R','RA','RAW','RAW*','RF','RF9','RFW','RFW9','S','S\'','S-','S:','SJ','SW','SW:',
                                    'X','X\'','X9','X9:','X:','XW','XW\'','XW9','XW9:','XW:','Z','Z-','ZJ','ZW','b','b\'','b*','b:','b<','bD','bJ','bJ<','bW',
                                    'bW-','bm','bv','c','c\'','c:','cC','cC,','cC,\'','cCW','d','d\'','d*','d-','d.','d.*','d.<','d.n','d.r','d.z','d<','dD','dD*',
                                    'dD6','dD9','dD<','dDJ','dDn','dDz','dJ','dZ','dZ\'','dZ-','dZJ','dZW','d_','d_*','d_<','d_n','dj','dj*','dj:','dj<','djjF','djjFW','djz,','dlF','dn',
                                    'dz','dz\'','dz-','f','f\'','f:','fJ','fW','g','g!','g#','g#j','g#jx','g#jx?','g\'','g/','g/=','g/=x','g/=x?','g/x','g/x?','g<','gA',
                                    'gA*','gF','gF*','gFJ','gFW','gJ','gL','gW','gb','gbW','gn','g|','g|x','g|x?','h','h*','hJ','hLF','hN','hNJ','hNW','hNm','hW','hh','hj',
                                    'hl','hl-','hl.','hlD','hlDF','hlDF:','hlDFJ','hlDFJ\'','hlF','hlFJ','hlJ','hm','hn','hn!?','hn#?','hn#j?','hn#jx?','hn-','hn.','hn/=?',
                                    'hn/=x?','hn/?','hn/x?','hnD','hnJ','hn_','hnj','hn|?','hn|x?','hr','hr[-','hr[J','hw','hxlF','j','j*','jF','j_','j~','k','k\'','k*','k9','k:','kJ',
                                    'kJ\'','kW','kW\'','kW*','kW:','klF','klF\'','kp','kpW','kx','kx\':','kx:','l','l*','l-','l.','l.F','l.[','l.[*','l9','lD','lD-','lD:','lDF',
                                    'lDFJ','lDJ','lF','lFJ','lJ','l[','l[J','l_','lj','l~','m','m*','m:','mD','mJ','mW','mW-','n','n!','n#','n#j','n*','n-','n.','n/',
                                    'n/=','n:','nD','nD*','nDJ','nJ','nU','n_','nj','nj*','nj:','njW','n|','p','p\'','p*','p:','p<','pJ','pW','pf','pf\'','q',
                                    'q\'','q*','q9\'','q:','q<','qW','qW\'','qW*','qW9\'','qW:','qX','qX\'','qX\':','qX9','qX9\'','qX9\':','qX:','qXW','qXW\'','qXW9','qXW9\'','r',
                                    'r.','r.A','r.[','r.[~','rA','rD','rDJ','rDT','rDT*','rD[','rJ','rT','r[','r[*','r[-','r[F','r[J','r_[','rj','rr','rrD','rrJ','s','s\'','s*',
                                    's.','s.\'','s9','s:','sD','sD\'','sD*','sD9','sDJ','sJ','t','t\'','t-','t.','t.*','t.0','t.r','t.s','t.s\'','t0','t:','t<','tD',
                                    'tD\'','tD*','tD0','tD0\'','tD9','tDJ','tDs','tDs\'','tDsJ','tJ','tS','tS\'','tS\':','tS*','tS-','tS:','tSJ','tSW','tSW\'','tSW:','t_','tlF',
                                    'tlF\'','ts','ts\'','ts*','ts-','v','vA','vJ','vW','v[','w','w*','wj','w~','x','x\'','x:','xJ','xW','xW\'','xW:','z','z,','z.',
                                    'z.*','zD','zD9','zDJ','|','|?','|x',]
features['aspirated'] =     ['!h','!xh','"sh','"t-h','"tJh','"tWh','"th','"tlFWh','"tlFh','"tsWh','"tsh','#h','#jh','#xh','/=h','/h','/xh','Nkh','Nqh','cC,h','cCh','ch',
                            'hn!h','hn#h','hn#jh','hn/=h','hn/h','hn|h','kJh','kWh','kh','kph','kxWh','kxh','mph','nt.sh','ntDh','ntDsh','ntSh','pJh','pW-h','pfh','ph','q9h','qW9h','qWh','qh',
                            't.h','t.sh','t0h','tD0h','tDh','tDsh','tSJh','tSWh','tSh','t_h','th','tlFh','tsh','tshh','|h','|xh',]
features['preaspirated'] =  ['"hs','hS','hk','hp','ht','htS',]
features['prestopped'] =    ['dlD']
features['prenasalized'] =  ['"nd','"ndJ','"ndW','"ns','"nt','"nts','"nz','Ng','NgW','Nk','NkJ','NkW','Nkh','Nmgb','Nq','Nqh','mb','mbJ','mbW','mp','mph','mv',
                            'nZ','nc','ncC,','nd','nd.','nd.z','ndD','ndDz','ndJ','ndZ','nd_','ndj','ndjjF','ndjz,','ndz','nr','nt','nt.','nt.s','nt.sh','ntD',
                            'ntDh','ntDs','ntDsh','ntS','ntSh','nt_','nz','nzD',]
features['breathy'] =   ['"dh','"dzh','"lh','"nh','"thh','"tshh','Nh','Zh','bJh','bh','d.h','dDh','dZh','dzh','g#jh','g/=h','g/h','gWh','gh','g|h','khh','l_h',
                        'mh','n#jh','n/=h','n/h','nDh','n_h','n|h','phh','tDhh','thh','tshh','vh',]

features['no sec. articulation'] =  ['!','!?','!h','!xh','"6','"d','"d<','"dh','"dlF','"dz','"dzh','"hl','"hlF','"hlF\'','"hlF:','"hn','"hr','"hrA','"hrr','"hs','"l','"lF',
                                    '"l[','"lh','"n','"n:','"nd','"nh','"ns','"nt','"nts','"nz','"r','"rA','"rF','"r[','"rr','"s','"s\'','"s:','"sh','"t','"t\'','"t:','"th','"thh',
                                    '"tlF','"tlF\'','"tlF\':','"tlF:','"tlFh','"ts','"ts\'','"ts\':','"ts:','"tsh','"tshh','"z','#','#?','#h','#j','#jh','#jx','#xh','/','/=','/=h','/=x','/h',
                                    '/s','/x','/xh','0','0D','0_','6','6','6D','6_','9','99','?','??','B','BA','BA:','C','C,','C,\'','G','H','L','N',
                                    'Ng','Nh','Nk','Nkh','Nm','Nmgb','Nq','Nqh','P','P\'','PA','R','RA','RF','S','S\'','S:','X','X\'','X:','Z','Zh','b',
                                    'b\'','b:','b<','bD','bh','bm','bv','c','c\'','c:','cC','cC,','cC,\'','cC,h','cCh','ch','d','d\'','d.','d.<','d.h','d.n','d.r','d.z',
                                    'd<','dD','dD6','dD<','dDh','dDn','dDz','dZ','dZ\'','dZh','d_','d_<','d_n','dj','dj:','dj<','djjF','djz,','dlD','dlF','dn','dz','dz\'','dzh',
                                    'f','f\'','f:','g','g!','g#','g#j','g#jh','g#jx','g#jx?','g\'','g/','g/=','g/=h','g/=x','g/=x?','g/h','g/x','g/x?','g<','gA','gF','gL','gb',
                                    'gh','gn','g|','g|h','g|x','g|x?','h','hLF','hN','hNm','hS','hh','hj','hk','hl','hl.','hlD','hlDF','hlDF:','hlF','hm','hn','hn.','hnD','hn_',
                                    'hnj','hp','hr','ht','htS','hw','hxlF','j','jF','j_','k','k\'','k:','kh','khh','klF','klF\'','kp','kph','kx','kx\':','kx:','kxh','l',
                                    'l.','l.F','l.[','lD','lD:','lDF','lF','l[','l_','l_h','lj','m','m:','mD','mb','mh','mp','mph','mv','n','n.','n:','nD','nDh','nU',
                                    'nZ','n_','n_h','nc','ncC,','nd','nd.','nd.z','ndD','ndDz','ndZ','nd_','ndj','ndjjF','ndjz,','ndz','nj','nj:','nr','nt','nt.','nt.s','nt.sh','ntD','ntDh',
                                    'ntDs','ntDsh','ntS','ntSh','nt_','nz','nzD','p','p\'','p:','p<','pf','pf\'','pfh','ph','phh','q','q\'','q:','q<','qX','qX\'','qX\':',
                                    'qX:','qh','r','r.','r.A','r.[','rA','rD','rDT','rD[','rT','r[','r[*','r[F','r_[','rj','rr','rrD','s','s\'','s.','s.\'','s:','sD',
                                    'sD\'','t','t\'','t.','t.0','t.h','t.r','t.s','t.s\'','t.sh','t0','t0h','t:','t<','tD','tD\'','tD0','tD0\'','tD0h','tDh','tDhh','tDs',
                                    'tDs\'','tDsh','tS','tS\'','tS\':','tS:','tSh','t_','t_h','th','thh','tlF','tlF\'','tlFh','ts','ts\'','tsh','tshh','v','vA','v[','vh','w',
                                    'wj','x','x\'','x:','z','z,','z.','zD','|','|?','|h','|x',]
features['labialized'] =    ['"dW','"hlFW','"hlFW:','"nW','"ndW','"sW','"sW:','"tW','"tWh','"tlFW\'','"tlFWh','"tsW\'','"tsW:','"tsWh','"zW','?W','CW','GW','GW9','NW','NgW','NkW',
                            'PW','PW-','RAW','RAW*','RFW','RFW9','SW','SW:','XW','XW\'','XW9','XW9:','XW:','ZW','bW','bW-','cCW','dZW','djjFW','fW','gFW','gW','gWh','gbW','hNW',
                            'hW','kW','kW\'','kW*','kW:','kWh','kpW','kxWh','mW','mW-','mbW','njW','pW','pW-h','qW','qW\'','qW*','qW9\'','qW9h','qW:','qWh','qXW','qXW\'','qXW9',
                            'qXW9\'','tSW','tSW\'','tSW:','tSWh','vW','xW','xW\'','xW:',]
features['palatalized'] =   ['"dJ','"dzJ','"hlFJ','"lJ','"nJ','"ndJ','"rJ','"r[J','"sJ','"tJ','"tJh','"tsJ','"zJ','6DJ','BAJ','BJ','NJ','NkJ','PJ','SJ','ZJ','bJ',
                            'bJ<','bJh','dDJ','dJ','dZJ','fJ','gFJ','gJ','hJ','hNJ','hlDFJ','hlDFJ\'','hlFJ','hlJ','hnJ','hr[J','kJ','kJ\'','kJh','lDFJ','lDJ','lFJ',
                            'lJ','l[J','mJ','mbJ','nDJ','nJ','ndJ','pJ','pJh','rDJ','rJ','r[J','rrJ','sDJ','sJ','tDJ','tDsJ','tJ','tSJ','tSJh','vJ','xJ','zDJ',]
features['velarized'] =     ['"l-','"r-','"t-h','BA-','PW-','S-','Z-','bW-','d-','dZ-','dz-','hl-','hn-','hn/x?','hr[-','l-','lD-','mW-','n-','pW-h','r[-','t-',
                            'tS-','ts-','|xh',]

features['bilabial'] =  ['B','BA','BA-','BA:','BAJ','BJ','P','P\'','PA','PJ','PW','PW-','b','b\'','b*','b:','b<','bJ','bJ<','bJh','bW','bW-',
                        'bh','bm','hm','hp','m','m*','m:','mJ','mW','mW-','mb','mbJ','mbW','mh','mp','mph','p','p\'','p*','p:','p<','pJ','pJh',
                        'pW','pW-h','ph','phh',]
features['labiodental'] =   ['bD','bv','f','f\'','f:','fJ','fW','mD','mv','pf','pf\'','pfh','v','vA','vJ','vW','v[','vh',]
features['dental'] =    ['0D','6D','6DJ','dD','dD*','dD6','dD9','dD<','dDJ','dDh','dDn','dDz','dlD','g|','g|h','g|x','g|x?','hlD','hlDF','hlDF:','hlDFJ','hlDFJ\'',
                        'hnD','hn|?','hn|h','hn|x?','lD','lD-','lD:','lDF','lDFJ','lDJ','nD','nD*','nDJ','nDh','ndD','ndDz','ntD','ntDh','ntDs','ntDsh','nzD','n|','n|h','rD',
                        'rDJ','rDT','rDT*','rD[','rrD','sD','sD\'','sD*','sD9','sDJ','tD','tD\'','tD*','tD0','tD0\'','tD0h','tD9','tDJ','tDh','tDhh','tDs','tDs\'','tDsJ','tDsh',
                        'zD','zD9','zDJ','|','|?','|h','|x','|xh',]
features['dental/alveolar'] =   ['"6','"d','"d*','"d9','"d<','"dJ','"dW','"dh','"dlF','"dz','"dzJ','"dzh','"hl','"hlF','"hlF\'','"hlF:','"hlFJ','"hlFW','"hlFW:','"hn','"hr','"hrA',
                                '"hrr','"hs','"l','"l*','"l-','"l9','"lF','"lJ','"l[','"lh','"n','"n*','"n:','"nJ','"nW','"nd','"ndJ','"ndW','"nh','"ns','"nt','"nts','"nz','"r','"r*',
                                '"r-','"r9','"rA','"rF','"rJ','"r[','"r[J','"rr','"rr*','"s','"s\'','"s9','"s:','"sJ','"sW','"sW:','"sh','"t','"t\'','"t*','"t-h','"t9','"t:','"tJ',
                                '"tJh','"tW','"tWh','"th','"thh','"tlF','"tlF\'','"tlF\':','"tlF*','"tlF:','"tlFW\'','"tlFWh','"tlFh','"ts','"ts\'','"ts\':','"ts*','"ts:','"tsJ','"tsW\'',
                                '"tsW:','"tsWh','"tsh','"tshh','"z','"z9','"zJ','"zW',]
features['alveolar'] =  ['#','#?','#h','#xh','/','/h','/s','/x','/xh','6','d','d\'','d*','d-','d<','dJ','dlF','dn','dz','dz\'','dz-','dzh',
                        'g#','g/','g/h','g/x','g/x?','hl','hl-','hlF','hlFJ','hlJ','hn','hn#?','hn#h','hn-','hn/?','hn/h','hn/x?','hnJ','hr',
                        'hr[-','hr[J','ht','klF','l','l*','l-','l9','lF','lFJ','lJ','l[','l[J','l~','n','n#','n*','n-','n/','n/h','n:','nJ','nd','ndJ','ndz',
                        'nr','nt','nz','r','rA','rJ','rT','r[','r[*','r[-','r[F','r[J','rr','rrJ','s','s\'','s*','s9','s:','sJ','t','t\'','t-','t0',
                        't0h','t:','t<','tJ','th','thh','tlF','tlF\'','tlFh','ts','ts\'','ts*','ts-','tsh','tshh','z',]
features['palato-alveolar'] =   ['!','!?','!h','!xh','0_','6_','S','S\'','S-','S:','SJ','SW','SW:','Z','Z-','ZJ','ZW','Zh','dZ','dZ\'','dZ-','dZJ',
                                'dZW','dZh','d_','d_*','d_<','d_n','g!','hS','hn!?','hn!h','hn_','htS','j_','l_','l_h','n!','nZ','n_','n_h','ndZ','nd_',
                                'ntS','ntSh','nt_','r_[','tS','tS\'','tS\':','tS*','tS-','tS:','tSJ','tSJh','tSW','tSW\'','tSW:','tSWh','tSh','t_','t_h',]
features['retroflex'] =     ['0','6','d.','d.*','d.<','d.h','d.n','d.r','d.z','hl.','hn.','l.','l.F','l.[','l.[*','n.','nd.','nd.z','nt.','nt.s','nt.sh',
                            'r.','r.A','r.[','r.[~','s.','s.\'','t.','t.*','t.0','t.h','t.r','t.s','t.s\'','t.sh','z.','z.*',]
features['palatal'] =   ['#j','#jh','#jx','/=','/=h','/=x','C','C,','C,\'','CW','c','c\'','c:','cC','cC,','cC,\'','cC,h','cCW','cCh','ch','dj','dj*',
                        'dj:','dj<','djjF','djjFW','djz,','g#j','g#jh','g#jx','g#jx?','g/=','g/=h','g/=x','g/=x?','hj','hn#j?','hn#jh','hn#jx?','hn/=?',
                        'hn/=h','hn/=x?','hnj','j','j*','jF','j~','lj','n#j','n#jh','n/=','n/=h','nc','ncC,','ndj','ndjjF','ndjz,','nj','nj*','nj:','njW','rj','z,',]
features['labial-palatal'] =    ['wj']
features['velar'] =     ['L','N','N*','N9','NJ','NW','Ng','NgW','Nh','Nk','NkJ','NkW','Nkh','g','g\'','g<','gA','gA*','gF','gF*','gFJ','gFW',
                        'gJ','gL','gW','gWh','gh','gn','hLF','hN','hNJ','hNW','hk','k','k\'','k*','k9','k:','kJ','kJ\'','kJh','kW','kW\'','kW*','kW:','kWh',
                        'kh','khh','klF','klF\'','kx','kx\':','kx:','kxWh','kxh','x','x\'','x:','xJ','xW','xW\'','xW:',]
features['velar-alveolar'] =    ['hxlF']
features['labial-velar'] =  ['Nm','Nmgb','gb','gbW','hNm','hw','kp','kpW','kph','w','w*','w~',]
features['uvular'] =    ['G','G9','GW','GW9','Nq','Nqh','R','RA','RAW','RAW*','RF','RF9','RFW','RFW9','X','X\'','X9','X9:','X:','XW','XW\'','XW9',
                        'XW9:','XW:','nU','q','q\'','q*','q9\'','q9h','q:','q<','qW','qW\'','qW*','qW9\'','qW9h','qW:','qWh','qX','qX\'','qX\':','qX9',
                        'qX9\'','qX9\':','qX:','qXW','qXW\'','qXW9','qXW9\'','qh',]
features['pharyngeal'] =    ['9','99','H']
features['glottal'] =   ['?','?9','??','?W','h','h*','hJ','hW','hh',]

features['sibilant'] =  ['"dz','"dzJ','"dzh','"hs','"ns','"nts','"nz','"s','"s\'','"s9','"s:','"sJ','"sW','"sW:','"sh','"ts','"ts\'','"ts\':','"ts*','"ts:','"tsJ',
                        '"tsW\'','"tsW:','"tsWh','"tsh','"tshh','"z','"z9','"zJ','"zW','C,','C,\'','S','S\'','S-','S:','SJ','SW','SW:','Z','Z-','ZJ','ZW','Zh','cC,',
                        'cC,\'','cC,h','d.z','dDz','dZ','dZ\'','dZ-','dZJ','dZW','dZh','djz,','dz','dz\'','dz-','dzh','hS','htS','nZ','ncC,','nd.z','ndDz','ndZ','ndjz,',
                        'ndz','nt.s','nt.sh','ntDs','ntDsh','ntS','ntSh','nz','nzD','s','s\'','s*','s.','s.\'','s9','s:','sD','sD\'','sD*','sD9','sDJ','sJ','t.s',
                        't.s\'','t.sh','tDs','tDs\'','tDsJ','tDsh','tS','tS\'','tS\':','tS*','tS-','tS:','tSJ','tSJh','tSW','tSW\'','tSW:','tSWh','tSh','ts','ts\'',
                        'ts*','ts-','tsh','tshh','z','z,','z.','z.*','zD','zD9','zDJ',]
features['lateral'] =   ['"dlF','"hl','"hlF','"hlF\'','"hlF:','"hlFJ','"hlFW','"hlFW:','"l','"l*','"l-','"l9','"lF','"lJ','"l[','"lh','"tlF','"tlF\'','"tlF\':','"tlF*','"tlF:',
                        '"tlFW\'','"tlFWh','"tlFh','#','#?','#h','#j','#jh','#jx','#xh','L','dlD','dlF','g#','g#j','g#jh','g#jx','g#jx?','hLF','hl','hl-','hl.','hlD','hlDF','hlDF:',
                        'hlDFJ','hlDFJ\'','hlF','hlFJ','hlJ','hn#?','hn#h','hn#j?','hn#jh','hn#jx?','hxlF','klF','klF\'','l','l*','l-','l.','l.F','l.[','l.[*','l9','lD','lD-','lD:',
                        'lDF','lDFJ','lDJ','lF','lFJ','lJ','l[','l[J','l_','l_h','lj','l~','n#','n#j','n#jh','tlF','tlF\'','tlFh',]

features['click'] =     ['!','!?','!h','!xh','/','/=','/=h','/=x','/h','/x','/xh','g!','g/','g/=','g/=h','g/=x','g/=x?','g/h','g/x','g/x?',
                        'hn!?','hn!h','hn/=?','hn/=h','hn/=x?','hn/?','hn/h','hn/x?','n!','n/','n/=','n/=h','n/h',]
features['affricated click'] =  ['#','#?','#h','#j','#jh','#jx','#xh','/s','g#','g#j','g#jh','g#jx','g#jx?','g|','g|h','g|x','g|x?','hn#?','hn#h','hn#j?','hn#jh',
                                'hn#jx?','hn|?','hn|h','hn|x?','n#','n#j','n#jh','n|','n|h','|','|?','|h','|x',]
features['velar-fricated click'] =  ['!xh','#jx','#xh','/=x','/x','/xh','g#jx','g#jx?','g/=x','g/=x?','g/x','g/x?','g|x','g|x?','hn#jx?','hn/=x?','hn|x?','|x',]
features['ejective stop'] =     ['"t\'','b\'','c\'','d\'','g\'','k\'','kJ\'','kW\'','p\'','q\'','q9\'','qW\'','qW9\'','t\'','tD\'',]
features['ejective fricative'] =    ['"hlF\'','"s\'','C,\'','P\'','S\'','X\'','XW\'','f\'','hlDFJ\'','s\'','s.\'','sD\'','x\'','xW\'',]
features['ejective affricate'] =    ['"tlF\'','"tlF\':','"tlFW\'','"ts\'','"ts\':','"tsW\'','cC,\'','dZ\'','dz\'','klF\'','kx\':','pf\'','qX\'','qX\':','qX9\'','qX9\':','qXW\'',
                                    'qXW9\'','t.s\'','tD0\'','tDs\'','tS\'','tS\':','tSW\'','tlF\'','ts\'',]
features['implosive'] =     ['"d<','b<','bJ<','d.<','d<','dD<','d_<','dj<','g<','p<','q<','t<',]
features['plosive'] =   ['"d','"d*','"d9','"dJ','"dW','"dh','"nd','"ndJ','"ndW','"nt','"t','"t*','"t-h','"t9','"t:','"tJ','"tJh','"tW','"tWh','"th','"thh','99',
                        '?','?9','??','?W','G','G9','GW','GW9','Ng','NgW','Nk','NkJ','NkW','Nkh','Nmgb','Nq','Nqh','b','b*','b:','bD','bJ','bJh','bW','bW-',
                        'bh','bm','c','c:','ch','d','d*','d-','d.','d.*','d.h','d.n','dD','dD*','dD9','dDJ','dDh','dDn','dJ','d_','d_*','d_n','dj','dj*','dj:',
                        'dn','g','gJ','gL','gW','gWh','gb','gbW','gh','gn','hk','hp','ht','k','k*','k9','k:','kJ','kJh','kW','kW*','kW:','kWh','kh','khh',
                        'klF','kp','kpW','kph','mb','mbJ','mbW','mp','mph','nc','nd','nd.','ndD','ndJ','nd_','ndj','nt','nt.','ntD','ntDh','nt_','p','p*','p:','pJ',
                        'pJh','pW','pW-h','ph','phh','q','q*','q9h','q:','qW','qW*','qW9h','qW:','qWh','qh','t','t-','t.','t.*','t.h','t:','tD','tD*','tD9','tDJ',
                        'tDh','tDhh','tJ','t_','t_h','th','thh',]
features['tap/flap'] = tapflap
features['(affricated) trill'] = trill
features['nasal'] = nasal
features['affricate'] = affricate
features['fricative'] = fricative
features['r-sound'] =   ['"hrr','"rr','"rr*','rr','rrD','rrJ',]
features['approximant'] =   ['"hl','"hrA','"l','"l*','"l-','"l9','"lJ','"lh','"rA','BA','BA-','BA:','BAJ','L','PA','RA','RAW','RAW*','dlD','gA','gA*',
                            'hj','hl','hl-','hl.','hlD','hlJ','hw','j','j*','j_','j~','l','l*','l-','l.','l9','lD','lD-','lD:','lDJ','lJ','l_','l_h','lj','l~',
                            'r.A','rA','vA','w','w*','wj','w~',]

features['no release modifier'] =   ['!','!?','!h','!xh','"6','"d','"d*','"d9','"d<','"dJ','"dW','"dh','"dlF','"dz','"dzJ','"dzh','"hl','"hlF','"hlF\'','"hlF:','"hlFJ','"hlFW',
                                    '"hlFW:','"hn','"hr','"hrA','"hrr','"hs','"l','"l*','"l-','"l9','"lF','"lJ','"l[','"lh','"n','"n*','"n:','"nJ','"nW','"nd','"ndJ','"ndW','"nh','"ns','"nt',
                                    '"nts','"nz','"r','"r*','"r-','"r9','"rA','"rF','"rJ','"r[','"r[J','"rr','"rr*','"s','"s\'','"s9','"s:','"sJ','"sW','"sW:','"sh','"t','"t\'',
                                    '"t*','"t-h','"t9','"t:','"tJ','"tJh','"tW','"tWh','"th','"tlF','"tlF\'','"tlF\':','"tlF*','"tlF:','"tlFW\'','"tlFWh','"tlFh','"ts','"ts\'',
                                    '"ts\':','"ts*','"ts:','"tsJ','"tsW\'','"tsW:','"tsWh','"tsh','"z','"z9','"zJ','"zW','#','#?','#h','#j','#jh','#jx','#xh','/','/=','/=h','/=x',
                                    '/h','/s','/x','/xh','0','0D','0_','6','6','6D','6DJ','6_','9','99','?','?9','??','?W','B','BA','BA-','BA:','BAJ','BJ','C',
                                    'C,','C,\'','CW','G','G9','GW','GW9','H','L','N','N*','N9','NJ','NW','Ng','NgW','Nh','Nk','NkJ','NkW','Nkh','Nm','Nmgb','Nq',
                                    'Nqh','P','P\'','PA','PJ','PW','PW-','R','RA','RAW','RAW*','RF','RF9','RFW','RFW9','S','S\'','S-','S:','SJ','SW','SW:','X','X\'',
                                    'X9','X9:','X:','XW','XW\'','XW9','XW9:','XW:','Z','Z-','ZJ','ZW','Zh','b','b\'','b*','b:','b<','bD','bJ','bJ<','bJh','bW','bW-',
                                    'bh','bv','c','c\'','c:','cC','cC,','cC,\'','cC,h','cCW','cCh','ch','d','d\'','d*','d-','d.','d.*','d.<','d.h','d.r','d.z','d<','dD',
                                    'dD*','dD6','dD9','dD<','dDJ','dDh','dDz','dJ','dZ','dZ\'','dZ-','dZJ','dZW','dZh','d_','d_*','d_<','dj','dj*','dj:','dj<','djjF','djjFW',
                                    'djz,','dlD','dlF','dz','dz\'','dz-','dzh','f','f\'','f:','fJ','fW','g','g!','g#','g#j','g#jh','g#jx','g#jx?','g\'','g/','g/=','g/=h','g/=x',
                                    'g/=x?','g/h','g/x','g/x?','g<','gA','gA*','gF','gF*','gFJ','gFW','gJ','gW','gWh','gb','gbW','gh','g|','g|h','g|x','g|x?','h','h*','hJ','hLF',
                                    'hN','hNJ','hNW','hNm','hS','hW','hh','hj','hk','hl','hl-','hl.','hlD','hlDF','hlDF:','hlDFJ','hlDFJ\'','hlF','hlFJ','hlJ','hm','hn','hn!?',
                                    'hn!h','hn#?','hn#h','hn#j?','hn#jh','hn#jx?','hn-','hn.','hn/=?','hn/=h','hn/=x?','hn/?','hn/h','hn/x?','hnD','hnJ','hn_','hnj','hn|?','hn|h',
                                    'hn|x?','hp','hr','hr[-','hr[J','ht','htS','hw','hxlF','j','j*','jF','j_','j~','k','k\'','k*','k9','k:','kJ','kJ\'','kJh','kW','kW\'',
                                    'kW*','kW:','kWh','kh','klF\'','kp','kpW','kph','kx','kx\':','kx:','kxWh','kxh','l','l*','l-','l.','l.F','l.[','l.[*','l9','lD','lD-','lD:',
                                    'lDF','lDFJ','lDJ','lF','lFJ','lJ','l[','l[J','l_','l_h','lj','l~','m','m*','m:','mD','mJ','mW','mW-','mb','mbJ','mbW','mh','mp','mph',
                                    'mv','n','n!','n#','n#j','n#jh','n*','n-','n.','n/','n/=','n/=h','n/h','n:','nD','nD*','nDJ','nDh','nJ','nU','nZ','n_','n_h','nc','ncC,',
                                    'nd','nd.','nd.z','ndD','ndDz','ndJ','ndZ','nd_','ndj','ndjjF','ndjz,','ndz','nj','nj*','nj:','njW','nr','nt','nt.','nt.s','nt.sh','ntD',
                                    'ntDh','ntDs','ntDsh','ntS','ntSh','nt_','nz','nzD','n|','n|h','p','p\'','p*','p:','p<','pJ','pJh','pW','pW-h','pf','pf\'','pfh','ph','q',
                                    'q\'','q*','q9\'','q9h','q:','q<','qW','qW\'','qW*','qW9\'','qW9h','qW:','qWh','qX','qX\'','qX\':','qX9','qX9\'','qX9\':','qX:','qXW','qXW\'',
                                    'qXW9','qXW9\'','qh','r','r.','r.A','r.[','r.[~','rA','rD','rDJ','rDT','rDT*','rD[','rJ','rT','r[','r[*','r[-','r[F','r[J','r_[','rj','rr',
                                    'rrD','rrJ','s','s\'','s*','s.','s.\'','s9','s:','sD','sD\'','sD*','sD9','sDJ','sJ','t','t\'','t-','t.','t.*','t.0','t.h','t.r','t.s',
                                    't.s\'','t.sh','t0','t0h','t:','t<','tD','tD\'','tD*','tD0','tD0\'','tD0h','tD9','tDJ','tDh','tDs','tDs\'','tDsJ','tDsh','tJ','tS','tS\'',
                                    'tS\':','tS*','tS-','tS:','tSJ','tSJh','tSW','tSW\'','tSW:','tSWh','tSh','t_','t_h','th','tlF','tlF\'','tlFh','ts','ts\'','ts*','ts-','tsh',
                                    'v','vA','vJ','vW','v[','vh','w','w*','wj','w~','x','x\'','x:','xJ','xW','xW\'','xW:','z','z,','z.','z.*','zD','zD9','zDJ',
                                    '|','|?','|h','|x','|xh',]
features['with breathy/fricative release'] =    ['"thh','"tshh','khh','klF','phh','tDhh','thh','tshh',]
features['laterally released'] =    ['gL']
features['nasally released'] =  ['bm','d.n','dDn','d_n','dn','gn',]
features['any release modifier'] = features[
    'with breathy/fricative release']+features[
    'laterally released']+features['nasally released']

not_in_upsid = []
for d in dictionaries:
    for s in d:
        if not s in all_features:
            not_in_upsid.append(s)
not_in_upsid = set(not_in_upsid)
percent_not_in_upsid = len(not_in_upsid)/(len(not_in_upsid)+len(all_features))
