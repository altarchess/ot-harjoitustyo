# Ohjelmistotekniikka, harjoitustyö
## Othello ohjelma
Sovelluksen käyttäjä voi pelata othelloa konetta vastaan, tai vaithoehtoisesti syöttäämään molempien pelaajien siirrot halutessaan, niin että hän voi pelata kaverinsa kanssa. Käyttäjä voi myös tallentaa pelin ja palata siihen myöhemmin.

[Release 1](https://github.com/altarchess/ot-harjoitustyo/releases/tag/viikko5)

[Release 2](https://github.com/altarchess/ot-harjoitustyo/releases/tag/viikko6)

[Lopppalautus](https://github.com/altarchess/ot-harjoitustyo/releases/tag/viikko7)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Dokumentaatio
[Vaatimusmäärittely](https://github.com/altarchess/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/altarchess/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Testausdokumentti](https://github.com/altarchess/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

[Kayttöohje](https://github.com/altarchess/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Arkkitehtuurikuvaus](https://github.com/altarchess/ot-harjoitustyo/blob/master/dokumentaatio/Arkkitehtuurikuvaus.md)

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

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```
poetry run invoke coverage-report
```

Raportti generoituu htmlcov-hakemistoon.
