import json

txt = """
Katso tästä, kuinka Awak Kuier teki suomalaista koripallohistoriaa! Lupaus nautti jo alkulämmittelyistä: "Oli tosi siistiä"

Awak Kuier pelasi ensimmäisenä suomalaisena WNBA-sarjassa. Dallas Wings hävisi ottelun Atlanta Dreamille lukemin 95–101. Kuier kertoi Yle Urheilulle, että debyytti jännitti. Pääkuvaa klikkaamalla voit katsoa koosteen Kuierin avauspelistä.

Naisten koripallon WNBA-sarjaan siirtynyt suomalainen Awak Kuier teki debyyttinsä, kun hänen joukkueensa Dallas Wings kohtasi Atlanta Dreamin vieraskentällä. Dallas hävisi ottelun 95–101.

Kuier teki ottelusta suomalaista koripallohistoriaa, sillä hänestä tuli ensimmäinen suomalaispelaaja, joka on pelannut WNBA-sarjassa.

Vain yhden kerran uuden joukkueen kanssa ennen ottelua harjoitellut Kuier sai peliaikaa kuusi minuuttia ja 45 sekuntia. Suomalainen teki yhden pisteen vapaaheitosta, kahmi yhden hyökkäyspään levypallon ja antoi yhden koriin johtaneen syötön.

– Kyllä jännitti tosi paljon. Olin kuitenkin myös innoissani. Oli tosi siistiä olla jengin kanssa jo alkulämmittelyissä, Kuier iloitsi Yle Urheilulle.

Kuier yritti kolmen pisteen heittoa kaksi kertaa ilman tulosta. Kuier pelasi ottelun avauspuolikkaalla 4.51 ja jälkimmäisellä puoliskolla alle kaksi minuuttia.

Kuier ehti harjoitella joukkueensa kanssa vain kertaalleen ennen debyyttiä.

– Olihan se vaikeaa. Onneksi meillä oli helppoa kuvioita, jotka muistin hyvin. Tärkeintä on päästä omaan rytmiin. Harjoitusten kautta se onnistuu, Kuier itse arvioi.

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
