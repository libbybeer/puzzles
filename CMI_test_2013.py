execfile('caesar.py')

Q1 = ["GIDEON","JOE","DREW","BEN","TYSON","MARK","GLENN","KURT","CAMERON","BENJAMIN","MATT","GEORGE","ALBERT","PHIL","WILLIAM","TOPHER","JIM","DARYL","RAY","GENE","NEIL","MICHAEL","BRYAN","RICHARD","EPHRAIM","BORIS","DANIEL","ADAM","COOPER","JACK","JEFF","BRUCE","TRENT","ALBERT","STEVIE","HERMAN","BILL","CALEB","EARL","PATRICK","SYLVESTER","COLIN","BURL","DEAN","DAVID","JON","NICK","TIM","SAL","RICHARD","ART","CHARLES","DALE","REX","JAN"]

Q1_ans = ["ALICE","AVERAGE","BARRYMORE","BIG","BISON","CAIN","CLOSE","","DIAZ","DORCAS","ELEVENTH","ELIOT","FAT","","FIRST","GOPHER","","HANNAH","HOPE","","","LEARNED","LION","LITTLE","LIZA","LORIS","MARTHA","MILLY","MINI","MISSISSIPPI","MISSOURI","MOOSE","NEW JERSEY","NEW YORK","NICKS","PEEWEE","RIGHTS","RUTH","SANDWICH","SECOND","SEVENTH","SIXTH","","STUDENTS","TENTH","THIRD","TICK","TICK","TINY","UTAH","VIRGINIA","WAR","WEST VIRGINIA","WHALE","",""]


# [len([x for x in Q1 if scrabscr(x)==i]) for i in xrange(20)]

Q2 = ["122453242","50220704","14142",
"104","57322641","213131221",
"31181","6629","25267",
"3111011","31118","66",
"06410","54420","2216921334",
"31110","60151112","69133",
"22232614","375514526","35161125919",
"21635","151142535","15476343",
"792","18851","21441433",
"1418","0938","121323",
"4875","121121322","3133118135",
"1019115610712","10111110","531442",
"41557","414334","435323344",
"99768","32023544","194410554",
"479","36477","113111",
"313334","3326201","8261481213",
"12112612925","6157703","6749",
"87224","52290018","54312",
"22172","547261035","161912033",
"2978","473757","478411",
"193","3215121119121322","1221913","77"]

Q3 = ["1111","ADDITION","ARIA","ATLANTA","BRFXXCCXXMNPCCCCLLLMMNPRXVCLMNCKSSQLBB11116","CBS","CIDER","CONTROVERSY","CUMMINGS","CURSEWORD","DAYS","DEFEATED","DINO","DO","DOCTOROW","EMMENTALER","ENCORE","EXCALIBUR","FA","FAIR","FLAMINGO","FORCE","FRO","FROST","GAUSS","HURRICANE","HUTTON","IT","LEG","LET","LOUD","MARSHALL","MEDIATES","MILESTONE","MIRAGE","NEEDLE","ORAL","PARIS","PHENYLALANINE","PI","POTATO","PROVIDENCE","ROUND","ROUSE","SISTER","THURSDAY","TIER","TOKEN","TOY","TROPICANA","VENETIAN","VOLUTE","WHITE","YELLOW","YOUNG"]

Q7 = ["ACRED","SQUAD","COMET","FILED","GOING","CARET"]

Q8a = ["KID","MAT","MOP","MUD","RAT","RUM","SET","PAW"]

Q8c = ["AFT","AND","ANT","MAN","ORE","ROE","SON","TON","USH","YES","THE"]

Q10a = ["HYBRID","HIATUS","PRISON","ISLAND","VIVACE"]

Q10d = ["JETS","FEED","SELFISH"]

Q12 = ["BLUBBER","BLUSTER","BUTTER","FEATHER","FLOWER","JITTER","RUBBER","SILVER","WATER","WINTER"]

Q16b = ["ARSINE","BIKER","CENTS","CLASS","COMET","COMING","DEAL","DEVIL","ETHER","EXITED","GARAGE","GET","HERS","LAY","MOAN","OVINE","PER","REUSE","STALEMATE","TIMER","WAITS"]

Q16d = ["ARABLE","BALD","BRUSH","BURP","CAPON","CHEST","DEFTER","DIREST","INVENT","LOOS","ORANG","PERT","PRONE","PROSE","RED","REED","REVERS","SCAR","SEARING","SERGE","SORES","STAKED","SUBTLE","TABS","TARTAN","THAT","UNDER","WRING"]

Q16e = ["BUTS","FOOT","HAIR","MATS","PEN","WEIR"]

Q17 = ["BONSAI","SOCIAL","ZODIAC","JIGSAW","THIRST","ENDEAR"]

Q18b = ["ALI","BARB","BRIDGET","BUD","DAN","DON","ELLE","ELMO","GARY","HART","KEN","LIN","LIZ","PIA","ROB","SAM","STAN","TED","TONI","VICTOR","WANDA","ZAK"]


Q2_scrab_poss = [x for x in Q2 if "6" not in x and "7" not in x and "9" not in x and "20" not in x]

Q2_phone_poss = [x for x in Q2 if "0" not in x and "1" not in x]

Q2_scrab_used = ["31181","3111011","31118","31110","1418","10111110","113111"]

Q2_scrab_comp = [w for w in Q2_scrab_poss if w not in Q2_scrab_used]



states_first_last = ["DE","PA","NY","GA","CT","MS","MD","SA","NE","VA","NY","NA","RD","VT","KY","TE","OO","LA","IA","MI","IS","AA","ME","MI","AS","MN","FA","TS","IA","WN","CA","MA","ON","KS","WA","NA","NA","CO","NA","SA","MA","WN","IO","WG","UH","OA","NO","AA","AA","HI"]

states_abbrev = ["DE","PA","NJ","GA","CT","MA","MD","SC","NH","VA","NY","NC","RI","VT","KY","TN","OH","LA","IN","MS","IL","AL","ME","MO","AR","MI","FL","TX","IA","WI","CA","MN","OR","KS","WV","NV","NE","CO","ND","SD","MT","WA","ID","WY","UT","OK","NM","AZ","AK","HI"]

states_names = ["Delaware","Pennsylvania","New Jersey","Georgia","Connecticut","Massachusetts","Maryland","South Carolina","New Hampshire","Virginia","New York","North Carolina","Rhode Island","Vermont","Kentucky","Tennessee","Ohio","Louisiana","Indiana","Mississippi","Illinois","Alabama","Maine","Missouri","Arkansas","Michigan","Florida","Texas","Iowa","Wisconsin","California","Minnesota","Oregon","Kansas","West Virginia","Nevada","Nebraska","Colorado","North Dakota","South Dakota","Montana","Washington","Idaho","Wyoming","Utah","Oklahoma","New Mexico","Arizona","Alaska","Hawaii"]


element_abbrevs = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Uut","Fl","Uup","Lv","Uus","Uuo"]


eldi = {}
for i in range(1,119):
    eldi[i] = element_abbrevs[i-1]

#idle = {}
#for i in range(1,119):
#    idle[str(i)[-1::-1]]=element_abbrevs[i-1][-1::-1]



#dict_build_anyscores("3326201",eldi)
    
def dict_revrev_anyscores(x,d,look=True):
    xr = x[-1::-1]
    parses = parse12_fromlist(xr,d.keys())
    pws = []
    print parses
    for p in parses:
        pws = make_check_trans_from_list(p,rev_each(d))
    pws = sorted(list(set(rev_each(pws))))
    if look:
        return [p for p in pws if dict_lookup(p)]
    return pws


Q25 = [(3,1,1),(5,2,2),(1,5,2),(1,5,1),(1,5,4),(1,1,1),(5,1,3),(6,6,2),
       (5,1,2),(7,1,2),(8,6,1),(2,1,2),(1,5,3),(5,7,2),(5,3,3),(7,3,4),
       (1,5,5),(7,6,2),(7,7,1),(2,7,2),(5,7,6),(1,1,3),(1,1,6),(5,4,3),
       (2,3,6),(2,3,1),(2,3,2),(8,5,1),(7,6,1),(1,3,4),(1,3,3),(1,4,3),
       (3,2,1),(3,4,4),(5,3,4),(3,3,2),(7,3,3),(1,1,4)]

Q1_cats = [["GIDEON","BENJAMIN","EPHRAIM","DANIEL","ADAM","CALEB","FRANK"],
           ["JOE","BEN","ALBERT","RICHARD","COOPER","HERMAN","TIM"],
           ["DREW","GLENN","CAMERON","GEORGE","DARYL","MICHAEL","STEVIE"],
           ["TYSON","TOPHER","BRYAN","BORIS","BRUCE","NICK","DALE"],
           ["MARK","","","","","",""],
           ["KURT","","","","","",""],
           ["MATT","WILLIAM","PATRICK","SYLVESTER","COLIN","DAVID","JON"],
           ["JACK","JEFF","TRENT","AL","SAL","RICH","CHARLES"]]

Q1_ans_cats = [["ALICE","DORCAS","LIZA","MARTHA","MILLY","RUTH","SARAH"],
               ["AVERAGE","BIG","FAT","LITTLE","MINI","PEEWEE","TINY"],
               ["BARRYMORE","CLOSE","DIAZ","ELIOT","HANNAH","LEARNED","NICKS"],
               ["BISON","GOPHER","LION","LORIS","MOOSE","TICK","WHALE"],
               ["CAIN","","","","","",""],
               ["","","","","","",""],
               ["ELEVENTH","FIRST","SECOND","SEVENTH","SIXTH","TENTH","THIRD"],
               ["MISSISSIPPI","MISSOURI","NEW JERSEY","NEW YORK","UTAH",
                "VIRGINIA","WEST VIRGINIA"]]

def try_q25(seq=[0,1,2,3,4,5,6]):
    ret = ""
    for trip in Q25:
        if len(Q1_ans_cats[trip[0]])<trip[1]-1:
            return "sorry"
        if len(Q1_ans_cats[trip[0]][trip[1]])<trip[2]-1:
            return "still sorry"
        ret += Q1_ans_cats[trip[0]][trip[1]][trip[2]]
    return ret

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def try_q25s():
    failed = 0
    for p in all_perms(range(len(Q1_cats))):
        a = try_q25(p)
        if "sorry" not in a:
            print [p,a]
        else:
            failed += 1
    print "Failed: "+ str(failed)

Q2_ans_cats = [["CHESHIRE","PEPPERJACK","EDAM","GRUYERE",
                "SBRINZ","ROQUEFORT","BRIE",""],
               ['CHILI','BISQUE','STEW','CHOWDER',
                'SOUP','RAGOUT','GUMBO',''],
               ['DIX','CINQ','ZEHN','TRES',
                'UNO','QUATRE','ZWEI',''],
               ['GALENA','BORAX','OZONE','ETHANOL',
                'WATER','ACETYLENE','AMMONIA',''],
               ['RACCOON','LYNX','BAT','PLATYPUS',
                'WOLF','KANGAROO','WOMBAT',''],
               ['RUBY','QUARTZ','ONYX','GARNET',
                'OPAL','AGATE','MOONSTONE',''],
               ['SAMSON','SAMSON','SAMSON','SAMSON',
                'SAMSON','SAMSON','SAMSON',''],
               ['TRIANGLE','BANJO','XYLOPHONE','TRUMPET',
                'HARP','BALALAIKA','BASSOON','']]
