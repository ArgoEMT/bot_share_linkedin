class Reshare () :

    share : object
    text : str

    def __init__ (self, share, text=None) :
        self.share = share
        self.text = text

    def toJSON (self) :
        json = {
            "originalShare: {originalShare}".format(self.share.originalShare),
            "owner: {owner}".format(self.share.owner),
            "text: {text}".format(self.share.text)
        }
        return json

