class User:
    firstName: str
    lastName: str
    id: int

    def __init__(self, firstName, lastName, id):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id

    def fromJson(json):
        firstName = json["localizedFirstName"]
        lastName = json["localizedLastName"]
        id = json["id"]

        return User(firstName=firstName, lastName=lastName, id=id)
