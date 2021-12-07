# Ohjelmistotekniikka, harjoitustyö
## Othello ohjelma
Sovelluksen käyttäjä voi pelata othelloa konetta vastaan, tai vaithoehtoisesti syöttäämään molempien pelaajien siirrot halutessaan, niin että hän voi pelata kaverinsa kanssa. Käyttäjä voi myös tallentaa pelin ja palata siihen myöhemmin.

## Dokumentaatio
[Vaatimusmäärittely](https://github.com/altarchess/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/altarchess/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
