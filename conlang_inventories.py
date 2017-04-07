from tkinter import *
from tkinter import font
from functools import partial
from inventories import *
from articulations import *
import textwrap


class App(Frame):
   
    def __init__(self, master=None, *pargs):
        
        Frame.__init__(self, master, *pargs)
        self.master.title("CLIPS")
        self.master.minsize(600, 100)
        self.grid(row = 0)

        # all the widgets for the home page
        self.welcome = Label(text = "This is the interface "
                                 "to the conlang UPSID analog.",
                                 wraplength = 1230, 
                                 bg = "white",
                                 justify = "right")
        self.welcome.grid(row = 0, column = 0,
                              columnspan = 2,padx=10,pady=10, sticky=W)
        self.question = Label(text= "Do you want to:", bg = 'white')
        self.question.grid(row = 1, column = 0,pady=5, padx=10)
        
        self.ask_info = Label(text = "get information about a langauge?",
                              bg = 'white', fg= 'blue', cursor= "hand2",
                              justify = "left")
        self.ask_info.grid(row = 2, column = 1,pady=5, sticky=W)
        self.ask_info.bind("<Button-1>",self.info)

        self.sort_sound = Label(text = "sort languages by the number of sounds?",
                              bg = 'white', fg= 'blue', cursor= "hand2")
        self.sort_sound.grid(row = 3, column = 1,pady=5, sticky=W)
        self.sort_sound.bind("<Button-1>",self.sort_by_sound)

        self.sort_freq = Label(text = "sort languages by their frequency index?",
                              bg = 'white', fg= 'blue', cursor= "hand2")
        self.sort_freq.grid(row = 4, column = 1,pady=5, sticky=W)
        self.sort_freq.bind("<Button-1>",self.sort_by_freq)
        
        self.ask_class = Label(text = "get information about a language class?",
                              bg = 'white', fg= 'blue', cursor= "hand2")
        self.ask_class.grid(row = 5, column = 1,pady=5, sticky=W)
        self.ask_class.bind("<Button-1>",self.classes)

        self.ask_find = Label(text = "find certain sounds and languages that have them?",
                              bg = 'white', fg= 'blue', cursor= "hand2")
        self.ask_find.grid(row = 6, column = 1,pady=5, sticky=W)
        self.ask_find.bind("<Button-1>",self.find_langs_with)

        self.ask_compare = Label(text = "compare two languages?",
                              bg = 'white', fg= 'blue', cursor= "hand2")
        self.ask_compare.grid(row = 7, column = 1,pady=5, sticky=W)
        self.ask_compare.bind("<Button-1>",self.compare)

        # button to return to the home page
        self.home_button = Button(text = "Home")
        self.home_button.bind("<Button-1>",self.home)

        self.master.configure(bg="white")
        
        # 'hyperlinks to info about a langauge, used throughout
        # the interface
        self.list = []
        for language in upper_languages:
            x = Label(text = language, anchor = NW,
                              bg = 'white', fg= 'blue', cursor= "hand2")
            x.bind('<Button-1>',partial(self.language_info,
                                        lang = language))
            self.list.append(x)

        self.mapping = {}
        self.langs_with_counts = []
        count = 0
        for language in languages:
            self.mapping[language] = self.list[languages.index(language)]
            self.langs_with_counts.append(language+ " ("+str(len(
                dictionaries[count]))+")")
            count+=1
        self.counts = None
        self.count_list = []
        self.things = []
   
    def info (self,event) :
        """A list of langauges organized alphabetically you can click on"
"to find more about."""
        self.clear_home_board()
        self.welcome['text']="Click on a language to learn about it's inventory:"
        row_count = 1
        column_count = 1
        for language in self.list:
            if row_count > 15:
                row_count = 1
                column_count = 2
            language.grid(row = row_count, column =column_count)
            row_count +=1

    def language_info (self,event,**lang):
        self.clear_home_board()
        for itme in self.count_list:
            itme.grid_forget()
        for itme in self.things:
            itme.grid_forget()
        self.welcome['text']="Displaying information for "+list(lang.values())[0]+":"
        for item in self.list:
            item.grid_forget()
        index_of_lang = languages.index(list(lang.values())[0].lower())
        self.s = ' '.join(dictionaries[index_of_lang])
        self.inventory = Label(text = self.s,anchor = NW,
                               wraplength = 700,
                              bg = 'white')
        self.inventory.grid(row = 1,column = 0, pady = 30, padx = 40)
        self.counter = Label(text = "# of segments = " +str(
            len(dictionaries[index_of_lang])))
        self.counter.grid(row = 2, column = 0)
        self.home_button.bind('<Button-1>',self.remove_inventory)
        self.home_button.grid(row = 3, column = 0,pady = 30)

    def remove_inventory (self,event):
        self.inventory.grid_forget()
        self.counter.grid_forget()
        self.home(event)
          
    def sort_by_sound (self,event):
        """Returns an ordered list of languages by number of sounds."""
        self.clear_home_board()
        self.welcome['text']="Languages from least number of phonemes to most:"
        self.ordered_dicts = sorted(dictionaries,key=lambda dic:len(dic))
        count = 1
        self.count_list = []

        for item in self.ordered_dicts:
            x = dictionaries.index(item)
            x_i = self.mapping[languages[x]]
            x_i.grid(row=count,column=0)
            self.count_list.append(x_i)
            y = Label(text = str(len(item)),bg='white')
            y.grid(row = count,column = 1)
            self.count_list.append(y)
            count +=1

    
            
        self.home_button.bind('<Button-1>',self.remove_list)
        self.home_button.grid(row = 1, column = 2)

    def remove_list (self,event):
        for widget in self.winfo_children():
            widget.destroy()
        for widget in self.count_list:
            widget.grid_forget()
        self.home(event)
                   
    def sort_by_freq (self,event):
        """Returns a 3 columm table of Freq. index, # of segments, and "
"language"""
        self.welcome['text']=''
        self.clear_home_board()
        self.freqlab = Label(text = 'Frequency Index', bg= 'white')
        self.freqlab.grid(row = 0, column = 0, padx= 10,pady = 10)
        self.ns = Label(text = '# of segments',bg='white')
        self.ns.grid(row = 0, column = 1, padx= 10,pady = 10)
        self.lng = Label(text = 'Language',bg = 'white')
        self.lng.grid(row = 0, column = 2, padx= 10,pady = 10)
        self.home_button.bind('<Button-1>',self.remove_frequencies)
        self.home_button.grid(row = 2,column =3, rowspan = 2, padx=20)

        self.things = [self.freqlab,self.ns,self.lng]

        for i in range(0,len(sorted_languages)):
            x = Label(text = str(least_to_greatest[i]),bg = 'white')
            x.grid(row = i+1,column = 0,padx = 10)
            self.things.append(x)
            w = languages.index(sorted_languages[i])
            y = Label(text = str(len(dictionaries[w])),bg='white')
            y.grid(row = i+1,column = 1,padx = 10)
            self.things.append(y)
            self.list[w].grid(row=i+1,column = 2,padx=10)
            self.things.append(self.list[w])
        
    def remove_frequencies(self,event):
        for widget in self.things:
            widget.grid_forget()
        self.home(event)
    def classes (self,event):
        """Returns a list of language classes.  When you click on them, "
"you can see which languages are a part of that class."""
        pad  = 10
        self.clear_home_board()
        
        self.welcome['text'] = 'These are the language classes (click to see languages).'
        self.art = Label(text = 'Artistic (19 languages)', bg = 'white',
                         fg = 'blue')
        self.eng = Label(text = 'Engineered (7 languages)', bg = 'white',
                         fg = 'blue')        
        self.aux = Label(text = 'Auxiliary Languages (5 languages)', bg = 'white',
                         fg = 'blue')
        self.art.bind('<Button-1>',partial(self.show_class,lang = 'artistic'))
        self.eng.bind('<Button-1>',partial(self.show_class,lang = 'engineered'))
        self.aux.bind('<Button-1>',partial(self.show_class,
                                           lang = 'auxiliary language'))
        self.art.grid(row =1, column = 0, columnspan =2,padx= pad,pady=pad)
        self.eng.grid(row =2, column = 0, columnspan =2,padx= pad,pady=pad)
        self.aux.grid(row =3, column = 0, columnspan =2,padx= pad,pady=pad)

        self.classes = [self.art,self.eng,self.aux]

        self.home_button.bind('<Button-1>',self.remove_classes)
        self.home_button.grid(row = 4,column = 0, columnspan = 2, padx = pad*2,
                       pady=pad*2)

    def remove_classes(self,event):
        for widget in self.classes:
            widget.grid_forget()
        self.home(event)
            
    def show_class(self,event,**lang):
        for widget in self.classes:
            widget.grid_forget()
        clas = list(lang.values())[0]
        self.welcome['text']= "Languages in the "+clas+" class."
        self.langs_in_class = []
        rowcount = 1
        for lang in classes[clas]:
            self.langs_in_class.append(self.list[languages.index(lang)])
            self.list[languages.index(lang)].grid(row = rowcount,column = 0)
            rowcount+=1
        self.home_button.bind('<Button-1>',self.remove_class_list)
        self.home_button.grid(row=2,rowspan = 2, column = 1)

    def remove_class_list(self,event):
        for widget in self.langs_in_class:
            widget.grid_forget()
        self.home(event)
        
    def find_langs_with (self,event):
        """Find languages that contain some number of vowels or consonants "
"with a given criteria."""
        self.welcome['text']=''
        self.clear_home_board()
        self.one = Label(text ='Find langauges that',bg='white')
        self.one.grid(row = 0,column=0,pady = 10)
        self.things.append(self.one)
        
        self.contain = StringVar(self.master)
        self.contain.set('do contain')
        self.contain_menu = OptionMenu(self.master,self.contain,
                                       'do contain','do not contain')
        self.contain_menu.grid(row = 0,column = 1,pady=10)
        self.things.append(self.contain_menu)

        self.any = StringVar(self.master)
        self.any.set('any')
        numbers = ['any','1','2','3','4','5','6','7','8','9','10']
        self.any_menu = OptionMenu(self.master,self.any,
                                       *numbers)
        self.any_menu.grid(row = 0,column = 2,pady=10)
        self.things.append(self.any_menu)

        self.numberof = StringVar(self.master)
        self.numberof.set('number of')
        self.numberof_menu = OptionMenu(self.master,self.numberof,
                                       'number of','or less','or more')
        self.numberof_menu.grid(row = 0,column = 3,pady=10)
        self.things.append(self.numberof_menu)

        self.either = Label(text = 'either vowels with the following criteria:',
                            bg ='white')
        self.either.grid(row = 1,column =0,columnspan = 5,pady=10)
        self.things.append(self.either)

        vlength = ['-any length-','overshort','short','long']
        vmod = ['-any modifier-','no modifier','fricative','retroflexed',
                'pharyngealized','laryngealized','nasalized']
        vvoi = ['-any voicing','breathy voicing',"'normal' voicing",
                'voiceless']
        vheight = ['-any height-','high','lowered high','higher mid','mid',
                   'lower mid','raised low','low']
        vback = ['-any backness-','front','retracted front','central',
                 'fronted back','back']
        vround = ['-any rounding-','unrounded','rounded']
        vvowel = ['-any vowel-','Monophthong','Diphthong']

        #
        self.vowel_length = StringVar(self.master)
        self.vowel_length.set('-any length-')
        self.vowel_length_menu = OptionMenu(self.master,self.vowel_length,
                                       *vlength)
        self.vowel_length_menu.grid(row = 2,column = 0,padx = 5)
        self.things.append(self.vowel_length_menu)

        self.vowel_mod = StringVar(self.master)
        self.vowel_mod.set('-any modifier-')
        self.vowel_mod_menu = OptionMenu(self.master,self.vowel_mod,
                                       *vmod)
        self.vowel_mod_menu.grid(row = 2,column = 1,padx = 5)
        self.things.append(self.vowel_mod_menu)

        self.vowel_voice = StringVar(self.master)
        self.vowel_voice.set('-any voicing-')
        self.vowel_voice_menu = OptionMenu(self.master,self.vowel_voice,
                                       *vvoi)
        self.vowel_voice_menu.grid(row = 2,column = 2,padx = 5)
        self.things.append(self.vowel_voice_menu)

        self.vowel_height = StringVar(self.master)
        self.vowel_height.set('-any height-')
        self.vowel_height_menu = OptionMenu(self.master,self.vowel_height,
                                       *vheight)
        self.vowel_height_menu.grid(row = 2,column = 3,padx = 5)
        self.things.append(self.vowel_height_menu)

        self.vowel_backness = StringVar(self.master)
        self.vowel_backness.set('-any backness-')
        self.vowel_backness_menu = OptionMenu(self.master,
                    self.vowel_backness,*vback)
        self.vowel_backness_menu.grid(row = 2,column = 4,padx = 5)
        self.things.append(self.vowel_backness_menu)

        self.vowel_rounding = StringVar(self.master)
        self.vowel_rounding.set('-any rounding-')
        self.vowel_rounding_menu = OptionMenu(self.master,
                            self.vowel_rounding,*vround)
        self.vowel_rounding_menu.grid(row = 3,column = 0,padx=5)
        self.things.append(self.vowel_rounding_menu)

        self.vowel_type = StringVar(self.master)
        self.vowel_type.set('-any vowel-')
        self.vowel_type_menu = OptionMenu(self.master,self.vowel_type,
                                       *vvowel)
        self.vowel_type_menu.grid(row = 3,column = 1,padx = 5)
        self.things.append(self.vowel_type_menu)

        #

        self.orl = Label(text = 'or consonants with the following criteria:',
                         bg = 'white')
        self.orl.grid(row = 4,column = 0, columnspan = 5, pady=10)
        self.things.append(self.orl)

        clength = ['-any length-','short','long']
        cvoi = ['-any voicing-','voiced','voiceless']
        casp = ['-any aspiration, etc.','no aspiration, etc.','aspirated',
                'preaspirated','prestopped','prenasalized','breathy']
        cart = ['-any sec. articulation-','no sec. articulation',
                'labialized','palatalized','velarized','pharyngelaized',
                'laryngealized','nasalized']
        cplace = ['-any place-','bilabial','labiodental','dental',
                  'dental/alveolar','alveolar','palato-alveolar','retroflex',
                  'palatal','labial-palatal','velar','velar-alveolar',
                  'labial-velar','uvular','pharyngeal','glottal']
        cmod = ['-any modifier-','no modifier','sibilant','lateral']
        cmanner = ['-any manner-','click','affricated click',
                   'velar-fricated click','ejective stop',
                   'ejective fricative','ejective affricate','implosive',
                   'plosive','tap/flap','(affricated) trill','nasal',
                   'affricate','fricative','r-sound','approximant']
        crelease = ['-any release-','no release modifier','any release modifier',
                    'with breathy/fricative release','laterally released',
                    'nasally released']

        #
        self.c_length = StringVar(self.master)
        self.c_length.set('-any length-')
        self.c_length_menu = OptionMenu(self.master,self.c_length,
                                       *clength)
        self.c_length_menu.grid(row = 5,column = 0,padx = 5)
        self.things.append(self.c_length_menu)

        self.c_voice = StringVar(self.master)
        self.c_voice.set('-any voicing-')
        self.c_voice_menu = OptionMenu(self.master,self.c_voice,
                                       *cvoi)
        self.c_voice_menu.grid(row = 5,column = 1,padx = 5)
        self.things.append(self.c_voice_menu)

        self.casp = StringVar(self.master)
        self.casp.set('-any aspiration, etc.-')
        self.casp_menu = OptionMenu(self.master,self.casp,
                                       *casp)
        self.casp_menu.grid(row = 5,column = 2,padx = 5)
        self.things.append(self.casp_menu)

        self.cart = StringVar(self.master)
        self.cart.set('-any sec. articulation-')
        self.cart_menu = OptionMenu(self.master,self.cart,
                                       *cart)
        self.cart_menu.grid(row = 5,column = 3,padx = 5)
        self.things.append(self.cart_menu)

        self.c_place = StringVar(self.master)
        self.c_place.set('-any place-')
        self.c_place_menu = OptionMenu(self.master,self.c_place,
                                       *cplace)
        self.c_place_menu.grid(row = 5,column = 4,padx = 5)
        self.things.append(self.c_place_menu)

        self.c_mod = StringVar(self.master)
        self.c_mod.set('-any modifier-')
        self.c_mod_menu = OptionMenu(self.master,self.c_mod,
                                       *cmod)
        self.c_mod_menu.grid(row = 6,column = 0,padx = 5)
        self.things.append(self.c_mod_menu)

        self.c_manner = StringVar(self.master)
        self.c_manner.set('-any manner-')
        self.c_manner_menu = OptionMenu(self.master,self.c_manner,
                                       *cmanner)
        self.c_manner_menu.grid(row = 6,column = 1,padx = 5)
        self.things.append(self.c_manner_menu)

        self.c_release = StringVar(self.master)
        self.c_release.set('-any release-')
        self.c_release_menu = OptionMenu(self.master,self.c_release,
                                       *cmanner)
        self.c_release_menu.grid(row = 6,column = 2,padx = 5)
        self.things.append(self.c_release_menu)

        self.go_button = Button(text = 'Find sounds and languages',
                                bg = 'springgreen2',
                                command = partial(
                                self.find_languages,event))
        self.go_button.grid(row = 7,column = 0,columnspan = 5,
                            pady = 20)
        self.things.append(self.go_button)

    def find_languages(self,event):
        for widget in self.things:
            widget.grid_forget()

        v_or_c = None # 0 for vowel, 1 for consonant
        
        contain = self.contain.get()
        anything = self.any.get()
        numberof = self.numberof.get()
        
        vlength = self.vowel_length.get()
        vmod = self.vowel_mod.get()
        vvoi = self.vowel_voice.get()
        vheight = self.vowel_height.get()
        vback = self.vowel_backness.get()
        vrnd = self.vowel_rounding.get()
        vtype = self.vowel_type.get()

        vowel_attributes = [vlength,vmod,vvoi,vheight,vback,vrnd,vtype]

        clength = self.c_length.get()
        cvoi = self.c_voice.get()
        casp = self.casp.get()
        cart = self.cart.get()
        cplace = self.c_place.get()
        cmod = self.c_mod.get()
        cman = self.c_manner.get()
        crel = self.c_release.get()

        consonant_attributes = [clength,cvoi,casp,cart,cplace,cmod,cman,
                                crel]

        if contain == 'do contain':
            contain  = 0
        else:
            contain = 1
        if anything == 'any':
            anything = 0
        else:
            anything = int(anything)
        if numberof == 'number of':
            numberof = 0
        elif numberof == 'or less':
            numberof = 1
        else:
            numberof = 2
            
        self.languages_to_print = []
        self.inventories_to_print = []

        print(consonant_attributes)
        
        if vowel_attributes == ['-any length-', '-any modifier-',
            '-any voicing-','-any height-', '-any backness-',
            '-any rounding-','-any vowel-']:
            for i in range(0, len(dictionaries)):
                count = 0
                segment_inventory = []
                for segment in dictionaries[i]:
                    if (segment in features[clength] and
                        segment in features[cvoi] and
                        segment in features[casp] and
                        segment in features[cart] and
                        segment in features[cplace] and
                        segment in features[cmod] and
                        segment in features[cman] and
                        segment in features[crel]):
                        segment_inventory.append(segment)
                        count+=1
                if ((contain == 0 and ((numberof == 2 and count >= anything)
                    or (numberof == 1 and count <= anything) or
                    (numberof == 0 and count == anything))) or
                    
                    (contain == 1 and ((numberof == 0 and count != anything)
                    or (numberof == 1 and count > anything) or
                    (numberof == 2 and count < anything))) or

                    (contain == 0 and anything == 0 and count >0) or
                    (contain == 1 and anything == 0 and count == 0)) :
                    self.languages_to_print.append(self.list[i])
                    self.inventories_to_print.append(segment_inventory)
            
        elif consonant_attributes == ['-any length-',
            '-any voicing-', '-any aspiration, etc.-',
            '-any sec. articulation-', '-any place-', '-any modifier-',
            '-any manner-', '-any release-']:
            for i in range(0, len(dictionaries)):
                count = 0
                segment_inventory = []
                for segment in dictionaries[i]:
                    if (segment in features[vlength] and
                        segment in features[vmod] and
                        segment in features[vvoi] and
                        segment in features[vheight] and
                        segment in features[vback] and
                        segment in features[vrnd] and
                        segment in features[vtype]):
                        segment_inventory.append(segment)
                        count+=1
                if ((contain == 0 and ((numberof == 2 and count >= anything)
                    or (numberof == 1 and count <= anything) or
                    (numberof == 0 and count == anything))) or
                    (contain == 1 and ((numberof == 0 and count != anything)
                    or (numberof == 1 and count > anything) or
                    (numberof == 2 and count < anything))))or 1==1:
                    self.languages_to_print.append(self.list[i])
                    self.inventories_to_print.append(segment_inventory)
        else:
            self.bad_value = Label(text =
                'You can compare vowels or consonants, but not both at the same time :(',
                bg = 'white')
            self.bad_value.grid(row = 0, column = 0)
            self.things.append(self.bad_value)
            self.home_button.grid(row = 1,column = 0)
        if len(self.languages_to_print)>0 and contain == 0:
            self.welcome['text'] ='These sounds occur in the following languages:'                                   
            a = Label(text = 'Language (# sounds):',bg='white')
            b = Label(text = 'Sound:',bg='white')
            c = Label(text = '% of sounds in langauge',bg = 'white')
            a.grid(row = 1,column = 0, pady=15)
            b.grid(row = 1,column = 1, pady=15)
            c.grid(row = 1,column = 2, pady=15)
            self.things.append(a)
            self.things.append(b)
            self.things.append(c)
            rowcount = 2
            for i in range(0,len(self.languages_to_print)):
                # 1st col language
                x  = Label(text = self.langs_with_counts[
                    self.list.index(self.languages_to_print[i])],
                           bg = 'white')
                x.grid(row = rowcount, column = 0,padx=10)
                # 2nd col segments
                y  = Label(text = self.inventories_to_print[i],bg='white')
                y.grid(row = rowcount, column = 1,padx=10)
                self.things.append(x)
                # 3rd col percentages
                z = Label(text = str(len(
                    self.inventories_to_print[i])/len(dictionaries[
                        self.list.index(
                        self.languages_to_print[i])])*100)+'%',
                          bg = 'white')
                z.grid(row = rowcount, column = 2,padx = 10)
                self.things.append(x)
                self.things.append(y)
                self.things.append(z)
                rowcount +=1
            
            self.home_button.grid(row=2,column = 3,rowspan = 2,padx = 20)
            self.home_button.bind('<Button-1>',self.home)
        elif len(self.languages_to_print)>0 and contain == 1:
            self.welcome['text'] ='These sounds do not occur in the following languages:'                                   
            rowcount = 1
            for language in self.languages_to_print:
                x  = Label(text = self.langs_with_counts[
                    self.list.index(language)],bg = 'white')
                x.grid(row = rowcount, column = 0)
                self.things.append(x)
                rowcount +=1
            self.home_button.grid(row=rowcount,column = 0)
            self.home_button.bind('<Button-1>',self.home)
                        
            
    def compare (self,event):
        """Find the sounds that two langauges or the languages in a class"
"share."""
        pad  = 15
        self.clear_home_board()
        self.welcome['text'] = ("Compare the sound inventory of two "
                                "languages or a whole language class.")

        self.space = Label(bg= 'white')
        self.space.grid(row = 1,column = 0, columnspan=2,
                                padx = pad,pady=pad)

        self.two_lang = Label(text = 'Compare two langauges:',bg = 'white')
        self.two_lang.grid(row = 2, column = 0,
                                padx = pad,pady=pad)
        
        self.lang1 = Label(text = 'Language 1 (# of segments): ',bg = 'white')
        self.lang1.grid(row = 3,column = 0,
                                padx = pad,pady=pad)

        self.lang1var = StringVar(self.master)
        self.lang1var.set('--Please Select--')
        self.lang1menu = OptionMenu(self.master, self.lang1var,
                                    *self.langs_with_counts)
        self.lang1menu.grid(row = 3,column = 1,
                                padx = pad,pady=pad)

        self.lang2 = Label(text = 'Language 2 (# of segments): ',bg = 'white')
        self.lang2.grid(row = 4,column = 0,
                                padx = pad,pady=pad)

        self.lang2var = StringVar(self.master)
        self.lang2var.set('--Please Select--')
        self.lang2menu = OptionMenu(self.master,self.lang2var,
                                    *self.langs_with_counts)
        self.lang2menu.grid(row = 4,column = 1,
                                padx = pad,pady=pad)
       
        self.space2 = Label(bg= 'white')
        self.space.grid(row = 5,column = 0, columnspan=2,
                                padx = pad,pady=pad)

        self.classcomp = Label(text = 'Compare languages within a class:',
                               bg = 'white')
        self.classcomp.grid(row = 5, column = 0,
                                padx = pad,pady=pad)

        self.classes = Label(text = 'Language class (# of languages):',
                             bg = 'white')
        self.classes.grid(row = 6, column = 0,
                                padx = pad,pady=pad)
        
        self.classvar = StringVar(self.master)
        self.classvar.set("--Please Select--") # default value
        self.class_compare = OptionMenu(self.master, self.classvar,
                        "Artistic (19)","Engineered (7)",
                        "Auxiliary Language (5)")
        self.class_compare.grid(row = 6, column = 1,
                                padx = pad,pady=pad)

        self.go_button = Button(text = 'Go',bg = 'springgreen2',
                                command= self.compare_options)
        self.go_button.grid(row = 7,column = 1,padx=pad,pady=pad)

        self.compare_menu = [self.space,self.two_lang,self.lang1,
                             self.lang2,self.lang1menu,
                             self.lang2menu,self.space2,self.classcomp,
                             self.classes,self.class_compare,
                             self.go_button]
        self.home_button.bind('<Button-1>',self.remove_compare_menu)
        self.home_button.grid(row = 8, column = 0,columnspan=2,padx = pad,
                              pady=pad)


    def remove_compare_menu(self,event):
        for widget in self.compare_menu:
            widget.grid_forget()
        self.home(event)

    def compare_options(self):
        master_inventory = []
        if self.classvar.get() =='--Please Select--':
            if self.lang1var.get()=='--Please Select--' or self.lang2var.get()=='--Please Select--':
                master_inventory = [[],[]]
            else:
                first = languages[self.langs_with_counts.index(self.lang1var.get())]
                second = languages[self.langs_with_counts.index(self.lang2var.get())]
                self.welcome['text']=first+" and "+second+" share the following segments:"
                master_inventory.append(dictionaries[languages.index(first)])
                master_inventory.append(dictionaries[languages.index(second)])
        else:
            third = self.classvar.get()[:2].lower()
            if third == 'ar':
                third = 'artistic'
            elif third == 'en':
                third = 'engineered'
            else:
                third = 'auxiliary language'
            self.welcome['text'] = "The class '"+third+"' shares the following segments:"
            for lang in classes[third.lower()]:
                master_inventory.append(
                    dictionaries[languages.index(lang)])
        for widget in self.compare_menu:
            widget.grid_forget()

        self.commons = Label(text = ' '.join(
            self.common_elements(master_inventory)),bg = 'white')
        self.commons.grid(row = 1,column = 0,columnspan=2)            
            
        self.home_button.bind('<Button-1>',self.remove_comparison)
        self.home_button.grid(row = 2, column = 0,columnspan = 2)

    def remove_comparison(self,event):
        self.commons.destroy()
        self.home(event)

    def common_elements(self,lists):
        return(set(lists[0]).intersection(*lists[1:]))        

    def home (self, event):
        for widget in self.winfo_children():
            widget.grid_forget()

        for widget in self.things:
            widget.grid_forget()
        self.grid(row = 0)
        self.welcome['text'] = ("This is the interface "
                                 "to the conlang UPSID analog.")
        self.welcome.grid(row = 0, column = 0, columnspan = 2)
        self.question.grid(row = 1, column = 0,pady = 5, sticky = W)
        self.ask_info.grid(row = 2, column = 1,pady=5, sticky=W)
        self.sort_sound.grid(row = 3, column =1,pady=5, sticky=W)
        self.sort_freq.grid(row = 4, column = 1,pady=5, sticky=W)
        self.ask_class.grid(row = 5, column = 1,pady=5, sticky=W)
        self.ask_find.grid(row = 6, column = 1,pady=5, sticky=W)
        self.ask_compare.grid(row = 7, column = 1,pady=5, sticky=W)
        self.home_button.grid_forget()

    def clear_home_board (self):
        self.question.grid_forget()
        self.ask_info.grid_forget()
        self.sort_sound.grid_forget()
        self.sort_freq.grid_forget()
        self.ask_class.grid_forget()
        self.ask_find.grid_forget()
        self.ask_compare.grid_forget()
  
root = Tk()
cuter = font.Font(family="Arial",size=14,weight="normal")
root.option_add("*Font", cuter)
app = App(master = root)
app.mainloop()
