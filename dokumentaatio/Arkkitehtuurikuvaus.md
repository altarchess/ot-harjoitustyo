# Arkkitehtuurikuvaus
## Rakenne
Koodin rakenne on seuraava

![image](https://user-images.githubusercontent.com/57199282/147420869-4f1956a7-42bb-49bd-931e-f936a892d519.png)

Game loop on ns pelilooppi. Screens pakkaus on sovelluslogiikka eri valikoille jne. Gui, on pakkaus grafiikalle. Entity on pakkaus esim othello laudalle ja muulle matalammalle tasolle jota muokataan ylhäältä. Engine on pakkaus AI:lle.

## Käyttöliittymä

Käyttöliittymä sisältää kolme erillistä näkymää:

- Peli moodi
- Asetusvalikko
- Latausvalikko

Jokainen näistä on toteutettu omana luokkanaan. Näkymistä yksi on aina kerrallaan näkyvänä. Pelilooppi hallitsee mitä milloinkiin [nähdään](https://github.com/altarchess/ot-harjoitustyo/blob/master/src/othello_gui.py)

## Sovelluslogiikka
Sovelluksen tietomallin muodostavat lauta ja latausluokka

![image](https://user-images.githubusercontent.com/57199282/147420890-8c8a7df7-a58a-4b6b-8ca8-67a7d6e4ce38.png)




