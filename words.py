# usr/bin/env python3

import argparse
import re
import string
import textwrap

# This creates the database of words. Must be run before importing nltk.corpus
# import nltk
# nltk.download()
# This creates the word list seen below in the assignment to w5list
# from nltk.corpus import words
# w5list = words.words()
# wlist = [w for w in w5list if re.match(".....$", w) and w.lower() == w]
# s = "w5list = [\n    "
# for i, w in enumerate(wlist):
#     s += f'"{w}",'
#     s += "\n    " if i % 15 == 14 else ""
# s = s.rstrip() + "]"
# with open("words.txt", "w") as f:
#     f.write(s)

# The word list is included here so that this script is self-contained and no dictionary needs to
# be downloaded. The above code was used to create the dictionary below.

# fmt: off
w5list = [
    "aalii","abaca","aback","abaff","abaft","abase","abash","abask","abate","abave","abaze","abbas","abbey","abbot","abdal",
    "abdat","abeam","abear","abele","abhor","abide","abidi","abilo","abkar","abler","ablow","abmho","abnet","abode","abody",
    "abohm","aboil","aboma","aboon","abord","abort","about","above","abret","abrim","abrin","absit","abuna","abura","abuse",
    "abuzz","abwab","abysm","abyss","acana","acapu","acara","acari","acate","accoy","acedy","acerb","achar","acher","achor",
    "acier","acker","ackey","aclys","acmic","acock","acoin","acold","acoma","acone","acorn","acred","acrid","acron","acryl",
    "actin","acton","actor","acute","adage","adapt","adati","adawe","adawn","adays","addax","added","adder","addle","adead",
    "adeem","adeep","adept","adfix","adieu","adion","adjag","adlay","adlet","adman","admit","admix","adnex","adobe","adopt",
    "adore","adorn","adown","adoxy","adoze","adpao","adrip","adrop","adrue","adult","adunc","adusk","adust","adyta","adzer",
    "aegis","aeric","aerie","aevia","aface","afara","afear","affix","afire","aflat","aflow","afoam","afoot","afore","afoul",
    "afret","after","again","agama","agami","agamy","agape","agasp","agate","agaty","agaze","agent","agger","aggry","aggur",
    "agile","aging","agist","aglet","agley","aglow","agnel","agnus","agoge","agoho","agone","agony","agora","agrah","agral",
    "agree","agria","agrin","agrom","agsam","aguey","agush","agust","ahead","aheap","ahind","ahint","ahong","ahsan","ahull",
    "ahunt","ahura","ahush","ahwal","aider","aillt","aimer","ainoi","airan","airer","aisle","aitch","aiwan","aizle","ajaja",
    "ajari","ajava","ajhar","akala","akasa","akebi","akeki","aknee","akpek","akule","akund","alack","alada","alala","alamo",
    "aland","alani","alarm","alary","alate","alban","albee","album","albus","alder","aldim","aldol","aleak","aleft","aleph",
    "alert","alfet","algae","algal","algic","algid","algin","algor","algum","alias","alibi","alien","align","alike","alima",
    "alish","aliso","alisp","alist","alite","alive","alkyd","alkyl","allan","allay","aller","alley","allot","allow","alloy",
    "allyl","almon","almud","almug","alody","aloed","aloft","alogy","aloid","aloin","aloma","alone","along","aloof","alose",
    "aloud","alowe","alpha","altar","alter","altho","altin","altun","alula","alure","aluta","alvar","alvus","alway","amaas",
    "amaga","amain","amala","amang","amani","amapa","amass","amaze","amban","ambar","ambay","amber","ambit","amble","ambon",
    "ambos","ambry","ameed","ameen","amelu","amend","amene","ament","amhar","amice","amide","amido","amine","amini","amino",
    "amiss","amity","amman","ammer","amnia","amnic","amoke","amole","among","amort","amour","amove","amper","ample","amply",
    "ampul","ampyx","amsel","amuck","amula","amuse","amuze","amvis","amylo","anabo","anama","anana","ancon","anear","anele",
    "anend","anent","angel","anger","angle","angor","angry","angst","anigh","anile","anima","anime","animi","anion","anise",
    "anjan","ankee","anker","ankle","ankus","annal","annat","annet","annex","annoy","annul","anode","anoil","anole","anoli",
    "anomy","ansar","antal","antes","antic","antra","antre","anury","anvil","aorta","apace","apaid","apart","apeak","apert",
    "apery","aphid","apian","apiin","aping","apish","apism","apnea","apoop","aport","apout","appay","appet","apple","apply",
    "apron","apsis","aptly","araba","araca","arado","arain","arake","arara","arati","arbor","arche","archy","ardeb","ardor",
    "ardri","aread","areal","arear","areek","areel","arena","arend","areng","arent","arete","argal","argel","argil","argol",
    "argon","argot","argue","arhar","arhat","ariel","ariot","arise","arist","arite","arjun","arles","armed","armer","armet",
    "armil","armor","arnee","arnut","aroar","arock","aroid","aroma","aroon","arose","arpen","arrah","arras","arrau","array",
    "arrie","arris","arrow","arses","arsis","arsle","arson","arsyl","artal","artar","artel","artha","aruke","arupa","arusa",
    "arval","arvel","arzan","arzun","asale","asana","ascan","ascii","ascon","ascot","ascry","ascus","asdic","ashen","ashes",
    "ashet","ashur","aside","askar","asker","askew","askip","askos","aslop","asoak","asoka","aspen","asper","aspic","assai",
    "assay","asset","assis","astay","aster","astir","astor","asway","aswim","asyla","atavi","ataxy","atelo","athar","atilt",
    "atlas","atlee","atman","atmid","atmos","atoke","atoll","atomy","atone","atony","atopy","atour","atria","atrip","attar",
    "atter","attic","attid","atule","atune","atwin","atypy","audio","audit","augen","auger","aught","augur","aulae","aulic",
    "auloi","aulos","aumil","aurae","aural","aurar","auric","aurin","aurir","aurum","auryl","autem","auxin","avahi","avail",
    "avast","avens","avera","avert","avian","avick","avine","aviso","avoid","awabi","awaft","await","awake","awald","awalt",
    "awane","award","aware","awash","awave","awber","aweek","aweel","awest","aweto","awful","awhet","awhir","awide","awing",
    "awink","awiwi","awned","awner","awoke","awork","axial","axile","axine","axiom","axion","axite","axled","axman","axoid",
    "ayelp","aylet","ayllu","ayond","ayont","ayous","azide","azine","azoch","azofy","azoic","azole","azote","azoth","azoxy",
    "azure","azury","azyme","babai","babby","baboo","babul","bacao","bacca","bache","bacon","badan","badge","badly","baffy",
    "bafta","bagel","baggy","bagre","bahan","bahar","bahay","bahoe","bahoo","bahur","bahut","baioc","bairn","baith","baize",
    "bajan","bajra","bajri","bakal","baked","baken","baker","bakie","bakli","balai","balao","balas","baldy","balei","baler",
    "balky","balli","bally","balmy","baloo","balow","balsa","balut","balza","banak","banal","banat","banca","banco","banda",
    "bande","bandi","bando","bandy","banga","bange","banig","banjo","banky","banns","banty","banya","barad","barbe","bardo",
    "bardy","barer","barff","barge","bargh","baria","baric","barid","barie","baris","barit","barky","barmy","barny","baroi",
    "baron","barra","barry","barse","barth","barye","basal","based","bases","basic","basil","basin","basis","bason","basos",
    "basso","basta","baste","basto","batad","batch","batea","bated","batel","bater","bathe","batik","baton","batta","batty",
    "bauch","bauno","bauta","bavin","bayal","bayed","bayok","bayou","bazoo","beach","beady","beaky","beala","beamy","beano",
    "beant","beany","beard","bearm","beast","beata","beath","beaux","bebar","bebat","bebay","bebed","bebog","bebop","becap",
    "becry","becut","bedad","beday","bedel","beden","bedew","bedim","bedin","bedip","bedog","bedot","bedub","bedur","bedye",
    "beech","beefy","beery","beest","beeth","beety","beeve","befan","befit","befog","befop","begad","begar","begat","begay",
    "begem","beget","begin","begob","begum","begun","begut","behap","behen","beice","beige","being","beira","beisa","bejan",
    "bejel","bejig","bekah","bekko","belah","belam","belar","belay","belch","belee","belga","belie","belle","belly","below",
    "belve","bemad","beman","bemar","bemat","bemix","bemud","benab","bench","benda","bendy","benet","benjy","benne","benny",
    "bensh","benty","benzo","beode","bepat","bepaw","bepen","bepun","berat","beray","beret","bergy","berne","berri","berry",
    "berth","beryl","besan","besee","beset","besin","besit","besom","besot","bespy","besra","betag","betel","betis","betso",
    "betty","bevel","bever","bevue","bewet","bewig","bezel","bezzi","bezzo","bhalu","bhang","bhara","bhava","biabo","bichy",
    "bidar","biddy","bider","bidet","bidri","bield","bifer","bifid","bigha","bight","bigot","bijou","bilbo","bilby","bilch",
    "bilge","bilgy","bilic","bilio","billa","billy","bilsh","binal","binge","bingo","bingy","binna","biome","biose","biota",
    "biped","bipod","birch","birdy","birle","birma","birny","birse","birsy","birth","bison","bisti","bitch","biter","bitty",
    "biune","bixin","bizet","black","blade","blady","blaff","blain","blair","blake","blame","blanc","bland","blank","blare",
    "blart","blase","blash","blast","blate","blaze","blazy","bleak","blear","bleat","bleck","bleed","blend","blent","bless",
    "blest","blibe","blick","blimp","blimy","blind","blink","bliss","blite","blitz","blizz","bloat","block","bloke","blood",
    "bloom","bloop","blore","blout","blown","blowy","bluer","blues","bluet","bluey","bluff","blunk","blunt","blurb","blurt",
    "blush","blype","board","boast","bobac","bobby","bocal","bocca","bocce","bocoy","boden","boder","bodge","bodhi","bodle",
    "bogan","bogey","boggy","bogie","bogle","bogue","bogum","bogus","bohea","bohor","boily","boist","bokom","bolar","boldo",
    "boled","bolis","bolly","bolti","bolus","bombo","bonce","boned","boner","bongo","bonny","bonus","bonze","booby","boody",
    "booky","booly","boomy","boonk","boort","boose","boost","boosy","booth","boots","booty","booze","boozy","borak","boral",
    "borax","boree","borer","borgh","boric","borne","boron","borty","bortz","boryl","bosch","boser","bosky","bosom","bossy",
    "bosun","botch","bothy","bouge","bough","boule","bound","bourd","bourg","bourn","bouse","bousy","bouto","bovid","bowed",
    "bowel","bower","bowet","bowie","bowla","bowls","bowly","boxen","boxer","boxty","boyar","boyer","boyla","bozal","bozze",
    "braca","brace","brach","brack","bract","braid","brail","brain","brake","braky","brand","brank","brant","brash","brass",
    "brave","bravo","brawl","brawn","braws","braxy","braza","braze","bread","break","bream","breba","breck","brede","bredi",
    "breed","breek","breme","brent","breth","brett","breva","breve","briar","bribe","brick","bride","brief","brier","brill",
    "brine","bring","brink","briny","brisk","briss","brith","brizz","broad","broch","brock","broil","broke","broll","broma",
    "brome","bronc","bronk","brood","brook","brool","broom","broon","brose","brosy","broth","brown","brugh","bruin","bruit",
    "bruke","brume","brunt","brush","brute","bruzz","buaze","bubal","bubby","bucca","buchu","bucko","bucky","buddy","budge",
    "buffy","bugan","buggy","bugle","bugre","build","built","buist","bulak","bulby","bulge","bulgy","bulky","bulla","bully",
    "bulse","bumbo","bumpy","bunce","bunch","bundy","bungo","bungy","bunko","bunny","bunty","bunya","buran","burao","burel",
    "buret","burgh","burin","burka","burke","burly","burnt","burny","burro","burry","bursa","burse","burst","busby","bushi",
    "bushy","busky","bussu","butch","butic","butte","butty","butyl","butyr","buxom","buyer","buzzy","bylaw","byous","bysen",
    "byway","caama","cabal","caban","cabas","cabby","cabda","caber","cabin","cabio","cable","cabob","cabot","cacam","cacao",
    "cache","cacti","cacur","caddy","cader","cadet","cadew","cadge","cadgy","cados","cadre","cadua","cadus","caeca","caffa",
    "cafiz","caged","cager","cagey","caggy","cagit","cahiz","cahot","cahow","caird","cairn","cajun","caker","cakey","calid",
    "calix","calli","callo","calmy","calor","calve","calyx","caman","camel","cameo","campo","camus","canal","canch","candy",
    "canel","caner","canid","canna","canny","canoe","canon","canso","canto","canty","canun","caoba","capax","caped","capel",
    "caper","capes","capon","capot","cappy","capsa","carat","carbo","cardo","carer","caret","carga","cargo","carid","carls",
    "caroa","carob","carol","carom","carry","carse","carte","carty","carua","carve","caryl","casal","casco","cased","caser",
    "casha","casse","caste","catan","catch","cater","catty","cauch","cauda","cauld","cauma","caupo","cause","cavae","caval",
    "cavel","cavie","cavil","cavus","cawky","caxon","cease","cebid","cebil","cebur","cedar","ceder","cedre","cedry","ceibo",
    "ceile","cella","cello","cense","cento","ceorl","cequi","ceral","ceras","cerci","cered","cerer","ceria","ceric","cerin",
    "certy","ceryl","cetic","cetin","cetyl","chack","chafe","chaff","chaft","chain","chair","chais","chaja","chaka","chalk",
    "champ","chang","chank","chant","chaos","chape","chaps","chapt","chard","chare","chark","charm","charr","chart","chary",
    "chase","chasm","chati","chauk","chaus","chawk","chawl","chaya","cheap","cheat","check","cheek","cheep","cheer","cheet",
    "cheir","cheke","cheki","chela","chelp","chena","cheng","chert","chess","chest","cheth","cheve","chevy","chewy","chick",
    "chico","chide","chief","chien","child","chile","chili","chill","chime","china","chine","ching","chink","chino","chint",
    "chips","chirk","chirm","chiro","chirp","chirr","chive","chlor","choca","chock","choel","choga","choil","choir","choke",
    "choky","chola","chold","choli","chomp","choop","chopa","chord","chore","chort","chose","chott","choup","chous","chowk",
    "choya","chria","chuck","chufa","chuff","chump","chunk","churl","churm","churn","churr","chute","chyak","chyle","chyme",
    "cibol","cicad","cicer","cider","cigar","cigua","cilia","cimex","cinch","cinct","cinel","circa","cirri","cisco","cista",
    "citee","citer","citua","civet","civic","civil","civvy","clack","claim","clamb","clame","clamp","clang","clank","clapt",
    "clark","claro","clart","clary","clash","clasp","class","claut","clava","clave","clavy","clawk","clead","cleam","clean",
    "clear","cleat","cleck","cleek","cleft","clerk","cleve","click","cliff","clift","clima","climb","clime","cline","cling",
    "clink","clint","clips","clipt","clite","clive","cloak","cloam","clock","cloff","cloit","clomb","clone","cloof","cloop",
    "cloot","close","closh","clote","cloth","cloud","clour","clout","clove","clown","cluck","cluff","clump","clung","clunk",
    "clyer","clype","cnida","coach","coact","coaid","coaly","coapt","coarb","coast","coati","coaxy","cobby","cobia","coble",
    "cobra","cocci","cocco","cocky","cocoa","coder","codex","codol","codon","cogon","cogue","cohol","coign","coiny","coker",
    "colic","colin","colly","colon","color","colza","comal","comby","comer","comes","comet","comfy","comic","comma","compo",
    "conal","conch","coned","coner","cones","conga","conic","conin","conky","conte","conto","conus","cooba","cooee","cooer",
    "cooja","cooky","cooly","coomb","coomy","coony","coost","copal","copei","copen","coper","copis","coppy","copra","copse",
    "copsy","copus","coque","corah","coral","coram","cordy","cored","corer","corge","corgi","corke","corky","cornu","corny",
    "coroa","corol","corps","corse","corta","coryl","cosec","coset","cosse","costa","cotch","cothe","cothy","cotta","cotte",
    "cotty","couac","couch","coude","cough","could","couma","count","coupe","courb","court","couth","coved","cover","covet",
    "covey","covid","covin","cowal","cower","cowle","coxal","coyan","coyly","coyol","coypu","cozen","crack","craft","crain",
    "crake","cramp","crane","crank","crape","craps","crapy","crare","crash","crass","crate","crave","cravo","crawl","crawm",
    "craze","crazy","creak","cream","creat","creed","creek","creel","creem","creen","creep","crena","crepe","crept","crepy",
    "cress","crest","creta","cribo","crick","cried","crier","criey","crile","crime","crimp","crine","crink","crisp","criss",
    "crith","croak","croci","crock","croft","crome","crone","cronk","crony","crood","crook","crool","croon","crore","crosa",
    "cross","croup","crout","crowd","crowl","crown","croze","cruce","cruck","crude","cruel","cruet","crumb","crump","crunk",
    "crunt","cruor","cruse","crush","crust","cruth","crypt","ctene","cubby","cubeb","cuber","cubic","cubit","cuddy","cueca",
    "cuffy","culet","culla","cully","culmy","culpa","cumal","cumay","cumbu","cumic","cumin","cumol","cumyl","cunye","cupay",
    "cupel","cuppy","curby","curch","curdy","curer","curie","curin","curio","curly","curry","curse","curst","curua","curve",
    "curvy","cusec","cushy","cusie","cusso","cutch","cutie","cutin","cutis","cutty","cutup","cyath","cycad","cycle","cylix",
    "cymar","cymba","cynic","cypre","cyrus","cyton","dabba","dabby","dadap","daddy","daffy","dagga","daggy","daily","daira",
    "dairi","dairy","daisy","daiva","daker","dakir","dalar","daler","dalle","dally","daman","damie","damme","dampy","dance",
    "danda","dandy","danio","danli","danta","darac","daraf","darat","darby","darer","daric","darky","daroo","darst","darts",
    "dashy","dasnt","dassy","datch","dater","datil","datum","daube","dauby","daunt","daven","daver","davit","dawdy","dawny",
    "dawut","dayal","dazed","deair","dealt","deary","deash","death","deave","debar","debby","deben","debit","debus","debut",
    "decad","decal","decan","decap","decay","decil","decke","decoy","decry","decus","decyl","deedy","defat","defer","defog",
    "degas","degum","deice","deify","deign","deink","deism","deist","deity","dekko","dekle","delay","delft","delta","delve",
    "demal","demit","demob","demon","demos","denat","denda","denim","dense","denty","deota","depas","depoh","depot","depth",
    "derah","derat","deray","derby","deric","derma","derry","desex","desma","dessa","desyl","detar","detax","deter","detin",
    "detur","deuce","devil","devow","dewan","dewax","dewer","dhabb","dhava","dheri","dhobi","dhole","dhoni","dhoon","dhoti",
    "dhoul","dhyal","diact","diamb","diary","dicer","dicky","dicot","dicta","diddy","didie","didle","didna","didnt","didst",
    "didym","diene","dight","digit","diker","dildo","dilli","dilly","dimer","dimit","dimly","dimps","dinar","diner","dinge",
    "dingo","dingy","dinic","dinky","dinus","diode","diose","diota","dioxy","dirge","dirty","disme","disna","dital","ditch",
    "diter","ditto","ditty","divan","divel","diver","divot","divus","divvy","dixie","dixit","dizen","dizzy","djave","dobby",
    "dobla","dobra","doddy","dodge","dodgy","doest","dogal","doggo","doggy","dogie","dogly","dogma","doigt","doily","doina",
    "doing","dolia","dolly","dolor","domal","domba","domer","domic","dompt","donax","donee","doney","donga","donna","donor",
    "donum","dooja","dooli","dooly","dooms","doper","dopey","dorab","dorad","doree","doria","dorje","dormy","dorts","dorty",
    "doser","dosis","dotal","doted","doter","dotty","douar","doubt","douce","dough","douse","dover","dowdy","dowed","dowel",
    "dower","dowie","downy","dowry","dowse","dozed","dozen","dozer","draff","draft","drago","drail","drain","drake","drama",
    "dramm","drang","drank","drant","drape","drate","drawk","drawl","drawn","dread","dream","drear","dreep","dregs","dreng",
    "dress","drest","drias","dried","drier","drift","drill","drink","drinn","drisk","drive","drogh","droit","droll","drome",
    "drona","drone","drony","drool","droop","dropt","dross","droud","drouk","drove","drovy","drown","druid","drung","drunk",
    "drupe","druse","drusy","druxy","dryad","dryas","dryly","dryth","duali","dubba","dubby","ducal","ducat","duces","duchy",
    "dugal","duhat","dujan","dukhn","duler","dulia","dully","dulse","dumba","dummy","dumpy","dunal","dunce","dunch","dungy",
    "dunne","dunny","dunst","duole","duper","dupla","duple","duppy","dural","durax","durra","durry","durst","duryl","dusio",
    "dusky","dusty","dutch","dutra","duvet","dwale","dwalm","dwang","dwarf","dwell","dwelt","dwine","dying","dyker","eager",
    "eagle","eagre","eared","early","earth","easel","easer","eaten","eater","eaved","eaver","eaves","ebony","echea","ecize",
    "eclat","ecoid","ecole","ectad","ectal","edder","edema","edged","edger","edict","edify","educe","educt","eeler","eerie",
    "egest","egger","egret","eider","eight","eigne","eimer","eject","ekaha","eking","elain","eland","elate","elbow","elder",
    "eldin","elect","elegy","elemi","elfic","elfin","elide","elite","eloge","elope","elops","elsin","elude","elute","elvan",
    "elver","elves","elvet","embar","embay","embed","ember","embog","embow","embox","embus","emcee","emeer","emend","emery",
    "emmer","emmet","emote","empty","enact","enage","enapt","enarm","enate","encup","ended","ender","endew","endow","endue",
    "enema","enemy","engem","enhat","eniac","enjoy","ennui","enoil","enorm","enray","enrib","enrol","enrut","ensky","ensue",
    "entad","ental","enter","entia","entry","enure","envoy","enzym","eosin","epact","ephah","ephod","ephor","epoch","epode",
    "epopt","epulo","equal","equid","equip","erade","erase","erbia","erect","erept","ergal","ergon","ergot","erika","erizo",
    "erode","erose","error","eruca","eruct","erupt","esere","eshin","esker","essay","essed","ester","estoc","estop","estre",
    "estus","ethal","ethel","ether","ethic","ethid","ethos","ethyl","ettle","etude","eupad","eusol","evade","evase","evens",
    "event","evert","every","evict","evoke","ewder","ewery","exact","exalt","excel","exdie","exeat","exert","exile","exist",
    "exite","exlex","exode","exody","expel","exter","extol","extra","exude","exult","eying","eyoty","eyrie","eyrir","fabes",
    "fable","faced","facer","facet","facia","facks","facty","faddy","faded","faden","fader","fadge","faery","faffy","fager",
    "fagot","faham","fains","faint","fairm","fairy","faith","faker","fakir","fally","false","fanal","fanam","fancy","fangy",
    "fanon","farad","farce","farcy","farde","fardh","fardo","farer","farmy","farse","fatal","fated","fatil","fatly","fatty",
    "faugh","fauld","fault","fause","faust","fauve","favor","favus","fawny","feast","featy","feaze","fecal","feces","feedy",
    "feere","feeze","feign","feint","feist","felid","felly","felon","felty","femic","femur","fence","fendy","fenks","fenny",
    "feoff","feral","feria","ferie","ferly","ferme","ferny","ferri","ferry","fetal","fetch","fetid","fetor","fetus","feuar",
    "feued","fever","fezzy","fiard","fiber","fibry","fiche","fichu","fidge","field","fiend","fient","fiery","fifer","fifie",
    "fifth","fifty","figgy","fight","fikie","filao","filar","filch","filer","filet","filly","filmy","filth","final","finch",
    "finer","finis","finny","fiord","fique","firca","fired","firer","firry","first","firth","fishy","fisty","fitch","fitly",
    "fitty","fiver","fives","fixed","fixer","fizzy","fjeld","flack","flaff","flail","flair","flake","flaky","flamb","flame",
    "flamy","flane","flank","flare","flary","flash","flask","flavo","flawn","flawy","flaxy","fleam","fleay","fleck","fleer",
    "fleet","flesh","flews","flick","flier","flimp","fling","flint","flipe","flirt","flisk","flite","float","flock","floey",
    "flong","flood","floor","flora","flory","flosh","floss","flota","flour","flout","flown","flued","fluer","fluey","fluff",
    "fluid","fluke","fluky","flume","flump","flung","flunk","fluor","flurn","flurr","flush","flusk","flute","fluty","flyer",
    "flype","foaly","foamy","focal","focus","fodda","foder","fodge","foehn","fogey","foggy","fogle","fogon","fogou","fogus",
    "fohat","foist","foldy","folia","folie","folio","folky","folly","fomes","fondu","fonly","foody","foots","footy","foppy",
    "foray","forby","force","fordo","fordy","forel","forge","forgo","forky","forme","formy","forte","forth","forty","forum",
    "fosie","fossa","fosse","fotch","fotui","found","fount","foute","fouth","fovea","foxer","foyer","frack","fraid","fraik",
    "frail","frame","franc","frank","frase","frass","fraud","frawn","frayn","fraze","freak","fream","freck","freed","freer",
    "freet","freir","freit","fremd","fresh","frett","friar","fried","frier","frike","frill","frisk","frist","frith","fritt",
    "frize","frizz","frock","frond","front","froom","frore","frory","frosh","frost","froth","frowl","frown","frowy","froze",
    "fruit","frump","frush","fryer","fubby","fubsy","fucus","fuder","fudge","fudgy","fuffy","fugal","fuggy","fugle","fugue",
    "fully","fulth","fulwa","fumer","fumet","fundi","funds","fungi","fungo","funis","funky","funny","fural","furan","furca",
    "furil","furor","furry","furyl","furze","furzy","fused","fusee","fusht","fusil","fussy","fusty","futwa","fuzzy","gabby",
    "gable","gaddi","gadge","gadid","gaffe","gagee","gager","gagor","gaily","gaine","gains","gaize","galah","galea","galee",
    "galet","galey","galla","gally","galop","gamba","gamic","gamin","gamma","gammy","gamut","ganam","ganch","ganef","ganga",
    "gange","ganja","gansy","ganta","ganza","gaper","gapes","gappy","garad","garce","gardy","gareh","garle","garoo","garse",
    "garth","garum","gashy","gaspy","gassy","gatch","gated","gater","gator","gauby","gaudy","gauge","gault","gaumy","gaunt",
    "gauss","gauze","gauzy","gavel","gawby","gawky","gayal","gazee","gazel","gazer","gazon","gease","gebur","gecko","geest",
    "geira","gelid","gelly","gemel","gemma","gemmy","gemot","gemul","genal","genep","genet","genic","genie","genii","genin",
    "genip","genom","genos","genre","genro","genty","genua","genus","genys","geode","geoid","geoty","gerah","gerbe","gerim",
    "gerip","germy","gesso","geste","getah","getup","geyan","ghazi","ghoom","ghost","ghoul","giant","gibby","gibel","giber",
    "gibus","giddy","gigot","gilia","gilim","gilly","gilpy","gilse","gimel","ginny","gipon","girba","girly","girny","girse",
    "girsh","girth","gisla","given","giver","givey","glace","glack","glade","glady","glaga","glaik","glair","glaky","gland",
    "glans","glare","glary","glass","glaum","glaur","glaze","glazy","gleam","glean","gleba","glebe","glede","gledy","gleed",
    "gleek","gleet","glent","glial","glide","gliff","glime","glink","glint","glisk","gloam","gloat","globe","globy","gloea",
    "glome","gloom","glore","glory","gloss","glost","glout","glove","gloze","gluck","glued","gluer","gluey","gluma","glume",
    "glump","glyph","gnarl","gnash","gnawn","gnome","goaty","goave","goban","gobbe","gobby","godet","godly","goety","gogga",
    "going","goldy","golee","golem","golly","goloe","golpe","gomer","gonad","gonal","goner","gonia","gonid","gonne","gonys",
    "goods","goody","goofy","gools","gooma","goose","goosy","goral","goran","gorce","gorer","gorge","goric","gorra","gorry",
    "gorse","gorsy","gossy","gotch","gotra","gouge","goumi","gourd","gouty","gowan","goyim","goyin","goyle","grace","grade",
    "graff","graft","grail","grain","graip","grama","grame","gramp","grand","grane","grank","grano","grant","grape","graph",
    "grapy","grasp","grass","grate","grave","gravy","graze","great","grebe","grece","greed","green","greet","grege","grego",
    "grein","grice","gride","grief","griff","grift","grike","grill","grime","grimp","grimy","grind","gripe","gripy","grist",
    "grith","grits","groan","groat","groff","groin","groom","groop","groot","grope","gross","grosz","grouf","group","grout",
    "grove","grovy","growl","grown","grubs","gruel","gruff","grume","grump","grunt","grush","gruss","gryde","guaba","guaco",
    "guaka","guama","guana","guano","guara","guard","guasa","guava","guaza","gubbo","gucki","gudge","gudok","guess","guest",
    "guffy","gugal","guiba","guide","guige","guijo","guild","guile","guilt","guily","guise","gulae","gular","gulch","gules",
    "gulfy","gulix","gully","gulpy","gumbo","gumby","gumly","gumma","gummy","gundi","gundy","gunge","gunne","gunny","guppy",
    "gurge","gurly","gurry","gushy","gusla","gusle","gusto","gusty","gutta","gutte","gutti","gutty","guyer","gweed","gwely",
    "gwine","gymel","gynic","gypsy","gyral","gyric","gyron","gyrus","habit","hache","hacky","haddo","hadji","hafiz","haggy",
    "hagia","haily","haine","haire","hairy","hajib","hakam","hakim","halal","halch","haler","halma","halse","halve","hamal",
    "hamel","hammy","hamsa","hamus","hamza","hance","hanch","handy","hange","hanif","hanky","hanna","hansa","hanse","haole",
    "haoma","haori","haply","happy","harbi","hardy","harem","harka","harry","harsh","hasan","hashy","hasky","hasta","haste",
    "hasty","hatch","hater","hathi","hatty","haugh","hauld","haulm","haunt","hause","havel","haven","haver","havoc","hawer",
    "hawky","hawok","hawse","hayey","hazel","hazen","hazer","hazle","heady","heald","heaps","heapy","heart","heath","heave",
    "heavy","hecte","heder","hedge","hedgy","heedy","heeze","heezy","hefty","heiau","heigh","helio","helix","hello","helly",
    "heloe","helve","hemad","hemal","hemen","hemic","hemin","hemol","hempy","henad","hence","henna","henny","henry","hepar",
    "herby","herem","herma","herne","heron","herse","hertz","heuau","heugh","hewel","hewer","hexad","hexer","hexis","hexyl",
    "hiant","hiate","hided","hider","hield","hight","hiker","hilch","hilly","hilsa","hilum","hilus","hinau","hinch","hinge",
    "hinny","hiper","hippo","hippy","hired","hirer","hirse","hitch","hithe","hiver","hives","hoard","hoary","hoast","hobby",
    "hocco","hocky","hocus","hoddy","hogan","hoggy","hoick","hoise","hoist","hokey","hokum","holer","holey","holia","holla",
    "hollo","holly","homer","homey","honda","hondo","honey","honor","hooch","hooey","hoofs","hoofy","hooky","hooly","hoose",
    "hoosh","hoove","hoped","hoper","hoppy","horal","horde","horme","horny","horse","horst","horsy","hosed","hosel","hotch",
    "hotel","hotly","hough","hound","houri","house","housy","hovel","hoven","hover","howdy","howel","howff","howso","hoyle",
    "huaca","huaco","hubba","hubby","hucho","huffy","hulky","human","humbo","humet","humic","humid","humin","humor","humph",
    "humpy","humus","hunch","hundi","hunks","hunky","hurds","hurly","huron","hurry","hurst","hurty","husho","husky","hussy",
    "hutch","hutia","huzza","hydro","hyena","hying","hyleg","hylic","hymen","hynde","hyoid","hyper","hypha","hypho","hyrax",
    "hyson","iambi","ibota","icaco","ichor","icica","icily","icing","ictic","ictus","idant","iddat","ideal","idgah","idiom",
    "idiot","idite","idler","idola","idose","idryl","igloo","ihram","ikona","ileac","ileon","ileum","ileus","iliac","ilial",
    "iliau","ilima","ilium","illth","image","imago","imban","imbat","imbed","imber","imbue","imide","imine","imino","immew",
    "immit","immix","impar","impel","impen","imply","impot","imshi","inaja","inane","inapt","inarm","incog","incur","incus",
    "incut","indan","index","indic","indri","indue","indyl","inept","inerm","inert","infer","infit","infix","infra","ingle",
    "ingot","inial","inion","inken","inker","inket","inkle","inlaw","inlay","inlet","inner","innet","inoma","inone","inorb",
    "input","inrub","inrun","insea","insee","inset","inter","intil","intue","inula","inure","inurn","inwit","iodic","iodol",
    "ionic","irade","irate","irene","irian","iroko","irone","irony","islay","islet","islot","ismal","issei","issue","istle",
    "itchy","itcze","itemy","ither","ivied","ivory","izard","izote","iztle","jabia","jabot","jabul","jacal","jacko","jaded",
    "jagat","jager","jaggy","jagir","jagla","jagua","jakes","jalap","jaman","jambo","jammy","jantu","janua","japan","japer",
    "jarra","jarry","jasey","jatha","jaunt","javer","jawab","jawed","jazzy","jeans","jeery","jehup","jelab","jelly","jemmy",
    "jenna","jenny","jerez","jerib","jerky","jerry","jetty","jewel","jheel","jhool","jibby","jiboa","jiffy","jiggy","jihad",
    "jimmy","jingo","jinja","jinks","jinni","jinny","jiqui","jirga","jitro","jixie","jocko","jocum","jodel","joint","joist",
    "joker","jokul","jolly","jolty","joola","joree","jorum","joshi","josie","jotty","jough","joule","jours","joust","jowar",
    "jowel","jower","jowly","jowpy","jubbe","judex","judge","jufti","jugal","juger","jugum","juice","juicy","julep","julid",
    "julio","jumba","jumbo","jumby","jumma","jumpy","junta","junto","jupon","jural","jurat","jurel","juror","justo","jutka",
    "jutty","juvia","kabel","kados","kafir","kafiz","kafta","kahar","kahau","kaiwi","kakar","kakke","kalon","kamao","kamas",
    "kamik","kanae","kanap","kanat","kande","kaneh","kanga","kapai","kapok","kappa","kappe","kapur","kaput","karbi","karch",
    "karma","karou","karri","karst","kashi","kassu","katar","katha","katun","kauri","kayak","kazoo","keach","keawe","kebab",
    "kecky","kedge","keech","keena","keest","keeve","kefir","keita","keleh","kelek","kelep","kella","kelly","kelpy","kelty",
    "kempt","kempy","kenaf","kench","kenno","kerat","kerel","kerry","ketal","ketch","keten","ketol","kette","ketty","ketyl",
    "kevel","keyed","khadi","khair","khaja","khaki","khass","khoja","khoka","khula","khvat","kiack","kiaki","kiang","kibei",
    "kiddy","kieye","kikar","kilah","kilan","kileh","kiley","kilim","killy","kinah","kinch","kinky","kioea","kiosk","kippy",
    "kirve","kishy","kisra","kissy","kiswa","kitab","kitar","kithe","kitty","kiver","kiyas","klops","klosh","knack","knape",
    "knark","knave","knead","kneed","kneel","knell","knelt","knezi","kniaz","knick","knife","knock","knoll","knosp","knout",
    "knowe","known","knurl","knyaz","koala","koali","koban","kodak","kodro","kohua","koila","koine","kokam","kokan","kokil",
    "kokio","kokra","kokum","kolea","kombu","konak","kongu","kooka","koppa","korec","korin","kosin","kotal","kouza","kovil",
    "koyan","kraal","kraft","krait","krama","kraut","kreis","krems","kreng","krina","krome","krona","krone","kroon","krosa",
    "kubba","kudos","kudzu","kugel","kukri","kukui","kulah","kulak","kumbi","kunai","kurus","kusam","kusha","kusti","kusum",
    "kvass","kvint","kyack","kylix","laang","labba","label","labia","labis","labor","labra","lacca","laced","lacer","lacet",
    "lache","lacis","lacto","laden","lader","ladle","laeti","lagan","lagen","lager","lagna","laich","laigh","laine","laird",
    "lairy","laity","laker","lakie","lamba","lamby","lamel","lamia","lamin","lammy","lanas","lanaz","lance","laney","langi",
    "lanky","lanum","lapel","lapon","lapse","lapsi","larch","lardy","large","largo","larid","larin","larky","larry","larva",
    "larve","laser","lasso","lasty","latah","latch","lated","laten","later","latex","lathe","lathy","latro","latus","lauan",
    "laugh","lauia","laund","laura","laver","lavic","lawny","lawzy","laxly","layer","layne","lazar","leach","leady","leafy",
    "leaky","leant","leapt","learn","lease","leash","least","leath","leave","leavy","leban","leden","ledge","ledgy","ledol",
    "leech","leeky","leery","legal","leger","leges","leggy","legit","legoa","legua","lehua","lekha","leman","lemel","lemma",
    "lemon","lemur","lenad","lench","lenis","lenth","lento","leper","lepra","lerot","lesiy","lessn","letch","letup","leuch",
    "leuco","leuma","levee","level","lever","levin","levir","lewis","lewth","lexia","liana","liang","liard","libel","liber",
    "libra","licca","lichi","licit","liege","liesh","lieue","lieve","lifer","lifey","ligas","light","ligne","liken","liker",
    "likin","lilac","liman","limbo","limby","limen","limer","limes","limey","limit","limma","limmu","limpy","limsy","linch",
    "lindo","linea","lined","linen","liner","linga","linge","lingo","lingy","linha","linie","linin","linja","linje","links",
    "linky","linon","linty","lipin","lippy","lisle","litas","litch","liter","lithe","lithi","litho","lithy","litra","litus",
    "lived","liven","liver","livid","livor","livre","liwan","llama","llano","loach","loamy","loath","loave","lobal","lobar",
    "lobby","lobed","local","lochy","locky","locum","locus","lodge","loess","lofty","logia","logic","logie","login","logoi",
    "logos","lohan","lokao","loket","lolly","longa","longe","longs","looby","loony","loopy","loose","loper","loppy","loral",
    "loran","lordy","lored","loric","loris","lorry","lorum","losel","loser","lotic","lotto","lotus","louch","louey","lough",
    "loulu","loupe","louse","lousy","louty","lover","lowan","lower","lowly","lowth","loxia","loxic","loyal","lubra","lucet",
    "lucid","lucky","lucre","luger","lulab","lumen","lummy","lumpy","lunar","lunch","lunes","lunge","lungi","lungy","lupis",
    "lupus","lural","lurch","lurer","lurid","lurky","lurry","lushy","lusky","lusty","luteo","luter","luxus","lyard","lycid",
    "lyery","lying","lymph","lynch","lyric","lysin","lysis","lyssa","lytic","lytta","macan","macao","macaw","macco","macer",
    "machi","macle","macro","madam","madid","madly","mafic","mafoo","magas","magic","magma","magot","mahar","mahoe","mahua",
    "maidy","maiid","mains","maint","maire","maize","major","maker","makuk","malar","malax","maleo","malic","malik","malmy",
    "malty","mamba","mambo","mamma","mammy","manal","manas","maned","manei","manes","maney","manga","mange","mangi","mango",
    "mangy","mania","manic","manid","maniu","manly","manna","manny","manoc","manor","manse","manso","manta","manto","manul",
    "manus","mapau","maple","mappy","maqui","marae","maral","march","marco","mardy","marge","maria","marid","maris","marka",
    "marli","marly","marok","marry","marsh","masha","mashy","mason","massa","masse","massy","masty","matai","matax","match",
    "mater","matey","matin","matka","matra","matsu","matta","matte","matti","matzo","maugh","maund","mauve","mavis","mawky",
    "maxim","maybe","maynt","mayor","mazed","mazer","mazic","mazut","mbori","mealy","meant","mease","meaty","mecon","medal",
    "media","medic","medio","meece","meese","meile","meith","melam","melch","melee","melic","meloe","melon","melos","mends",
    "mensa","mense","mensk","merch","mercy","merel","merge","mergh","meril","merit","merle","merop","meros","merry","merse",
    "mesad","mesal","mesem","meshy","mesic","mesne","meson","messe","messy","metad","metal","metel","meter","metic","metis",
    "metra","metze","meuse","meute","mewer","mezzo","miaow","miasm","miaul","miche","micht","micro","middy","midge","midgy",
    "midst","miffy","might","mikie","milch","miler","milha","milky","milla","mille","milpa","milty","mimeo","mimer","mimic",
    "mimly","minar","mince","miner","mines","minge","mingy","minim","minny","minor","minot","minty","minus","miqra","mirid",
    "mirth","mirza","misdo","miser","misgo","misky","missy","misty","miter","mitis","mitra","mitre","mitty","mixed","mixen",
    "mixer","mizzy","mneme","mobby","mobed","moble","mocha","modal","model","moggy","mohar","mohel","mohur","moire","moise",
    "moist","moity","mokum","molal","molar","moldy","moler","molka","molle","molly","molpe","momme","mommy","monad","monal",
    "monas","monel","moner","money","monny","monte","month","mooch","moody","mools","moony","moorn","moors","moory","moosa",
    "moose","moost","mooth","moper","mopla","moppy","mopsy","mopus","moral","morat","moray","morel","mores","morga","moric",
    "morin","mormo","morne","moroc","moron","morph","morse","morth","mosey","mossy","moste","moted","motel","moter","motet",
    "motey","mothy","motif","motor","motte","motto","moudy","mould","moule","mouls","mouly","mound","mount","mourn","mouse",
    "mousy","mouth","mover","movie","mowch","mower","mowha","mowie","mowra","mowse","mowth","moyen","moyle","mpret","muang",
    "mucic","mucid","mucin","mucky","mucor","mucro","mucus","mudar","mudde","muddy","mudee","mudir","mudra","muffy","mufti",
    "mufty","muggy","muist","mukti","mulch","mulct","muley","mulga","mulla","mulse","mummy","mumps","munch","munga","munge",
    "mungo","mungy","mural","murex","murga","murid","murky","murly","murra","murre","murva","murza","musal","musar","mused",
    "muser","musha","mushy","music","musie","musky","mussy","musty","mutch","mutic","muzzy","myall","myoid","myoma","myope",
    "myops","myopy","myron","myrrh","mysel","mysid","nabak","nabla","nable","nabob","nacre","nacry","nadir","naggy","naght",
    "nagor","naiad","naily","nairy","naish","naive","naked","naker","nakoo","namaz","namda","namer","nancy","nandi","nandu",
    "nanes","nanga","nanny","napal","napoo","nappe","nappy","nares","naric","narky","narra","nasab","nasal","nasch","nasty",
    "nasus","natal","natch","nates","nathe","natty","naumk","naunt","naval","navar","navel","navet","navew","navvy","nawab",
    "nazim","nazir","neath","nebby","nebel","neddy","needs","needy","neeld","neele","neese","neeze","neffy","neger","negro",
    "negus","neigh","neist","nenta","neoza","neper","nerve","nervy","nesty","neter","netop","netty","neuma","neume","nevel",
    "never","nevoy","nevus","newel","newly","newsy","nexal","nexum","nexus","ngaio","ngapi","niata","nibby","niche","nicky",
    "nidal","nidge","nidor","nidus","niece","niepa","nieve","nific","nifle","nifty","night","nigre","nigua","nikau","nimbi",
    "ninny","ninon","ninth","nintu","ninut","niota","nippy","nisei","nisse","nisus","nitch","niter","nitid","niton","nitro",
    "nitty","nival","nixie","nizam","njave","nobby","noble","nobly","nodal","noddy","noded","nodus","nogal","nohow","noily",
    "noint","noise","noisy","nokta","nolle","nomad","nomic","nomos","nonce","nonda","nondo","nones","nonet","nonic","nonly",
    "nonya","nonyl","nooky","noose","nopal","noria","norie","norma","north","nosed","noser","nosey","notal","notan","notch",
    "noted","noter","notum","novel","novem","noway","nowed","nowel","noxal","noyau","nubby","nubia","nucal","nucha","nucin",
    "nudge","nullo","numda","numen","nummi","numud","nunch","nunky","nunni","nuque","nurly","nurse","nursy","nutty","nylon",
    "nymil","nymph","nyxis","oadal","oaken","oakum","oared","oaric","oasal","oases","oasis","oaten","obeah","obese","obley",
    "obole","occur","ocean","ocher","ochro","ocote","ocque","ocrea","octad","octan","octet","octic","octyl","ocuby","oddly",
    "odeon","odeum","odist","odium","odoom","oecus","oenin","offal","offer","often","ofter","oftly","ogeed","ogham","ogive",
    "ogler","ogmic","ohelo","ohmic","oiled","oiler","oisin","okapi","okrug","olden","older","oleic","olein","olena","olent",
    "oliva","olive","ology","olona","omber","omega","omina","omlah","oncia","oncin","onery","onion","onium","onkos","onlay",
    "onset","ontal","onymy","oolak","oolly","oopak","oopod","ootid","opera","ophic","opine","opium","optic","orach","orage",
    "orang","orant","orary","orate","orbed","orbic","orbit","orcin","order","oread","organ","orgia","orgic","orgue","oribi",
    "oriel","orlet","orlop","ormer","ornis","orris","orsel","ortet","ortho","oscin","osela","oshac","oside","osier","osmic",
    "osmin","osone","ossal","otary","otate","other","otkon","ottar","otter","ouabe","ought","oukia","oulap","ounce","ounds",
    "ouphe","ourie","outby","outdo","outed","outen","outer","outgo","outly","outre","ouzel","ovant","ovary","ovate","overt",
    "ovest","ovile","ovine","ovism","ovist","ovoid","ovolo","ovule","owght","owing","owler","owlet","owner","owsen","owser",
    "oxane","oxbow","oxboy","oxeye","oxfly","oxide","oxime","oxlip","oxman","oxter","ozena","ozone","paauw","pablo","pacay",
    "paced","pacer","paddy","padge","padle","padre","paean","paeon","pagan","pager","pagus","pahmi","paint","paisa","palar",
    "palas","palay","palch","palea","paled","paler","palet","palla","palli","pally","palma","palmo","palmy","palpi","palsy",
    "palus","panax","panda","pandy","paned","panel","pangi","panic","panne","panse","pansy","panto","pants","panty","paolo",
    "papal","papaw","paper","papey","pappi","pappy","papyr","parah","param","parao","parch","pardo","parel","paren","parer",
    "parge","pargo","parka","parky","parle","parly","parma","parol","parry","parse","parto","party","pasan","pasha","pashm",
    "pasmo","passe","passo","paste","pasty","pasul","patao","patas","patch","patel","paten","pater","pathy","patio","patly",
    "patta","patte","pattu","patty","pause","pauxi","pavan","paver","pavid","pavis","pawer","pawky","payed","payee","payer",
    "payor","peace","peach","peage","peaky","pearl","peart","peasy","peaty","peavy","pecan","pecht","pecky","pedal","pedee",
    "pedes","pedro","pedum","peele","peeoy","peepy","peery","peeve","peggy","peine","peise","pekan","pekin","pekoe","pelon",
    "pelta","penal","pence","penda","pengo","penis","penna","penni","penny","pensy","penta","peony","peppy","perch","perdu",
    "peres","peril","perit","perky","perle","perry","perse","perty","pesky","peste","petal","peter","petit","petre","petty",
    "peuhl","pewee","pewit","pfund","phage","phano","phare","phase","phasm","pheal","phene","pheon","phial","phoby","phoca",
    "phone","phono","phony","phose","photo","phyla","phyle","phyma","piaba","piano","pical","pichi","picky","picot","picra",
    "picul","pidan","piece","piend","piety","piezo","piggy","pigly","piked","pikel","piker","pikey","pikle","pilar","pilau",
    "pilch","piled","piler","piles","pilin","pilmy","pilon","pilot","pilum","pilus","pinax","pinch","pinda","pindy","pined",
    "piner","piney","pinic","pinky","pinna","pinny","pinon","pinta","pinte","pinto","pinyl","pious","pipal","piped","piper",
    "pipet","pipit","pippy","pique","pirny","pirol","pisay","pisco","pishu","pisky","pitau","pitch","pithy","piuri","pivot",
    "pixie","pizza","place","plack","plaga","plage","plaid","plain","plait","plane","plang","plank","plant","plash","plasm",
    "plass","plate","platy","plaud","playa","plaza","plead","pleat","plebe","plebs","pleck","pleny","pleon","plica","plied",
    "plier","plies","ploat","ploce","plock","plomb","plook","plote","plouk","plout","pluck","pluff","pluma","plumb","plume",
    "plump","plumy","plunk","plush","plyer","poach","pobby","poche","pocky","podal","poddy","podex","podge","podgy","poesy",
    "pogge","poggy","pohna","poilu","poind","point","poise","poked","poker","pokey","polar","poler","poley","polio","polis",
    "polka","polos","polyp","pombe","pombo","pomey","pomme","pommy","pompa","ponce","pondy","poney","ponga","ponja","ponto",
    "pooch","pooka","pooli","pooly","popal","poppa","poppy","poral","porch","pored","porer","porge","porgy","porky","poros",
    "porry","porta","porto","porty","porus","posca","poser","posey","posit","posse","potch","poter","potoo","potto","potty",
    "pouce","pouch","poulp","poult","pound","pouty","power","poyou","praam","prana","prank","prase","prate","prawn","praya",
    "preen","press","prest","prexy","price","prich","prick","pride","pridy","pried","prier","prill","prima","prime","primp",
    "primy","prine","prink","print","prion","prior","prism","priss","prius","privy","prize","proal","probe","proem","proke",
    "prone","prong","proof","props","prore","prose","proso","pross","prosy","prote","proto","prove","prowl","proxy","prude",
    "prune","prunt","pryer","pryse","psalm","pshaw","psoas","psora","psych","pubal","pubes","pubic","pubis","pucka","puddy",
    "pudge","pudgy","pudic","pudsy","puffy","puggi","puggy","pugil","puist","puker","puler","pulka","pulli","pulpy","pulse",
    "punch","punct","punga","pungi","punky","punta","punti","punto","punty","pupal","pupil","puppy","purdy","pured","puree",
    "purer","purga","purge","purre","purry","purse","pursy","pussy","putid","putty","pyche","pygal","pygmy","pylar","pylic",
    "pylon","pyoid","pyral","pyran","pyrex","pyxie","pyxis","quack","quaff","quail","quake","quaky","quale","qualm","quant",
    "quare","quark","quarl","quart","quash","quasi","quata","quauk","quave","quawk","qubba","queak","queal","quean","queen",
    "queer","queet","quegh","quell","queme","querl","quern","query","quest","queue","quica","quick","quiet","quiff","quila",
    "quill","quilt","quina","quink","quint","quipo","quipu","quira","quire","quirk","quirl","quirt","quite","quits","quoin",
    "quoit","quota","quote","quoth","raash","rabat","rabbi","rabic","rabid","racer","rache","racon","radar","radii","radio",
    "radix","radon","raffe","rafty","rager","raggy","rainy","raise","rajah","rakan","raker","rakit","rally","ralph","ramal",
    "ramed","ramet","ramex","ramie","rammy","ramus","ranal","rance","ranch","randy","range","rangy","ranid","ranny","ranty",
    "raper","raphe","rapic","rapid","rappe","rasen","raser","raspy","rasse","ratal","ratch","rated","ratel","rater","rathe",
    "ratio","ratti","ratty","ratwa","rauli","raupo","ravel","raven","raver","ravin","rayed","rayon","razee","razer","razoo",
    "razor","reaal","reach","react","readd","ready","realm","reamy","rearm","reask","reasy","reave","rebab","rebag","reban",
    "rebar","rebec","rebed","rebeg","rebel","rebia","rebid","rebob","rebop","rebox","rebud","rebus","rebut","rebuy","recap",
    "recce","recco","reccy","recon","recta","recti","recto","recur","recut","redan","reddy","redia","redig","redip","redly",
    "redox","redry","redub","redue","redux","redye","reedy","reefy","reeky","reese","reesk","reest","reeve","refan","refel",
    "refer","refit","refix","refly","regal","reges","reget","regia","regin","regle","regma","regur","rehoe","reify","reign",
    "reina","reins","relap","relax","relay","relet","relic","relot","reman","remap","remex","remit","remix","remop","renal",
    "reneg","renes","renet","renew","renin","renky","renne","reoil","reown","repay","repeg","repel","repen","repew","repic",
    "repin","reply","repot","reree","rerig","rerob","rerow","rerub","rerun","resaw","resay","resee","reset","resew","resex",
    "resin","resow","resty","resue","resun","resup","retag","retan","retax","retch","retem","rethe","retia","retie","retin",
    "retip","retry","reune","reuse","revel","rever","revet","revie","revue","rewax","rewed","rewet","rewin","rexen","rhamn",
    "rheen","rheic","rhein","rhema","rheme","rheum","rhine","rhino","rhomb","rhumb","rhyme","rhymy","riant","riata","ribat",
    "ribby","ricer","ricey","richt","ricin","riden","rider","ridge","ridgy","rifle","rifty","right","rigid","rigol","rigor",
    "riley","rilly","rimal","rimer","rimpi","rinch","rindy","ringe","ringy","rinka","rinse","ripal","ripen","riper","ripup",
    "risen","riser","rishi","risky","ritzy","rival","rivel","riven","river","rivet","riyal","roach","roast","rober","robin",
    "roble","robot","robur","rocky","rocta","rodeo","rodge","rogan","roger","rogue","rohan","rohob","rohun","roily","rokee",
    "roker","rokey","roleo","romal","rompu","rompy","ronco","ronde","rondo","roofy","rooky","roomy","roosa","roost","rooty",
    "roove","roper","ropes","roque","roral","roric","rorty","rosal","rosed","rosel","roset","rosin","rotal","rotan","rotch",
    "roter","rotge","rotor","rouge","rough","rougy","rouky","round","roupy","rouse","roust","route","routh","rover","rovet",
    "rowan","rowdy","rowed","rowel","rowen","rower","rowet","rowty","royal","royet","rozum","ruach","ruana","ruble","rubor",
    "ruche","rucky","rudas","ruddy","rudge","rufus","ruggy","ruing","ruler","rumal","rumbo","rumen","rumly","rummy","rumor",
    "runby","runch","runed","runer","runic","runny","runty","rupee","rupia","rupie","rural","rushy","rusky","rusma","rusot",
    "rusty","rutch","rutic","rutin","rutty","rutyl","ruvid","rybat","ryder","saber","sable","sably","sabot","sabra","sabzi",
    "sacra","sacro","sadhe","sadhu","sadic","sadly","safen","saggy","sagum","sahib","sahme","saiga","saily","saimy","saint",
    "sairy","sajou","saker","salad","salal","salar","salat","salay","salep","salic","salix","salle","sally","salma","salol",
    "salon","salpa","salse","salta","salty","salve","salvo","salvy","samaj","saman","samba","sambo","samel","samen","sammy",
    "sampi","sanai","sanct","sandy","sanga","sansi","sapan","sapek","sapid","sapin","saple","sapor","sappy","saraf","sargo",
    "sarif","sarip","sarna","sarod","saron","saros","sarpo","sarra","sarsa","sarus","sasan","sasin","sassy","satan","satin",
    "satyr","sauce","saucy","saugh","sauld","sault","sauna","saury","saute","sauty","sauve","saved","saver","savin","savor",
    "savoy","savvy","sawah","sawed","sawer","sayer","sayid","sazen","scads","scaff","scala","scald","scale","scall","scalp",
    "scalt","scaly","scamp","scant","scape","scare","scarf","scarn","scarp","scart","scary","scase","scaul","scaum","scaup",
    "scaur","scaut","scawd","scawl","sceat","scena","scend","scene","scent","schuh","schwa","scind","scion","sclaw","scler",
    "sclim","scoad","scobs","scoff","scoke","scolb","scold","scone","scoon","scoop","scoot","scopa","scope","scops","score",
    "scorn","scote","scouk","scoup","scour","scout","scove","scovy","scowl","scrab","scrae","scrag","scram","scran","scrap",
    "scrat","scraw","scray","scree","screw","scrim","scrin","scrip","scrob","scrod","scrog","scroo","scrow","scrub","scruf",
    "scrum","scudi","scudo","scuff","scuft","scull","sculp","scurf","scuse","scuta","scute","seamy","seary","seave","seavy",
    "sebum","secos","secre","sedan","sedge","sedgy","sedum","seech","seedy","seege","seely","seepy","segol","seine","seise",
    "seism","seity","seize","sekos","selah","sella","selly","selva","semen","semic","semis","senam","sence","senna","sensa",
    "sense","senso","sepad","sepal","sepia","sepic","sepoy","septa","sequa","serab","serai","seral","serau","seraw","sereh",
    "serge","serif","serin","serio","sermo","seron","serow","serra","serry","serta","serum","serut","serve","servo","sesma",
    "sesti","setae","setal","seton","setup","seugh","seven","sever","sewan","sewed","sewen","sewer","sexed","sexly","sexto",
    "sfoot","shack","shade","shady","shaft","shahi","shake","shako","shaku","shaky","shale","shall","shalt","shaly","shama",
    "shame","shank","shant","shape","shaps","shapy","shard","share","shark","sharn","sharp","shaul","shaup","shave","shawl",
    "shawm","shawy","sheaf","sheal","shear","sheat","sheen","sheep","sheer","sheet","sheik","shela","sheld","shelf","shell",
    "shend","sheng","sheth","sheva","shewa","shice","shide","shied","shiel","shier","shies","shift","shiko","shilf","shill",
    "shine","shiny","shire","shirk","shirl","shirr","shirt","shish","shisn","shita","shive","shivy","shoad","shoal","shoat",
    "shock","shode","shoer","shogi","shoji","shola","shole","shone","shood","shooi","shook","shool","shoop","shoor","shoot",
    "shore","shorn","short","shote","shott","shout","shove","shown","showy","shoya","shrab","shraf","shrag","shram","shrap",
    "shred","shree","shrew","shrip","shrog","shrub","shrug","shuba","shuck","shuff","shune","shunt","shure","shurf","shush",
    "shyer","shyly","sibby","sibyl","sicca","sided","sider","sides","sidhe","sidle","sidth","siege","sieve","sievy","sifac",
    "sight","sigil","sigla","sigma","sikar","siket","silen","silex","silky","silly","silty","silva","silyl","simal","simar",
    "sinal","since","sinew","singe","singh","sinky","sinus","siper","sipid","siren","sirih","siris","sirki","sirky","siroc",
    "sirup","sisal","sisel","sissy","sitao","sitar","sitch","sithe","sitio","situs","siver","sixer","sixte","sixth","sixty",
    "sizal","sizar","sized","sizer","sizes","skaff","skair","skart","skate","skean","skeed","skeeg","skeel","skeen","skeer",
    "skeet","skeif","skein","skelf","skell","skelp","skemp","skene","skere","skete","skewl","skewy","skice","skied","skier",
    "skies","skiff","skift","skill","skime","skimp","skink","skirl","skirp","skirr","skirt","skite","skive","skoal","skout",
    "skulk","skull","skulp","skunk","skuse","skyey","skyre","slack","slade","slain","slait","slake","slaky","slamp","slane",
    "slang","slank","slant","slape","slare","slart","slash","slate","slath","slaty","slaum","slave","sleck","sleek","sleep",
    "sleer","sleet","slent","slept","slete","slice","slich","slick","slide","slime","slimy","sline","sling","slink","slipe",
    "slirt","slish","slite","slive","sloan","slock","sloka","sloke","slone","slonk","sloom","sloop","slope","slops","slopy",
    "slorp","slosh","slote","sloth","slour","slows","sloyd","sluer","sluig","sluit","slump","slung","slunk","slurp","slush",
    "slyly","slype","smack","smaik","small","smalm","smalt","smarm","smart","smash","smaze","smear","smeek","smeer","smell",
    "smelt","smeth","smich","smile","smily","smirk","smite","smith","smock","smoke","smoky","smolt","smook","smoot","smore",
    "smote","smous","smout","smurr","smuse","smush","smyth","snack","snaff","snafu","snail","snake","snaky","snape","snaps",
    "snapy","snare","snark","snarl","snary","snath","snead","sneak","sneap","sneck","sneer","snell","snerp","snick","snide",
    "sniff","snift","snipe","snipy","snirl","snirt","snite","snivy","snock","snoek","snoga","snoke","snood","snook","snoop",
    "snoot","snore","snork","snort","snout","snowk","snowl","snowy","snuck","snuff","snurl","snurp","snurt","soaky","soapy",
    "soary","sobby","sober","socht","socii","socky","socle","soddy","sodic","sodio","sofar","softa","softy","soger","soget",
    "soggy","soily","soken","solan","solar","solay","soldi","soldo","solea","solen","soler","soles","solid","solio","solod",
    "solon","solum","solve","somal","somma","sonar","songy","sonic","sonly","sonny","sonsy","sooky","soord","sooth","sooty",
    "sophy","sopor","soppy","soral","sorda","soree","sorgo","sorra","sorry","sorty","sorus","sorva","sotie","sotol","sough",
    "souly","sound","soupy","soury","souse","south","sowan","sowar","sowel","sower","sowle","sowse","sowte","sozin","space",
    "spack","spacy","spade","spaer","spahi","spaid","spaik","spald","spale","spall","spalt","spane","spang","spank","spann",
    "spare","spark","sparm","spart","spary","spasm","spate","spave","spawn","speak","speal","spean","spear","spece","speck",
    "specs","speed","speel","speen","speer","spelk","spell","spelt","spend","spent","speos","sperm","spewy","spica","spice",
    "spick","spicy","spied","spiel","spier","spiff","spike","spiky","spile","spill","spilt","spina","spine","spink","spiny",
    "spire","spiro","spirt","spiry","spise","spite","spitz","splat","splay","splet","split","spode","spoil","spoke","spoky",
    "spole","spong","spoof","spook","spool","spoom","spoon","spoor","spoot","spore","sport","sposh","spout","sprad","sprag",
    "sprat","spray","spree","spret","sprew","sprig","sprit","sprod","sprue","sprug","spuke","spume","spumy","spung","spunk",
    "spurl","spurn","spurt","sputa","spyer","squab","squad","squam","squat","squaw","squib","squid","squin","squit","sruti",
    "staab","stack","stade","staff","stage","stagy","staia","staid","stain","staio","stair","stake","stale","stalk","stall",
    "stamp","stand","stane","stang","stank","stare","stark","starn","start","stary","stash","state","stauk","staun","staup",
    "stave","stawn","stays","stchi","stead","steak","steal","steam","stean","stech","steed","steek","steel","steen","steep",
    "steer","steid","stein","stela","stele","stell","stema","stend","steng","steno","stent","stept","stere","steri","sterk",
    "stern","stero","stert","stewy","stich","stick","stife","stiff","stile","still","stilt","stime","stimy","stine","sting",
    "stink","stint","stion","stipe","stirk","stirp","stite","stith","stive","stivy","stoat","stock","stoep","stoff","stoga",
    "stogy","stoic","stoke","stola","stole","stoma","stomp","stond","stone","stong","stony","stood","stoof","stook","stool",
    "stoon","stoop","stoot","stopa","stope","store","stork","storm","story","stosh","stoss","stoun","stoup","stour","stout",
    "stove","strad","strae","strag","stram","strap","straw","stray","stree","stret","strew","strey","stria","strid","strig",
    "strip","strit","strix","strom","strop","strow","stroy","strub","strue","strum","strut","struv","stubb","stuck","stude",
    "study","stuff","stull","stulm","stump","stung","stunk","stunt","stupa","stupe","stupp","sturk","sturt","stuss","styan",
    "styca","style","stylo","suade","suant","suave","subah","suber","succi","sucre","suddy","sudsy","suede","suety","sugan",
    "sugar","suine","suing","suint","suist","suite","suity","sulea","sulfa","sulka","sulky","sulla","sully","sumac","sumph",
    "sunny","sunup","super","surah","sural","surat","sures","surfy","surge","surgy","surly","surma","surra","sutor","sutra",
    "swack","swage","swain","swale","swami","swamp","swang","swank","swape","sward","sware","swarf","swarm","swart","swash",
    "swath","sweal","swear","sweat","sweep","sweer","sweet","swego","swell","swelp","swelt","swept","swerd","swick","swift",
    "swile","swill","swimy","swine","swing","swink","swipe","swipy","swird","swire","swirl","swish","swiss","swith","swoon",
    "swoop","sword","swore","sworn","swosh","swung","swure","sycee","sylid","sylph","sylva","synch","synod","syrma","syrup",
    "tabby","tabes","tabet","tabic","tabid","tabla","table","tabog","taboo","tabor","tabut","tache","tacit","tacky","tacso",
    "taffy","tafia","taggy","tagua","tahil","tahin","tahua","taich","taiga","taily","taint","taipo","tairn","taise","takar",
    "taken","taker","takin","takyr","talak","talao","talar","taled","taler","tales","talis","talky","tally","talma","talon",
    "taluk","talus","tamas","tambo","tamer","tamis","tammy","tanak","tanan","tanga","tangi","tango","tangs","tangy","tanha",
    "tania","tanka","tanoa","tansy","tanti","tanzy","tapas","tapen","taper","tapet","tapia","tapir","tapis","tapoa","tappa",
    "tapul","taqua","taraf","tarau","tardy","tarea","tarfa","targe","tarie","tarin","taroc","tarok","tarot","tarri","tarry",
    "tarse","tarsi","tarve","tasco","tasse","taste","tasty","tater","tatie","tatou","tatta","tatty","taula","taunt","taupe",
    "taupo","taver","tawer","tawie","tawny","tawpi","tawse","taxed","taxer","taxis","taxon","taxor","tayer","tayir","tayra",
    "tazia","tchai","teach","teaer","teaey","teart","teary","tease","teasy","teaty","teave","teaze","techy","tecon","tecum",
    "tedge","teems","teens","teeny","teest","teeth","teety","tegua","teind","tejon","tekke","tekya","telar","telic","tellt",
    "telyn","teman","tembe","temin","tempi","tempo","tempt","temse","tenai","tench","tenet","tengu","tenio","tenne","tenon",
    "tenor","tense","tenth","tenty","tepal","tepee","tepid","tepor","terap","teras","terek","tereu","terma","terna","terne",
    "terry","terse","terzo","testa","teste","testy","tetch","tetel","tetra","tewel","tewer","tewit","tewly","thack","thana",
    "thane","thank","tharf","tharm","thatn","thats","thave","thawn","thawy","theah","theat","theca","theek","theer","theet",
    "theft","thegn","their","thema","theme","theow","there","therm","these","theta","thewy","thick","thief","thigh","thilk",
    "thill","thine","thing","think","thiol","third","thirl","thirt","thisn","thoft","thoke","thole","tholi","thone","thong",
    "thoom","thore","thorn","thoro","thorp","thort","those","thowt","thram","thrap","thraw","three","threw","thrip","throb",
    "throe","throu","throw","thrum","thruv","thulr","thumb","thump","thung","thuoc","thurl","thurm","thurt","thyme","thymy",
    "tiang","tiara","tibby","tibet","tibey","tibia","tical","ticca","ticer","ticky","ticul","tidal","tiddy","tided","tiffy",
    "tiger","tight","tikka","tikor","tikur","tilde","tiled","tiler","tilly","tilth","tilty","timar","timbe","timbo","timed",
    "timer","times","timid","timon","timor","tinct","tinea","tined","tinge","tingi","tinny","tinta","tinty","tiple","tippy",
    "tipsy","tipup","tired","tirer","tirma","tirve","tisar","titar","titer","tithe","title","titre","titty","tiver","tizzy",
    "tlaco","tmema","toady","toast","today","toddy","toffy","togue","toher","toise","toity","tokay","token","tolan","toldo",
    "tolly","tolyl","toman","tombe","tomin","tommy","tonal","toned","toner","tonga","tongs","tonic","tonus","toosh","tooth",
    "topaz","topee","toper","topia","topic","toppy","topsl","toque","torah","toral","toran","torch","tored","toric","torii",
    "torma","torse","torsk","torso","torta","torus","torve","toshy","tossy","total","totem","toter","totty","totum","touch",
    "tough","tould","tourn","touse","tousy","tovar","towai","towan","towel","tower","towny","toxic","toxin","toxon","toyer",
    "toyon","tozee","tozer","trace","track","tract","trade","trady","tragi","traik","trail","train","trait","trama","trame",
    "tramp","trank","trant","traps","trash","trass","trasy","trave","trawl","tread","treat","treed","treen","treey","trend",
    "tress","trest","trews","triad","trial","tribe","trica","trice","trick","tried","trier","trifa","trike","trill","trine",
    "trink","trior","tripe","tripy","trist","trite","troat","troca","trock","troco","trode","troft","trogs","troke","troll",
    "tromp","trona","tronc","trone","troop","troot","trope","troth","trout","trove","trubu","truce","truck","truer","truff",
    "trull","truly","trump","trunk","trush","truss","trust","truth","tryma","trypa","tryst","tsere","tsine","tsuba","tsubo",
    "tuarn","tuart","tuath","tubae","tubal","tubar","tubba","tubby","tuber","tubig","tubik","tucky","tucum","tudel","tufan",
    "tufty","tugui","tuism","tukra","tulip","tulle","tulsi","tumid","tummy","tumor","tunca","tuned","tuner","tungo","tunic",
    "tunna","tunny","tupek","tupik","tuque","turbo","turco","turfy","turgy","turio","turma","turns","turps","turse","turus",
    "tusky","tutee","tutin","tutly","tutor","tutti","tutty","twain","twale","twalt","twang","twank","twant","tweag","tweak",
    "tweed","tweeg","tweel","tween","tweet","tweil","twere","twerp","twice","twick","twill","twilt","twine","twink","twiny",
    "twire","twirk","twirl","twist","twite","twixt","tydie","tying","tyken","tylus","typal","typer","typic","tyste","uayeb",
    "uckia","udasi","udder","udell","uhlan","uhllo","uinal","ukase","ulcer","ulema","uller","ulmic","ulmin","ulnad","ulnae",
    "ulnar","uloid","ultra","uluhi","ululu","umbel","umber","umble","umbra","umiak","umiri","umpty","unact","unadd","unamo",
    "unapt","unark","unarm","unary","unbag","unbar","unbay","unbed","unbet","unbid","unbit","unbog","unbow","unbox","unboy",
    "unbud","uncap","uncia","uncle","uncoy","uncus","uncut","undam","unden","under","undid","undig","undim","undog","undon",
    "undry","undub","undue","undug","undye","uneye","unfar","unfed","unfew","unfit","unfix","unfur","ungag","unget","ungka",
    "ungod","ungot","ungum","unhad","unhap","unhat","unhex","unhid","unhit","unhot","uniat","unice","unify","uninn","union",
    "unite","unity","unjam","unked","unken","unket","unkey","unkid","unkin","unlap","unlaw","unlay","unled","unlet","unlid",
    "unlie","unlit","unmad","unman","unmet","unmew","unmix","unnew","unode","unoil","unold","unorn","unown","unpeg","unpen",
    "unpin","unpot","unput","unram","unray","unred","unrid","unrig","unrip","unrow","unrun","unsad","unsay","unsee","unset",
    "unsew","unsex","unshy","unsin","unsly","unson","unsty","unsun","untap","untar","untax","untie","until","untin","untop",
    "unurn","unuse","unwan","unwax","unweb","unwed","unwet","unwig","unwon","unzen","uparm","upbar","upbay","upbid","upbuy",
    "upcry","upcut","updry","upeat","upend","upfly","upget","upher","upjet","uplay","upleg","upmix","upper","uppop","uprid",
    "uprip","uprun","upset","upsey","upsit","upsun","upsup","uptie","upwax","upway","urali","urare","urari","urase","urate",
    "urban","urbic","urdee","ureal","uredo","ureic","ureid","urent","urger","urial","urine","urite","urlar","urled","urman",
    "urnae","urnal","ursal","urson","ursuk","urubu","urucu","usage","usara","usent","usher","usnea","usnic","usque","uster",
    "usual","usure","usurp","usury","utchy","utees","uteri","utick","utile","utrum","utsuk","utter","uvate","uveal","uviol",
    "uvito","uvrou","uvula","uvver","uzara","vache","vacoa","vagal","vagas","vague","vagus","vaire","vairy","vajra","vakia",
    "vakil","valet","valid","valor","valse","value","valva","valve","valyl","vaned","vapid","vapor","varan","vardy","varec",
    "varix","varna","varus","varve","vasal","vasty","vatic","vaudy","vault","vaunt","vealy","vedro","veery","veily","veiny",
    "velal","velar","veldt","velic","velte","velum","venal","venie","venin","venom","venue","verby","verek","verge","vergi",
    "verre","verse","verso","verst","verve","vetch","veuve","vexed","vexer","vexil","viand","vibex","vibix","vicar","video",
    "vidry","vidya","viewy","vifda","vigia","vigil","vigor","vijao","villa","ville","vimen","vinal","vinea","vined","viner",
    "vinic","vinny","vinta","vinyl","viola","viper","viral","vireo","virga","virid","viron","virtu","virus","visie","visit",
    "visne","vison","visor","vista","visto","vital","vitta","viuva","vivax","viver","vives","vivid","vixen","vocal","vodka",
    "vogue","voice","voile","volar","volet","volva","vomer","vomit","votal","voter","vouch","vouge","vowed","vowel","vower",
    "vraic","vuggy","vulva","vying","waapa","wabby","wacke","wacky","waddy","wader","wadna","wafer","wafty","waged","wager",
    "wages","waggy","wagon","wahoo","waily","waird","waise","waist","waive","wakan","waken","waker","wakes","wakif","wakon",
    "waled","waler","wally","walsh","walth","waltz","wamel","wamus","wandy","waned","wanga","wanle","wanly","wanny","wanty",
    "warch","warly","warnt","warse","warst","warth","warty","warve","wasel","washy","wasnt","waspy","waste","wasty","watap",
    "watch","water","wauch","waugh","wauns","wauve","waved","waver","wavey","wawah","waxen","waxer","weaky","weald","weary",
    "weave","webby","weber","wecht","wedge","wedgy","weeda","weedy","weeny","weeps","weepy","weesh","weeze","wefty","weigh",
    "weird","weism","wekau","welly","welsh","wench","wende","wenny","weste","westy","wetly","wevet","whack","whale","whalm",
    "whalp","whaly","whame","whamp","whand","whang","whank","whare","wharf","wharl","wharp","whart","whase","whata","whats",
    "whauk","whaup","whaur","wheal","wheam","wheat","wheel","wheem","wheen","wheep","wheer","wheft","whein","wheki","whelk",
    "whelm","whelp","where","whewl","whewt","whiba","which","whick","whiff","whift","while","whilk","whill","whils","whine",
    "whing","whiny","whipt","whirl","whish","whisk","whisp","whist","white","whits","whity","whole","whone","whoof","whoop",
    "whore","whorl","whort","whose","whuff","whulk","whush","whute","wicht","wicky","widdy","widen","widow","width","wield",
    "wifie","wigan","wiggy","wight","wilga","willy","wince","winch","windy","wined","winer","wingy","winly","winna","winze",
    "wiper","wired","wirer","wirra","wisen","wiser","wisha","wisht","wispy","wisse","wiste","witan","witch","withe","withy",
    "witty","wiver","wizen","wloka","woady","woald","wodge","wodgy","woibe","wokas","woldy","wolve","woman","womby","wonga",
    "wonky","wonna","woody","wooer","woofy","woold","woons","woosh","wootz","woozy","wordy","works","worky","world","wormy",
    "worry","worse","worst","worth","wouch","wough","would","wound","woven","wrack","wramp","wrang","wrath","wrawl","wreak",
    "wreat","wreck","wrest","wrick","wride","wried","wrier","wring","wrist","write","writh","wrive","wroke","wrong","wrote",
    "wroth","wrung","wryly","wudge","wunna","wuzzy","wyson","wyver","xebec","xenia","xenon","xenyl","xeric","xoana","xurel",
    "xylan","xylem","xylic","xylol","xylon","xylyl","xyrid","xysti","yabbi","yabby","yacal","yacca","yacht","yagua","yahan",
    "yahoo","yaird","yakin","yakka","yalla","yamen","yampa","yamph","yanky","yaply","yapok","yappy","yarak","yaray","yarke",
    "yarly","yarth","yauld","yawny","yeara","yeard","yearn","yeast","yerba","yerga","yerth","yesso","yesty","yeuky","yeven",
    "yezzy","ygapo","yield","yince","yinst","yirth","yocco","yodel","yogin","yoick","yojan","yokel","yoker","yolky","yomer",
    "youff","young","yourn","yours","youse","youth","youve","youze","yoven","yowie","yucca","yucky","yulan","yummy","yurta",
    "zabra","zabti","zaman","zambo","zante","zanze","zapas","zayat","zayin","zebra","zebub","zeism","zeist","zemmi","zemni",
    "zerda","zesty","ziara","zibet","ziega","ziffs","zihar","zimbi","zimme","zimmi","zinco","zippy","zirai","zloty","zocco",
    "zoeal","zogan","zoism","zoist","zokor","zolle","zombi","zonal","zonar","zoned","zonic","zooid","zooks","zoons","zoril",
    "zorro","zowie","zudda","zygal","zygon","zymic","zymin"
    ]
# fmt: on


def contains_all(word, s):
    """Return True if 'word' contains all characters in 's'"""
    for c in s:
        if c not in word:
            return False
    return True


def contains_any(word, s):
    """Return True if 'word' contains any characters in 's'"""
    for c in s:
        if c in word:
            return True
    return False


def count_str(wlist):
    """Make English real good"""
    s = f"{len(wlist)} "
    s += "word matches" if len(wlist) == 1 else "words match"
    return s


# get arguments
parser = argparse.ArgumentParser(
    description="Helper for figuring out what words to guess with Wordle.",
    epilog=textwrap.dedent(
        """\
        Examples:
           python words.py .Ei.. --no=cdu
                Look for words where 'E' is in position 2, 'i' is anywhere
                but position 3, and letters 'c', 'd', 'u' do not exist

           python words.py LEyfa --no=x
                Look for words that begin with 'LE', have 'yfa' in some order
                but not in the positions shown, and do not contain 'x' anywhere
           
           python words.py .R..n,..I..,....r
                Uses three patterns to describe the following:
                    Word contains 'RI' in positions 2 and 3.
                    Word has an 'r' and an 'n', but neither is in position 5
                This could have been compressed to two patterns:
                    .RI..n,....r

        Scenario:
            Let's say the word to guess is GLOVE and you guess 'crate' first.
            You'll get Wordle's response that the 'e'' is correct. If you now want
            to see what words remain, you would run this:
            
            python words.py ....E --no=crat

            You'll get over 300 possible words. But you also find out that the top letters used in
            those 300+ words are:
            o:143
            i:141
            l:121
            s:116
            n:92

            So your next guess should use as many of those letters as possible. How do you find a good word?

            python words.py --yes=oils

            This says to tell you all 5 letter words that contain all of 'o', 'i', 'l', 's' in any order.
            From that list, you pick "solid".

            Now Wordle tells you that the 'l' and 'o' are used but in the wrong place. So you run again:

            python words.py .ol.E --no=cratsid

            You're asking for words that end in 'E' and have 'o' and 'l' somewhere in them not at the positions
            shown. Now we're down to 10 words. Keep going until you solve it!

           """
    ),
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    "patterns",
    nargs="?",
    default=".....",
    help=textwrap.dedent(
        """\
        Comma-separated list of patterns. Capital letter means correct in current position.
        Lower-case letter means correct but not in current position.
           """
    ),
)
parser.add_argument("--yes", "-y", default="", help="specify letters that must be included")
parser.add_argument("--no", "-n", default="", help="specify letters that must not be included")
args = parser.parse_args()
wlist = w5list[:]

# reduce 5-letter word list to those that match args.patterns
print(f"Processing patterns='{args.patterns}' yes='{args.yes}' no='{args.no}'")
print(f"    initial word count={len(wlist)}\n")
for pattern in args.patterns.split(","):
    print(f"Processing pattern {pattern}")
    for i, c in enumerate(pattern):
        if c == ".":
            continue
        if c in string.ascii_lowercase:
            # the lower case letters must exist, so keep only words
            # that have them
            print(f"    keeping words that contain '{c}'")
            wlist = [w for w in wlist if c in w]
            print(f"        count={len(wlist)}")
            # make sure the remaining words don't have those
            # characters in the invalid positions
            nopat = "." * i + c + "." * (4 - i)
            print(f"    excluding words that match '{nopat}'")
            wlist = [w for w in wlist if not re.match(nopat, w)]
            print(f"        count={len(wlist)}")
        else:
            # keep words that have characters matching the
            # uppercase letters
            c = c.lower()
            yespat = "." * i + c + "." * (4 - i)
            print(f"    keeping words that match '{yespat}'")
            wlist = [w for w in wlist if re.match(yespat, w)]
            print(f"        count={len(wlist)}")
    print()

# reduce word list to those that exclude the 'no' list
if len(args.no):
    wlist = [w for w in wlist if not contains_any(w, args.no)]
    print(f"{count_str(wlist)} nothing in NO list '{args.no}'")

# reduce word list to those that contain all characters in the 'yes' list
if len(args.yes):
    wlist = [w for w in wlist if contains_all(w, args.yes)]
    print(f"{count_str(wlist)} everything in YES list '{args.yes}'")

# results
print(f"\n{count_str(wlist)} requirements:")
wrapper = textwrap.TextWrapper(width=90)
if len(wlist) <= 100:
    print("\n".join(wrapper.wrap(" ".join(wlist))))
    print()
else:
    print("    (too many words to print)")

# show counts of characters that have not been specified in the patterns
# or in the 'yes' list
if len(wlist) > 1:
    print("Counts of unspecified letters (max 10)")
    chardict = {c: 0 for c in string.ascii_lowercase if c not in args.patterns.lower() + args.yes}
    for c in chardict:
        for w in wlist:
            if c in w:
                chardict[c] += 1
    for i, (k, v) in enumerate(reversed(sorted(chardict.items(), key=lambda item: item[1]))):
        if v > 0 and i < 10:
            print(f"{k}:{v}")
