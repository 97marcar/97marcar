Tycker att det har gått bra att göra programmet, lite utmanande vilket är bra. 
Det som jag tyckte var mindre bra var tiden. Hade gärna haft mer tid, då hade jag kunna lägga till mer funktioner.

Gillar biblioteket Qt när jag utveckalt en bra grundkunskap i första kursen

Det ska inte finnas några stora buggar, jag ska ha fixat dem. 
Om man försöker nog mycket kanske man skulle hitta något då tiden för buggtest har varit kort.
 
Det finns saker i programmet som kan förbättras så det blir mer användarvänligt, t.ex. hur man väljer en tillvald film.
Just nu väljer man först format(Blueray, DVD eller VHS) i en dropdownbox 
sen finns det en så kallad spinbox där man väljer vilken Blueray i listan det ser ut såhär:
(1, syns inte) Blueray    Filmnamn    Genre    Regissör    År      Upplösning
(2, syns inte) Blueray    Filmnamn    Genre    Regissör    År      Upplösning
(3, syns inte) Blueray    Filmnamn    Genre    Regissör    År      Upplösning
(1, syns inte) DVD        Filmnamn    Genre    Regissör    År      Upplösning
(2, syns inte) DVD        Filmnamn    Genre    Regissör    År      Upplösning
(3, syns inte) DVD        Filmnamn    Genre    Regissör    År      Upplösning
(1, syns inte) VHS        Filmnamn    Genre    Regissör    År      Upplösning
(2, syns inte) VHS        Filmnamn    Genre    Regissör    År      Upplösning
(3, syns inte) VHS        Filmnamn    Genre    Regissör    År      Upplösning

Låt säga att du ska ändra 5th saken i registret dvs den andra DVD filmen skulle du välja DVD i dropdownboxen och nummer 2 i spinboxen.
Detta skulle kunna förbättras t.ex. att man trycker på den filmen man ska ändra sedan på ändra.

Planen först var att ha 4 olika flikar, en med alla filmer, en med endast Blueray, en med endast DVD och en med endast VHS.
Det hade kunna göras utan att ändra så mycket endast lägga till kod men kapades pga tidsbrist.

Det finns många delar av koden som skulle kunna kortas ner med hjälp av listor och for-loopar och liknande. 
Att fixa detta tar dock mer tid och prioriterades lite lägre då de ger samma resultat som det är nu.

Det finns säker många småsaker för att få programmet skulle bli mer användarvänligt dessa är dock inte så högprioritet då programmet inte
ska användas av allmänheten. Skulle programmet vara till för att användas för folk hade man kunna uppdatera det utifrån feedback vilket
inte är möjligt som det ser ut nu.