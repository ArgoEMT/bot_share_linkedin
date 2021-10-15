class Share ():
    id: str
    owner: str

    def __init__(self, id, owner):
        self.id = id
        self.owner = owner

    def fromJson(self, json):
        id = json["id"]
        owner = json["owner"]

        return Share(id=id, owner=owner)
