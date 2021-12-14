# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/altarchess/ot-harjoitustyo/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Asennus

Riippuvuuksien asennus onnistuu komenolla

```bash
poetry install
```

## Ohjelman ajaminen

Kun riippuvuudet on asennettu, voi ohjelman käynnistää komennolla

```
poetry run invoke start
```

## Ohjelman käyttö

Pelinäkymässä käyttäjä voi syöttää siirtoja painamalla ruutua johon haluaa sijoittaa nappulan vasemalla hiiripainikkeella. Laudan oikeassa alanurkassa oleva pieni valkoinen tai musta merkki kertoo kumman siirtovuoro on.

![image](https://user-images.githubusercontent.com/57199282/146083891-3d42d20f-7f10-457e-bc5c-51080a3c2aed.png)

 Save - Tallenna laudalla oleva asema niin että siihen voi palata myöhemmin
 New - Aloita uusi peli
 Load - Avaa talenettujen asemien latausnäkymä
 Options - avaa asetuksien valikon
 In progress, jne - kertoo pelin tilan
 
 Latausnäkymässä voi liikkua asemien välillä previous ja next näppäimien avulla, ja palata aseman pelaamiseen painamalla load
 ![image](https://user-images.githubusercontent.com/57199282/146084816-9abbaa92-7b06-4415-90e5-abc445f76962.png)

 

