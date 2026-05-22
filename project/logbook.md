## 23 April 2119
Aanmaken van het project folder inclusief beginnen met de tutorial te kijken.
Vandaag ga ik niet veel kunnen verwezelijken was een lange dag op het werk van 12 uur.

## 23 April 2230
Mijn ogen vallen dicht terwijl ik de tutorial aan het kijken ben.
Ik heb toch wel een uurtje uur aandachtig kunnen kijken maar de rest zal voor morgen zijn jammer genoeg.
de concepten snap ik wel goed tot nu toe.

## 25 April 2230
Ik heb de volledige tutorial kunnen doornemen en ga nu beginnen met de analyse voor wat ik zelf nog wil toevoegen aan het blackjack project.

## 26 April 1230
De analyse van wat ik allemaal zou willen aanpassen is ongeveer gelukt maar jammer genoeg niet meer gisteren avond. 
Vandaag heb ik er toch wel een uurtje of 2 kunnen over nadenken en heb ongeveer wel een idee van wat ik wil bereiken.
Wel weet ik niet zo goed hoe ik de tijd ga kunnen inschatten maar het zal wel lukken.
1.  Achtergrond aanpassen naar misschien zo wat Casino achtige kleuren
2.  De kaarten tonen geen kleuren dus kaartkleuren en de echte symbolen erop toevoegen
3.  Welkomscherm misschien maken voor het spel zelf
4.  De "New Hand" misschien niet over al de rest laten gaan maar dat dit de enigste optie is wat er overblijft als er gewonnen/verloren is
5.  Simpele geluiden toevoegen 
Eenmaal ik dit heb toegevoegd kijk ik hoeveel tijd ik nog zou overhebben.

## 26 April 22:30
Vandaag ben ik dan begonnen aan de eerste aanpassing.
Ik wilde de achtergrondkleur veranderen van zwart naar dan het casino groen omdat ik het meer als een echte casinotafel er wil laten uitzien.
Eerst moest ik opzoeken hoe je de RGB kleur kon instellen in de pygame want was het al beetje vergeten na het filmpje. Maar via google heb ik het dan snel gevonden. Het is gewoon een tuple (x,x,x) dat je kan gebruiken. Alsook heeft het mij even geduurd om het casino groen te vinden maar uiteindelijk heb ik het gevonden door middel van de Color Contrast analyzer die ik nog onthouden had van Front End Development.
Alsook heb ik een titel BLACKJACK bovenaan geplaats met een gouden kleur als het spel nog niet begonnen is. Ik vind het er al veel beter uitzien. 
Ik had wel gedacht dat het makkelijk zou zijn deze aanpassingen en dat klopt ook maar omwille van de kleurwaarde en het opzoekwerk heb ik er toch wel wat tijd ingestoken.

Volgende stap ga ik proberen de kaarten te kleuren en de symbolen toe te voegen.

## 27 April 22:31
Mijn vorige commit was niet echt gelukt maar bon.
Dit is tot nu toe mijn moeilijkste stap, omwille van het vele refractoren van de code voor dit te laten slagen.
Ik wilde de kaartkleuren toevoegen maar wist eerst niet goed hoe ik dit moest aan pakken. 
Vervolgens besloot ik het als een tuple op te slaan maar dan was de calculate_score functie weer kapot omdat die de kaarten met strings vergelijkt.
De hand[i] moest ik dan vervangen met hand[i][0] op verschillende plaatsen dus heb ik uiteindelijk op veel gewoon opnieuw beginnen typen.
Na veel bloed zweet,tranen en een uur of 3 later zijn de kleuren correct en werkt het spel effectief terug wat een geluk...

Maar nu zit ik met het probleem dat de symbolen niet correct geladen worden alsook dat het niet zo staat zoals ik het zelf wil.
Dus dit voelt aan als ene stap achteruit jammer genoeg, maar met nog wat tijd en energie denk ik het wel te kunnen oplossen. 
De tuples die ik gemaakt heb werken goed maar ik moet echt uitzoeken waar het probleem nu zit in verband met de symbolen en de locaties.

## 27 April 22:51
Ik heb gevonden waarom mijn symbolen niet wilde laden en het font was uiteraard de oorzaak.
Gelukkig met een ander font te maken voor mijn symbolen en deze toe te passen op de kaarten zorgen er voor dat de symbolen nu correct zijn.

Ik had blijkbaar ook de positionering niet goed gedaan vorige keer van waar de kaart value & kaart suits terechtkomen.
Dus deze heb ik nu wel goed gezet zodanig dat het linksboven en rechtonder is.
Toch wel wat frustrened allemaal als je al wat moe bent :) 

Morgen moet ik er weer om 0500 opstaan dus ik denk dat ik het voor vandaag voor bekeken houdt.
Tijdens de dag als de kinderen op school zijn ga ik proberen om misschien het toch nog iets mooier te laten uitkomen of wel te beginnen aan het welkomscherm.
ik moet mijzelf altijd zeggen dat ik het niet te perfectionistisch om de mm moet maken.


# 28 April 09:00
Sinds deze morgen toch nog wat zitten aanpassen voor de symbolen en values beter te laten uitkomen.
Uiteindelijk heeft deze loophole mij toch ook weer wat tijd gekost om op te lossen zodanig dat ze goed uitkomen.
Alsook de knoppen zelf aanpassen is was toch even zoeken :D 
Maar voor mij is dit momenteel goed zo.
Nu kan ik beginnen met het welkomscherm aan te passen 

# 28 April 11:00
Ik heb zojuist het welkomstscherm gemaakt. Ik heb een variabele game_started aangemaakt die False is bij het starten. Zolang False toont het scherm een welkomstpagina met de naam van het spel. Ik liep even vast omdat ik de event-afhandeling voor het welkomstscherm apart moest doen van de rest van het spel, anders kon ik niet meer afsluiten. Uiteindelijk opgelost door een if/else structuur.
Het was ook wel zoeken naar de pygame syntax voor dit te verwezelijken
Nu kan er ook met een spatiebalk verder gegaan worden
Was even zoeken weer. MAar voorlopig vind ik het zo ok.
Nu ga ik proberen het new hand knop te fixen

# 28 April 22:30
Ik heb de "New Hand" knop nu gefixed zodat die bovenaan verschijnt als het spel gedaan is, en de "Hit Me" en "Stand" knoppen dan verdwijnen.
Hierdoor krijgt de speler na een gewonnen of verloren hand enkel de optie om opnieuw te spelen en maakt het duidelijk zichtbaar dat het spel voorbij is.

Het aanpassen van de draw_game functie was even puzzelen. Ik moest de logica opsplitsen in drie gevallen: spel niet actief, spel gedaan (resultaat), en spel actief. Maar daarna merkte ik dat de win/verlies tekst plots niet meer zichtbaar was. Het bleek dat ik die tekst gewoon niet meer tekende in het nieuwe geval, dus die was gewoon verdwenen.

Na even zoeken heb ik de results lijst terug opgeroepen in het juiste blok en de tekst op de correcte positie gezet. Achteraf simpel maar het heeft mij toch even gekost om te vinden waar het probleem zat.

Soms denk ik dat iets niet lang gaat duren maar dan zit ge er toch weer een paar uur mee te "kloten" om het mooi te verwoorden :D

Morgen na mijn werk ga ik proberen geluiden toe te voegen maar ik ben nog niet zeker wat ik exact wil doen.
Ik denk misschien dat ik het scherm iets groter ga maken en dan rechts een paar knoppen bij zet met specifieke muziek ofzo.
Moet er nog een nachtje over slapen :)

# 29 April 23:45
Vandaag stond muziek op het programma. Wat leek op een simpele taak bleek opnieuw toch niet zo simpel te zijn voor mij ...

Om te beginnen probeerde ik een Qmusic radiostream URL rechtstreeks in pygame.mixer.music.load() te steken. Pygame ondersteunt HTTP-streams echter niet blijkbaar. Bij het klikken op de knop crashte het volledige programma met exit code 1.
Jammer genoeg moest ik dus van radiostreams afzien.

Tweede poging was simpeler: één knop om muziek aan/uit te zetten met een lokaal mp3-bestand.
pygame.mixer.music kan enkel lokale bestanden aan blijkbaar(mp3, wav, ogg) dus besliste ik om lokale bestanden te gebruiken.

Ik wilde de mp3-bestanden netjes in een submap Music/ zetten. Het pad 'Music/song.mp3' werkte niet omdat het script opgestart wordt vanuit de project map, niet vanuit de pygameBlackjack-main map. 
mijn Oplossing was om dan maar : os.chdir(os.path.dirname(os.path.abspath(__file__))) bovenaan het script zodat de werkmap altijd de map van het script zelf is. Dit loste het probleem op.

Als eindresultaat na al mijn "gekloot" heb ik nu een playlist van nummers in de map Music/, drie knoppen (AAN/UIT, vorig, volgend) en de naam van het huidige nummer wordt getoond.

Toen ik wat verder aan het kijken was vond ik toch wel dat mijn achtergrond met RGB kleuren op niet veel trok dus heb ik via AI een achtergrond 900x900 laten maken die wel in mijn project paste.
Deze achtergrondafbeelding heb ik dan toegevoegd via pygame.image.load.

Ik heb zelf ook nog echt veel zitten spelen met die knoppen om ze exact mooi af te lijnen. 
Maar die milimeters zullen wel niet uitmaken vermoed ik.

Al met al weer een avond waarbij "simpel" toch niet zo simpel bleek, en uiteindelijk toch weer 4 uur prullen werd maar het werkt nu :)
Dat is het belangrijkste

Morgen ga ik misschien nog wat kleine aanpassingen doen maar ik zit zo goed als aan mijn 20 uur.
Ik ga misschien de feedback afwachten daarna om te kijken wat de docent graag nog van veranderingen ziet. 


# 30 April 22:51
Om eerlijk te zijn had ik vandaag niet veel zin om aan het project te werken want ik had echt een héél vermoeiende dag op het werk en had gisteren maar 3 uur geslapen.

Maar ik wilde er toch nog graag wat werk insteken en een volume slider toevoegen zodat je het geluid omhoog en omlaag kan draaien voor mensen die misschien wat sensitief zijn.

Ik dacht eerst dat dit simpel zou zijn maar er waren toch wat kleine uitdagingen. 
Het slepen van de slider moest ik bijhouden via een slider_dragging variabele. 
Bij MOUSEBUTTONDOWN zet ik die op True als je op de slider klikt, bij MOUSEMOTION pas ik het volume aan zolang je sleept, en bij MOUSEBUTTONUP laat ik de slider los. 
Het volume pas ik dan toe op zowel pygame.mixer.music als de twee geluidseffecten new_hand_sound en take_card_sound.

Daarna heb ik ook wat tijd gestoken in de positionering van de slider en de vorige/volgende knoppen zodanig dat alles netjes onder elkaar staat en niet over de tekst valt. Dit was meer trial and error met de coördinaten maar uiteindelijk ziet het er goed uit.

Ik ga het hierbij laten voor de moment en misschien toch de feedback vragen van de docent wat hij nog graag zou zien wat ik extra doe.
Ik denk dat ik nooit tevreden ga zijn en altijd uitbreidingen wil bijvoegen maar ik ga me moeten aan de uur restrictie houden.

# 02 Mei 18:15
Ik heb zojuist een mail gestuurd naar de lector voor feedback te vragen over het project.
Het was niet zo eenvoudig om te beslissen waar ik specifiek feedback op wou, want ik ben zelf niet altijd even zeker of ik de juiste keuzes gemaakt heb. 

Uiteindelijk heb ik gevraagd of hij vindt dat ik de juiste zaken heb aangepakt binnen de beschikbare tijd.
Alsook of er dingen zijn die hij liever anders had gezien. 

Ik ben benieuwd naar zijn antwoord, want ik merk dat ik snel geneigd ben om kleine details te blijven perfectioneren in plaats van grotere structurele keuzes in vraag te stellen.

De feedback zal me hopelijk wat meer richting geven over wat echt telt.

# 19 Mei 10:30
De feedback van de docent is binnen en ik heb die even rustig doorgenomen. Hij heeft zijn opmerkingen rechtstreeks in de code gezet via # [dn]commentaren, wat eigenlijk wel handig is want zo zie ik meteen exact waar het over gaat.

De pygame.transform.scale die ik gebruik om de achtergrond te schalen had ik inderdaad gewoon beter eenmalig gedaan in Paint of iets dergelijks. Dat is een stuk efficiënter dan dat elke keer opnieuw te laten berekenen bij het laden.
Uitendelijk had ik ok op het einde mijn Size window iets groter gemaakt en had ik daarvoor voor deze oplossing gekozen.

Voor de kaartsymbolen heb ik wel bewust gekozen voor de echte tekens (♠, ♥, ♦, ♣) omdat ik het visueel echt aantrekkelijk wou maken, gewoon letters leek mij iets te simpel voor het project. 
Maar hierdoor heb ik wel dan weer een aparte module moeten opzoeken die die symbolen uberhaupt kon weergeven want het standaard font kon er niet mee overweg. 
Daan de docent geeft aan dat S, H, D, C veel praktischer is en dat je dan via een dictionary de vertaling naar het echte symbool kan maken. Dat is eerlijk gezegd een stuk slimmer, want nu is het inderdaad wat omslachtig om die symbolen telkens terug te vinden als je iets wil aanpassen.
Alsook zoals hij vermeld kan dit veel problemen geven op later niveau.
Zeker iets om mee te nemen.

De variabelenamen heeft hij zeker en vast ook gelijk. en zijn ook een belangrijk punt van aandacht. outcome, add_score, results...
Daan merkt terecht op dat die niet veel zeggen als je de code leest zonder context. game_outcome of hand_outcome is al meteen veel duidelijker, en result_strings zegt ook beter wat die lijst eigenlijk doet. 
Kleine aanpassingen maar het maakt wel een verschil voor leesbaarheid.

Alsook moet ik zeker en vast bij bepaalde dingen extra inline commentaar voorzien toekomstgericht.

Dan de herhaling van getallen zoals 70 en 150 in draw_cards. 
De reden dat ik die niet als variabelen heb gezet is is eigenlijk omdat ik constant millimeter per millimeter te sleutelen zat aan posities om de tekst goed te laten uitkomen op de kaarten, en op dat moment leek het makkelijker om gewoon de getal zelf aan te passen.
Maar hij heeft gelijk dat je daarmee op meerdere plaatsen tegelijk moet aanpassen en dat je er snel eentje mist (wat ook héél veel is gebeurd :)).
Het is inderdaad beter één variabele bovenaan aanpassen dan vijf keer hetzelfde getal door de code te gaan zoeken.

Maar ik denk dat het beter is om dan dit op het einde te doen eenmaal de layout volledig in orde is.
Zeker als beginnende developer zoals mijzelf.

Hij vermelde ook dat in draw_game staat inderdaad ook een behoorlijk lange lap code aan elkaar zonder veel structuur. 
Wat witregels en commentaar zouden het inderdaad al een stuk overzichtelijker maken.
En in check_endgame gebruikte ik result == 2 zonder dat duidelijk is wat 2 betekent. 
Een variabele zoals game_won = 2 zou dat meteen verduidelijken.

Al met al gaat de feedback vooral over leesbaarheid en onderhoudbaarheid, niet echt over fouten.
Het spel werkt maar de code is soms wat moeilijk te volgen voor iemand anders. 
Dat is iets waar ik de volgende keer al vroeger in het proces bewuster op ga moeten letten en beter integreren.

Ik vond het wel goed om eens feedback te krijgen op een project dat ik heb gemaakt.