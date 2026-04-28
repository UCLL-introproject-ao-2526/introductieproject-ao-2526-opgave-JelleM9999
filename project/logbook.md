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
