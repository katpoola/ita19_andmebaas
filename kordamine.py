class Viga(Exception):
    pass


class Inimene:

    def __init__(self, kaal, pikkus):
        self.kaal = kaal
        self.pikkus = pikkus

    def kehamassiindex(self):
        kehamass = round(self.kaal//((self.pikkus*0.01)**2))
        return kehamass


try:
    Mari = Inimene(60, 150)
    print("Mari kehamassiindex on: "+str(Mari.kehamassiindex()))
except Viga(Exception):
    print("Midagi läks valesti!")
