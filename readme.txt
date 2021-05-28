

TEKSTIN KIRJAINTEN MÄÄRIEN VISUALISOINTI	


## ilmoitus.py

Python-koodi muuttaa tekstin pieniksi kirjaimiksi, laskee kunkin kirjaimen määrän, tekee jsonin ja tallentaa json-tiedoston alphabets.json.


## index.html

Lukee alphabets.jsonin ja muodostaa sen datan perusteella kirjain-div-gridin. Kunkin kirjaimen taustavärin opacity määräytyy kirjaimen esiintyvyyden mukaan: a-kirjain on yleisin, joten sen opacity on 1. Vastaavasti esimerkiksi c-kirjaimen opacity on 0, koska niitä ei ole demotekstissä. Värigridin alla esitetään kunkin kirjaimen määrä tekstissä.


