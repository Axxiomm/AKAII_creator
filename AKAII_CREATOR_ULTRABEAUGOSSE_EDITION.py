#   ___   _        _____
#  / __\ /_\  _ __|___  |
# / /   //_\\| '_ \  / /
#/ /___/  _  \ | | |/ /
#\____/\_/ \_/_| |_/_/
#



from tkinter import *
from tkinter import ttk

global L
global C

def apc_mini():
    global L
    global C
    L=8
    C=8
    fenetre_choix.destroy()

def apc_40():
    global L
    global C
    L=5
    C=8
    fenetre_choix.destroy()

fenetre_choix = Tk()

fenetre_choix.title('CHOIX MODELE AKAI')
B_mini = Button(fenetre_choix, text="APC MINI",height= 7, width=15, command=apc_mini)
B_mini.grid(row=0,column=0,padx=5,pady=14)
B_40 = Button(fenetre_choix, text="APC 40",height= 7, width=15, command=apc_40)
B_40.grid(row=0,column=1,padx=5,pady=14)
fenetre_choix.mainloop()




global color_in_use
global color_in_use_tk
global grp_in_use
global btn
global liste_finale
global B_grp
global B_color
global page
global edit
global change_colonne
global change_ligne
global change_tout
global pageencour
global listeCombo
global blink_mode
global blink_white #=0 si clignotage noir et =1 si blanc, vaut 0 de base

blink_white =0
pageencour = 1
change_ligne = 0
change_colonne = 0
change_tout = 0
edit='grp'


btn = []
color_in_use = "white"
grp_in_use = 0
blink_mode=10

global liste_finale
liste_finale = []
for ligne in range(L):
    sous_btn = []
    for colonne in range(C):
        sous_btn.append(['-1','black','white','5']) #grp, color, color_blink,blinkmodeon
    liste_finale.append(sous_btn)

def copy(inputString):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(inputString)
    r.destroy()

def change(m):
    global edit
    global change_colonne
    global change_ligne
    global change_tout

    if change_colonne == 0 and change_ligne == 0 and change_tout == 0:
        if edit == 'grp':grp_change(m)
        elif edit == 'color':color_change(m)

    else:

        if change_colonne == 1:
            if edit == 'grp':
                for i in range(L):
                    grp_change((i,m[1]))
            if edit == 'color':
                for i in range(L):
                    color_change((i,m[1]))

        if change_ligne == 1:
            if edit == 'grp':
                for i in range(C):
                    grp_change((m[0],i))
            if edit == 'color':
                for i in range(C):
                    color_change((m[0],i))

        if change_tout == 1:
            if edit == 'grp':
                for i in range(L):
                    for j in range(C):
                        grp_change((i,j))
            if edit == 'color':
                for i in range(L):
                    for j in range(C):
                        color_change((i,j))

def reverse_blinkcolor():
    global liste_finale
    global blink_white
    global B_change_blink_color
    global btn

    if blink_white:
        blink_white = 0
    else:
        blink_white = 1

    for ligne in range(L):
        for colonne in range(C):
            if liste_finale[ligne][colonne][1]!='black' and liste_finale[ligne][colonne][1]!='white':
                if liste_finale[ligne][colonne][2]=='black':
                    liste_finale[ligne][colonne][2]='white'
                    btn[ligne][colonne].config(fg = 'white')
                else:
                    liste_finale[ligne][colonne][2]='black'
                    btn[ligne][colonne].config(fg = 'black')

    if blink_white:
        B_change_blink_color.config(text = "clignotage en blanc")
    else:
        B_change_blink_color.config(text = "clignotage en noir")

def checkchecked():
    global change_colonne
    global change_ligne
    global change_tout

    change_colonne = checkcolonnevar.get()
    change_ligne = checklignevar.get()
    change_tout = checkallvar.get()

def reset():
    for i in range(L):
        for j in range(C):
            btn[i][j].config(fg = 'white')
            btn[i][j].config(text = '-1')
            btn[i][j].config(bg = 'black')

            liste_finale[i][j][1]='black'
            liste_finale[i][j][2]='white'
            liste_finale[i][j][0]=-1
            liste_finale[i][j][3]=5
    listeCombo.set(liste_blink[5])


def auto_group():
    global liste_finale
    global grp_in_use

    lfm = []

    for ligne in range(L):
        sous_liste = []
        for colonne in range(C):
            sous_liste.append([liste_finale[ligne][colonne][1],0]) #color, grp
        lfm.append(sous_liste)

    current_grp=1

    for ligne in range(L):
        for colonne in range(C):
            if lfm[ligne][colonne][1]==0:
                to_test = [(ligne,colonne)]

                for e in to_test:
                        l=e[0]
                        c=e[1]

                        if l!=0 and l!=L-1:
                            if lfm[l][c][0]==lfm[l+1][c][0] and (l+1,c) not in to_test:
                                lfm[l][c][1]=lfm[l+1][c][1]
                                to_test.append((l+1,c))
                            if lfm[l][c][0]==lfm[l-1][c][0] and (l-1,c) not in to_test:
                                lfm[l][c][1]=lfm[l-1][c][1]
                                to_test.append((l-1,c))
                        if l==0:
                            if lfm[l][c][0]==lfm[l+1][c][0] and (l+1,c) not in to_test:
                                lfm[l][c][1]=lfm[l+1][c][1]
                                to_test.append((l+1,c))
                        if l==4:
                            if lfm[l][c][0]==lfm[l-1][c][0] and (l-1,c) not in to_test:
                                lfm[l][c][1]=lfm[l-1][c][1]
                                to_test.append((l-1,c))

                        if c!=0 and c!=C-1:
                            if lfm[l][c][0]==lfm[l][c+1][0] and (l,c+1) not in to_test:
                                lfm[l][c][1]=lfm[l][c+1][1]
                                to_test.append((l,c+1))
                            if lfm[l][c][0]==lfm[l][c-1][0] and (l,c-1) not in to_test:
                                lfm[l][c][1]=lfm[l][c-1][1]
                                to_test.append((l,c-1))
                        if c==0:
                            if lfm[l][c][0]==lfm[l][c+1][0] and (l,c+1) not in to_test:
                                lfm[l][c][1]=lfm[l][c+1][1]
                                to_test.append((l,c+1))
                        if c==7:
                            if lfm[l][c][0]==lfm[l][c-1][0] and (l,c-1) not in to_test:
                                lfm[l][c][1]=lfm[l][c-1][1]
                                to_test.append((l,c-1))
                if lfm[to_test[0][0]][to_test[0][1]][0]=='black':
                    grp_in_use=-1
                else:
                    grp_in_use=current_grp
                    current_grp+=1
                for e in to_test:

                    lfm[e[0]][e[1]][1]=current_grp
                    grp_change(e)








#*******************************************************************
## COLOR
#*******************************************************************

def color(a):
    switcher = {
    1:"white",
    2:"black",
    3:"gray",
    4:"light_gray",
    5:"dim_gray",
    6:"red",
    7:"light_red",
    8:"half_red",
    9:"dim_red",
    10:"half_red2",
    11:"orange",
    12:"light_orange",
    13:"half_light_orange",
    14:"amber",
    15:"half_amber",
    16:"yellow",
    17:"half_yellow",
    18:"dim_yellow",
    19:"dark_yellow",
    20:"light_yellow",
    21:"white_yellow",
    22:"light_green",
    23:"half_light_green",
    24:"dim_light_green",
    25:"bright_light_green",
    26:"green",
    27:"dim_green",
    28:"half_green",
    29:"light_green2",
    30:"white_green",
    31:"water_green",
    32:"bright_water_green",
    33:"light_water_green",
    34:"half_water_green",
    35:"cyan_water_green",
    36:"cyan",
    37:"dark_cyan",
    38:"light_cyan",
    39:"half_cyan",
    40:"dim_cyan",
    41:"blue",
    42:"dim_blue",
    43:"half_blue",
    44:"light_blue",
    45:"purple",
    46:"half_purple",
    47:"dim_purple",
    48:"half_magenta",
    49:"magenta",
    50:"light_magenta",
    51:"pink",
    52:"red_pink",
    53:"dim_pink",
    54:"magenta_pink",
    55:"half_pink",
    56:"light_pink",
        }
    return switcher.get(a, "black")

def color_tk(a):
    switcher = {
    1:"white",
    2:"black",
    3:"gray30",
    4:"gray70",
    5:"gray45",
    6:"red",
    7:"indian red",
    8:"orange red",
    9:"red3",
    10:"tomato",
    11:"orange",
    12:"light salmon",
    13:"sandy brown",
    14:"DarkOrange3",
    15:"dark orange",
    16:"yellow",
    17:"gold",
    18:"light goldenrod",
    19:"goldenrod",
    20:"light goldenrod yellow",
    21:"light yellow",
    22:"lime green",
    23:"spring green",
    24:"pale green",
    25:"medium spring green",
    26:"green4",
    27:"olive drab",
    28:"green yellow",
    29:"yellow green",
    30:"green",
    31:"sea green",
    32:"medium sea green",
    33:"light sea green",
    34:"medium aquamarine",
    35:"aquamarine",
    36:"cyan",
    37:"dark turquoise",
    38:"light cyan",
    39:"pale turquoise",
    40:"cadet blue",
    41:"blue",
    42:"steel blue",
    43:"royal blue",
    44:"deep sky blue",
    45:"purple",
    46:"thistle",
    47:"medium purple",
    48:"violet red",
    49:"magenta",
    50:"dark orchid",
    51:"pink",
    52:"deep pink",
    53:"DeepPink4",
    54:"maroon1",
    55:"pink1",
    56:"hot pink",
        }
    return switcher.get(a, "black")

def table2tk(colortable):
    for i in range(57):
        if color(i)==colortable:
            return color_tk(i)


def color_select(a):
    global color_in_use
    global color_in_use_tk
    global B_color
    global e
    global edit
    edit='color'

    if type(a)==int:

        color_in_use = color(a)
        color_in_use_tk = color_tk(a)

    else:

        color_in_use = e.get()

    B_color.config(text = "couleur = "+color_in_use)



def color_menu():
    global color_in_use
    global e
    global edit
    edit='color'

    fenetre_color = Tk()
    fenetre_color.title('MENU COULEUR')

    Label(fenetre_color, text = "couleur =" ).pack(side='top')
    e = Entry( fenetre_color, bd = 5, textvariable = '' )
    e.pack(side = 'top', padx = 30)

    Button(fenetre_color, borderwidth=1, text = 'Valider', command=lambda : [color_select(''), fenetre_color.destroy()]).pack(side = 'top', padx=5,pady=5)

    fenetre_color.mainloop()

def color_change(m):
    global blink_white
    global btn
    global color_in_use
    global liste_finale

    btn[m[0]][m[1]].config(bg = color_in_use_tk)
    #print(color_in_use)
    liste_finale[m[0]][m[1]][1]=color_in_use

    if blink_white == 0:
        if color_in_use!='black':
            liste_finale[m[0]][m[1]][2]='black'
            btn[m[0]][m[1]].config(fg = 'black')
        else:
            liste_finale[m[0]][m[1]][2]='white'
            btn[m[0]][m[1]].config(fg = 'white')

    if blink_white == 1:
        if color_in_use!='white':
            liste_finale[m[0]][m[1]][2]='white'
            btn[m[0]][m[1]].config(fg = 'white')
        else:
            liste_finale[m[0]][m[1]][2]='black'
            btn[m[0]][m[1]].config(fg = 'black')



#*******************************************************************
## GROUP
#*******************************************************************


def grp_select(a):
    global grp_in_use
    global e_grp
    global B_grp
    global edit
    edit='grp'

    if type(a)==int:

        grp_in_use = int(a)

    else:

        grp_in_use = int(e_grp.get())

    B_grp.config(text = "groupe = "+str(grp_in_use))

def grp_plus_un(event=''):
    global grp_in_use
    global B_grp
    global edit
    edit='grp'

    grp_in_use += 1

    B_grp.config(text = "groupe = "+str(grp_in_use))
def grp_moins_un(event=''):
    global grp_in_use
    global B_grp
    global edit
    edit='grp'

    grp_in_use -= 1

    B_grp.config(text = "groupe = "+str(grp_in_use))


def grp_menu():
    global grp_in_use
    global e_grp
    global edit
    edit='grp'

    fenetre_grp = Tk()
    fenetre_grp.title('MENU GROUPE')

    """for colonne in range(8):
        Button(fenetre_grp,
        borderwidth=1,
        bg='gray',
        text = str(6-colonne),
        height=2,
        width=4,
        command=lambda m=6-colonne: [grp_select(m),fenetre_grp.destroy()]).pack(side = 'right',padx=5,pady=5)"""

    Label(fenetre_grp, text = "groupe =" ).pack(side='top')
    e_grp = Entry( fenetre_grp, bd = 5, textvariable = '' )
    e_grp.pack(side = 'top', padx = 30)

    Button(fenetre_grp, borderwidth=1, text = 'Valider', command=lambda : [grp_select(''), fenetre_grp.destroy()]).pack(side = 'top', padx=5,pady=5)



    fenetre_grp.mainloop()

def grp_change(m):
    global btn
    global grp_in_use
    global liste_finale

    btn[m[0]][m[1]].config(text = str(grp_in_use))
    liste_finale[m[0]][m[1]][0]=int(grp_in_use)

#*******************************************************************
# GENERATION CODE
#*******************************************************************

def change_blink(event):
    global liste_finale
    # Obtenir l'élément sélectionné
    select = listeCombo.get()
    if L == 5:
        switcher = {"off":0, "oneshot 1/24":1, "oneshot 1/16":2, "oneshot 1/8":3, "oneshot 1/4":4,
    "oneshot 1/2":5,"pulsing 1/24":6,"pulsing 1/16":7, "pulsing 1/8":8, "pulsing 1/4":9, "pulsing 1/2":10,"blinking 1/24":11,"blinking 1/16":12,"blinking 1/8":13, "blinking 1/4":14, "blinking 1/2":15}
        switcher.get(select, 10)
        for ligne in range(L):
            for colonne in range(C):
                liste_finale[ligne][colonne][3]=str(switcher.get(select, 10))
    else:

        switcher = {"10%":0, "25%":1, "50%":2, "65%":3, "90%":4,"75%":5,
    "ON":6,"pulsing 1/16":7, "pulsing 1/8":8, "pulsing 1/4":9, "pulsing 1/2":10,"blinking 1/24":11,"blinking 1/16":12,"blinking 1/8":13, "blinking 1/4":14, "blinking 1/2":15,"OFF":16}
        switcher.get(select, 10)
        for ligne in range(L):
            for colonne in range(C):
                liste_finale[ligne][colonne][3]=str(switcher.get(select, 10))

def generation():
    global pageencour
    global page
    global liste_finale
    global blink_mode

    if L==5:#APC 40
        pageencour = page.get()

        if pageencour=='' or not(pageencour.isnumeric()):
            erreur_page = Tk()
            erreur_page.title('ERREUR')
            erreur_page.geometry("400x50")
            erreur_page.configure(bg='yellow')
            Label(erreur_page, text = "ERREUR | PAS DE PAGE SELECTIONNÉE", bg='yellow' ).place(relx=0.5, rely=0.5, anchor=CENTER)
            erreur_page.mainloop()

        else:
            strfinal ="""local button = {};button[1] = {};button[2] = {};button[3] = {};button[4] = {};button[5] = {};
            """



            for ligne in range(1,6):
                for colonne in range(1,9):
                    sousstr = """button["""+str(ligne)+"""]["""+str(colonne)+"""] = {['grp'] = """+str(liste_finale[ligne-1][colonne-1][0])+""", ['cON1'] = '"""+liste_finale[ligne-1][colonne-1][1]+"""', ['cON2'] = '"""+liste_finale[ligne-1][colonne-1][2]+"""', ['mON'] = """+liste_finale[ligne-1][colonne-1][3]+""", ['cOFF1'] = '"""+liste_finale[ligne-1][colonne-1][1]+"""', ['cOFF2'] = 'black', ['mOFF'] = 0}; \n"""

                    strfinal+=sousstr


            return strfinal + """Buttons_Conf["""+str(pageencour)+"""] = button;"""


    if L==8:#APC mini

            strfinal ="""Buttons_Conf = {};
    Buttons_Conf[1] = {};
    Buttons_Conf[2] = {};
    Buttons_Conf[3] = {};
    Buttons_Conf[4] = {};
    Buttons_Conf[5] = {};
    Buttons_Conf[6] = {};
    Buttons_Conf[7] = {};
    Buttons_Conf[8] = {};"""



            for ligne in range(1,9):
                for colonne in range(1,9):
                    sousstr = """Buttons_Conf["""+str(ligne)+"""]["""+str(colonne)+"""] = {['grp'] = """+str(liste_finale[ligne-1][colonne-1][0])+""", ['cON1'] = '"""+liste_finale[ligne-1][colonne-1][1]+"""', ['cON2'] = '"""+liste_finale[ligne-1][colonne-1][2]+"""', ['mON'] = """+liste_finale[ligne-1][colonne-1][3]+""", ['cOFF1'] = '"""+liste_finale[ligne-1][colonne-1][1]+"""', ['cOFF2'] = 'black', ['mOFF'] = 6}; \n"""

                    strfinal+=sousstr


            return strfinal




#*******************************************************************
## LOAD CODE
#*******************************************************************


def load_menu():

    fenetre_load = Tk()
    fenetre_load.title('MENU CHARGER UN CODE')

    Label(fenetre_load, text = "collez votre code ci-dessous" ).pack(side='top')
    l = Entry( fenetre_load, bd = 5, textvariable = '' )
    l.pack(side = 'top', padx = 30)

    Button(fenetre_load, borderwidth=1, text = 'Valider', command=lambda : [load_test(l.get()), fenetre_load.destroy()]).pack(side = 'top', padx=5,pady=5)

    fenetre_load.bind('<Return>', lambda m: [load_test(l.get()),fenetre_load.destroy()])

    fenetre_load.mainloop()



def load_test(code):

    try:
        loader(code)
    except Exception:
        erreur_page2 = Tk()
        erreur_page2.title('ERREUR')
        erreur_page2.geometry("400x50")
        erreur_page2.configure(bg='yellow')
        Label(erreur_page2, text = "ERREUR | CODE INVALIDE\nVERIFIEZ QU'IL N'Y AI PAS DE CODE COMMENTÉ", bg='yellow' ).place(relx=0.5, rely=0.5, anchor=CENTER)

        erreur_page2.mainloop()



def loader(code):
    global page
    global btn
    global liste_finale
    global listeCombo

    a_retirer=['\n',
    " ","={['grp']=","['cON1']=","['cON2']=","['mON']=","localbutton={}","Buttons_Conf[","]=button","'"]+['button['+str(i)+']={};' for i in range(1,9)]+["button[","][","]"]+["Button_Conf[","][","]"]+[str(i)+'={};' for i in range(1,9)]+["Buttons_Conf={}"]

    for e in a_retirer:
        code = code.replace(e,'')

    code_ligne = code.split(';')

    code_ligne = [i for i in code_ligne if i!='']

    code_ligne_decoupe = []
    for e in code_ligne:
        code_ligne_decoupe += e.split(',')

    liste_return = []#recreation de la liste de base, au moins tout est complet
    for ligne in range(L):
        sous_btn = []
        for colonne in range(C):
            sous_btn.append(['-1','white','black','10']) #grp, color, color_blink,blinkmodeon
        liste_return.append(sous_btn)


    #print(code_ligne_decoupe)


    if L==5:#pas de pagind
        page_return=code_ligne_decoupe.pop()
        test = page_return.isnumeric()
        if not(test):
            raise Excpetion

    for i in range(len(code_ligne_decoupe)):
        if i%7 == 0:
            ligne = int(code_ligne_decoupe[i][0])-1
            colonne = int(code_ligne_decoupe[i][1])-1
            liste_return[ligne][colonne][0] = int(code_ligne_decoupe[i][2:])
        if i%7 == 1 or i%7 == 2 or i%7 == 3:
            liste_return[ligne][colonne][i%7]=code_ligne_decoupe[i]

    for i in range(L):
        for j in range(C):
            btn[i][j].config(fg = table2tk(liste_return[i][j][2]))
            btn[i][j].config(text = liste_return[i][j][0])
            btn[i][j].config(bg = table2tk(liste_return[i][j][1]))
            liste_finale[i][j][0]=liste_return[i][j][0]
            liste_finale[i][j][1]=liste_return[i][j][1]
            liste_finale[i][j][2]=liste_return[i][j][2]
            liste_finale[i][j][3]=liste_return[i][j][3]

    listeCombo.set(liste_blink[int(liste_return[0][0][3])])
    if L==5:
        page.delete(0, END)
        page.insert(0, page_return)



#*******************************************************************
## MAIN/INTERFACE
#*******************************************************************


fenetre_main = Tk()
fenetre_main.title('AKAI CREATOR ULTRABEAUGOSSE EDITION')

checkcolonnevar = IntVar()

checklignevar = IntVar()

checkallvar = IntVar()

#AKAII
Frame_akaii = LabelFrame(fenetre_main, text="AKAII", padx=20,pady=20)
Frame_akaii.grid(row=0,column=1,padx=5,pady=5)

for ligne in range(L):
    sous_btn = []
    for colonne in range(1,C+1):
        sous_btn.append(Button(Frame_akaii, borderwidth=1, bg='black' , height=2, width=8, text='-1',fg = 'white',command=lambda m=(ligne,colonne-1): change(m)))
    btn.append(sous_btn)

for ligne in range(L):
    for colonne in range(1,C+1):
        btn[ligne][colonne-1].grid(column=colonne, row = ligne,padx=2,pady=2)


#COLOR
Frame_color = LabelFrame(fenetre_main, text="COULEUR", padx=20,pady=20)
Frame_color.grid(row=1,column=1,padx=5,pady=5)



for k in range(1,57):
        if k<=5:r,c=k-1,1
        if 5<k<=10:r,c=k-6,2
        if 10<k<=15:r,c=k-11,3
        if 15<k<=21:r,c=k-16,4
        if 21<k<=25:r,c=k-22,5
        if 25<k<=30:r,c=k-26,6
        if 30<k<=35:r,c=k-31,7
        if 35<k<=40:r,c=k-36,8
        if 40<k<=44:r,c=k-41,9
        if 44<k<=50:r,c=k-45,10
        if 50<k<=56:r,c=k-51,11
        Button(Frame_color,
        borderwidth=1,
        bg = color_tk(k),
        height=2,
        width=4,
        command=lambda m=k: color_select(m)).grid(row=r+1,column=c,padx=5,pady=5)

B_color = Button(Frame_color, text="couleur = "+str(color_in_use), command=color_menu)
B_color.grid(row=0,column=0,columnspan = 12,padx=5,pady=5)
#

#GROUPE
Frame_grp = LabelFrame(fenetre_main, text="GROUPE", padx=20,pady=20)
Frame_grp.grid(row=0,column=0,padx=5,pady=5)

B_grp = Button(Frame_grp, text="groupe = "+str(grp_in_use), command=grp_menu)
B_grp.grid(row=1,column=0,padx=5,pady=14)
B_grp_plus_1 = Button(Frame_grp, text="groupe+1", command=grp_plus_un)
B_grp_plus_1.grid(row=2,column=0,padx=5,pady=14)
B_grp_moins_1 = Button(Frame_grp, text="groupe-1", command=grp_moins_un)
B_grp_moins_1.grid(row=3,column=0,padx=5,pady=14)
B_grp_reset = Button(Frame_grp, text="groupe reset", command=lambda m=-1: grp_select(m))
B_grp_reset.grid(row=4,column=0,padx=5,pady=14)

fenetre_main.bind('p', grp_plus_un)
fenetre_main.bind('m', grp_moins_un)
#

#MENU RAPIDE
Frame_chk = LabelFrame(fenetre_main, text="MODIFICATION RAPIDE", padx=20,pady=20)
Frame_chk.grid(row=0,column=2,padx=5,pady=5)

checkcolonne = Checkbutton(Frame_chk, text="changer colonne", variable=checkcolonnevar, onvalue=1, offvalue=0, command=checkchecked)
checkcolonne.grid(row=0,column=0,padx=5,pady=14)
checkligne = Checkbutton(Frame_chk, text="changer ligne", variable=checklignevar, onvalue=1, offvalue=0, command=checkchecked)
checkligne.grid(row=1,column=0,padx=5,pady=14)
checkall = Checkbutton(Frame_chk, text="changer tout", variable=checkallvar, onvalue=1, offvalue=0, command=checkchecked)
checkall.grid(row=2,column=0,padx=5,pady=14)

B_auto_group = Button(Frame_chk, text="GROUPE AUTOMATIQUE", command=auto_group)
B_auto_group.grid(row=3,column=0,padx=5,pady=14)
B_reset_all = Button(Frame_chk, text="RESET ALL",bg='red', command=reset)
B_reset_all.grid(row=4,column=0,padx=5,pady=14)
#

#FINAL
Frame_final = LabelFrame(fenetre_main, text="CODE FINAL", padx=20,pady=20)
Frame_final.grid(row=1,column=2,padx=5,pady=5)

B_load = Button(Frame_final, text="charger un code", command=load_menu)
B_load.grid(row=0,column=1,columnspan = 12,padx=5,pady=5)

if L==5:
    Label(Frame_final, text = "N° Page =", bg = "red").grid(row=1,column=0, pady = 0)
    value1 = StringVar()
    value1.set("")
    page = Entry(Frame_final, textvariable=value1, width=10)
    page.grid(row=1,column=1, pady = 10,padx=0)

Label(Frame_final, text = "choix clignotage").grid(row=2,column=0, pady = 10,padx=10)
if L==5:
    liste_blink=["off", "oneshot 1/24", "oneshot 1/16", "oneshot 1/8", "oneshot 1/4",
    "oneshot 1/2","pulsing 1/24","pulsing 1/16", "pulsing 1/8", "pulsing 1/4", "pulsing 1/2","blinking 1/24","blinking 1/16","blinking 1/8", "blinking 1/4", "blinking 1/2"]
if L==8:
    liste_blink=["10%", "25%", "50%","65%", "75%", "90%",
    "ON","pulsing 1/16", "pulsing 1/8", "pulsing 1/4", "pulsing 1/2","blinking 1/24","blinking 1/16","blinking 1/8", "blinking 1/4", "blinking 1/2","OFF"]
listeCombo = ttk.Combobox(Frame_final, values=liste_blink)
listeCombo.current(10)
listeCombo.grid(row=2,column=1, pady = 10)

listeCombo.bind("<<ComboboxSelected>>", change_blink)
if L==5:
    B_change_blink_color = Button(Frame_final, text="clignotage en noir", command=reverse_blinkcolor)
    B_change_blink_color.grid(row=3,column=1, pady = 10)

Button(Frame_final, text="copier code", command=lambda m=colonne: copy(generation())).grid(row=4,column=1, pady = 10)
#



fenetre_main.mainloop()



