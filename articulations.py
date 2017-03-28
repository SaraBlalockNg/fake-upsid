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

features['overshort'] = []
features['short'] = [] # for both v & c
features['long'] = [] # for both v & c

features['no modifier'] = [] # for both v & c
features['fricative'] = []
features['retroflexed'] = []
features['pharyngealized'] = [] # for both v & c
features['laryngealized'] = [] # for both v & c
features['nasalized'] = []

features['breathy voicing'] = []
features["'normal' voicing"] = []
features['voiceless'] = [] # both v & c

features['high'] = []
features['lowered high'] = []
features['higher mid'] = []
features['mid'] = []
features['lower mid'] = []
features['raised low'] = []
features['low'] = []

features['front'] = []
features['retracted front'] = []
features['central'] = []
features['fronted back'] = []
features['back'] = []

features['unrounded'] = []
features['rounded'] = []
features['Monopthong'] = []
features['Diphthong'] = []

features['voiced'] = []

features['no aspiration, etc.'] = []
features['aspirated'] = []
features['preaspirated'] = []
features['prestopped'] = []
features['prenasalized'] = []
features['breathy'] = []

features['no sec. articulation'] = []
features['labialized'] = []
features['palatalized'] = []
features['velarized'] = []

features['bilabial'] = []
features['labiodental'] = []
features['dental'] = []
features['dental/alveolar'] = []
features['alveolar'] = []
features['palato-alveolar'] = []
features['retroflex'] = []
features['palatal'] = []
features['labial-palatal'] = []
features['velar'] = []
features['velar-alveolar'] = []
features['labial-velar'] = []
features['uvular'] = []
features['pharyngeal'] = []
features['glottal'] = []

features['sibilant'] = []
features['lateral'] = []

features['click'] = []
features['affricated click'] = []
features['velar-fricated click'] = []
features['ejective stop'] = []
features['ejective fricative'] = []
features['ejective affricate'] = []
features['implosive'] = []
features['plosive'] = []
features['tap/flap'] = tapflap
features['(affricated) trill'] = []
features['nasal'] = []
features['affricate'] = []
features['fricative'] = []
features['r-sound'] = []
features['approximant'] = []

features['no release modifier'] = []
features['with breathy/fricative release'] = []
features['laterally released'] = []
features['nasally released'] = []
features['any release modifier'] = features[
    'with breathy/fricative release']+features[
    'laterally released']+features['nasally released']

not_in_upsid = []
for d in dictionaries:
    for s in d:
        if not s in all_features:
            not_in_upsid.append(s)
not_in_upsid = set(not_in_upsid)
print(not_in_upsid)
percent_not_in_upsid = len(not_in_upsid)/(len(not_in_upsid)+len(all_features))
