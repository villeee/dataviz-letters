import json

txt = """
Tiedon visualisoija Helsingin Sanomien datadeskiin

Helsingin Sanomien datadeski hakee tiedon visualisoijaa etsimään datasta uutisia ja visualisoimaan niitä.

Tehtäväsi on kahtalainen: keräät sekä analysoit erilaisia data-aineistoja ja etsit niistä uutisia. Lisäksi pystyt visualisoimaan tietoa grafiikan keinoin. 

Osaat ottaa haltuun erilaisia tietoaineistoja ja analysoida niitä itse koodaamalla tai erilaisten työkalujen avulla. Osaat tehdä tuloksista grafiikkaa esimerkiksi Illustratorilla. Ymmärrät, miten tietoa kannattaa visualisoida verkossa ja erityisesti pienillä mobiililaitteilla. Odotamme kokemusta journalismista tai ainakin vahvaa kiinnostusta alaa kohtaan.

Tehtävässä teet myös paljon yhteistyötä muun toimituksen kanssa. Pestiin kuuluu myös muulloin kuin toimistoaikaan tehtäviä työvuoroja.

HS:n toimituksen datadeski on 16 ihmisen tiimi, jonka digitaalisen journalismin osaaminen on maailmanluokkaa. Tiimissä työskentelee graafikoita, liikegraafikoita, datajournalisteja, tuottajia ja ohjelmistokehittäjiä. 

Lisätietoa antavat toimituspäällikkö toimituspäällikkö Esa Mäkinen, 040 3540371, esa.makinen@hs.fi, ja datadeskin esimies Juhani Saarinen, 050 5869053, juhani.saarinen@hs.fi.

"""

### Lasketaan kirjainten määrät tekstissä

alphabets = "abcdefghijklmnopqrstuvwxyzåäö"
json_alphabets = []

for i in range(len(alphabets)):
    counter = txt.lower().count(alphabets[i])
    data = {"alphabet": alphabets[i], "amount": counter}
    json_alphabets.append(data)

# print(json_alphabets)

with open("alphabets.json", "w") as f:
    json.dump(json_alphabets, f)
f.close()
