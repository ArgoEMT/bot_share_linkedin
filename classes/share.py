class Share ():
    id: str
    owner: str
    time: int

    def __init__(self, id, owner,time):
        self.id = id
        self.owner = owner
        self.time = time

    def fromJson(self, json):
        id = json["id"]
        owner = json["owner"]
        time = json["time"]

        return Share(id=id, owner=owner,time=time)
