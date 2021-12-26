# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.


## Yksikkö- ja integraatiotestaus

### Othello-lauta, ja siihen liittyvat funktiot

Othello laudasta vastaavaa `Board`-luokaa testataan [TestBoard](https://github.com/altarchess/ot-harjoitustyo/blob/master/src/tests/entity/internal_board_test.py) -testiluokalla. Asemien latausta ja tallentamista hoitava `Loader`-luokkaa testaa [TestLoader](https://github.com/altarchess/ot-harjoitustyo/blob/master/src/tests/entity/file_util_test.py) -testiluokka. Asetuksista vastaava luokkaa testaa [Settings](https://github.com/altarchess/ot-harjoitustyo/blob/master/src/tests/entity/settings_test.py) -testiluokka.

### AI, ja Siirtojen generointi
Tekoälysta vastaa `alpha_beta` ja `evaluate` -funktioita testaa [TestAI](https://github.com/altarchess/ot-harjoitustyo/blob/master/src/tests/engine/ai_test.py) -testiluokka. Siirtojen generoinnista vastaava `MoveGen`-luokkaa testaa [TestMoveGen](https://github.com/altarchess/ot-harjoitustyo/blob/master/src/tests/engine/move_gen_test.py) -testiluokka. TestMoveGen toteuttaa testauksen [PERFT](https://www.chessprogramming.org/Perft) menetelmällä.

### Testikattavuus
Käyttöliittymää lukuunottamatta testauksen haarautumakattavuus on 96%

![image](https://user-images.githubusercontent.com/57199282/147406226-40536c27-30b5-4b3f-b678-c1cd164b097e.png)


## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu [käyttöohjeen](./kayttoohje.md) kuvaamalla tavalla sekä Windows 11 - että Linux-ympäristöön.
