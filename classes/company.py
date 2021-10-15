class Company () :
    nom : str
    urn : str

    def __init__ (self, nom, urn) :
        self.nom = nom
        self.urn = urn

    def fromJSON (self, json) :
        nom = json["vanityName"]["entity~"]
        urn = json["entity"]

        return Company(nom= nom, urn= urn)
