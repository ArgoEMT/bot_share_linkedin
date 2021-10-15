class Share () :
    originalShare : str
    owner : str

    def __init__ (self, originalShare, owner) :
        self.originalShare = originalShare
        self.owner = owner

    def fromJSON (self, json) :
        originalShare = json["originalShare"]
        owner = json["owner"]

        return Share(originalShare=originalShare, owner=owner)
