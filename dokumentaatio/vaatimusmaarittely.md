# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksen käyttäjä voi pelata othelloa konetta vastaan, tai vaithoehtoisesti syöttäämään molempien pelaajien siirrot halutessaan, niin että hän voi pelata kaverinsa kanssa. Käyttäjä voi myös tallentaa pelin ja palata siihen myöhemmin.

## Suunnitellut toiminnallisuudet
- Pelinäkymä jossa käyttäjä näkee pelilaudan, Kumman pelaajan vuoro on, ja nappulat: Peru siirto, talenna peli, lataa peli ja uusi peli. (Tehty Siirron peruutusta lukuun ottamatta. Se vaatisi jatkokehitysideana ollutta koko pelin tallennusta.)
- Pelinäkymässä pelaaja pystyy lisäämän valkoisen nappulan painamalla haluamaansa ruutua vasemalla hiirinäpäimellä, ja samoin mustan nappulan painamalla oikeata. (Tehty, mutta mollemmat lisätään vasemalla hiirinäppäimellä. Nappulan väri määräytyy vuoron mukaan)
- Jos painaa "talenna peli" nappia, sovelluksen tulisi tallentaa peli ja aika, niin että pelin voi löytää myöhemmin (tehty)
- Jos painaa "lataa peli" nappulaa, pitäisi siirtä näkymään, jossa voi nuolinäppäimillä liikkua eri talenettujen pelien välillä, ja jatkaa niitä jos haluaa (Tehty, mutta nuolinäppäimien sijaan siirrytään asemien välillä "previous" ja "next" napeilla)
- Jos painaa "uusi peli" nappia, pitäisi siirtyä näkymään, jossa voi valita haluaako pelata konetta vastaan vai kaverin kanssa. ("New" nappula tehty joka aloittaa uuden pelin, käyttäjä voi itse valita milloin kone ja milloin ihminen pelaa pelin aikana "AI Move" napin avolla)

## Jatkokehitysideat
- Useat eri tasot tietokonetta vastaan (Tehty)
- Koko pelin eikä vain aseman tallennus. Tämä mahdollistaisi pelin läpikäynnin nuolinäppäimillä.
- Tietokoneanalyysin saaminen pelistä (edellyttää yllä olevaa). Kone analysoisi koko pelin ja piirtäisi sen perusteella evaluaatiograafin.
 
