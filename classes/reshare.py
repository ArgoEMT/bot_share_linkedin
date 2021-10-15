class Reshare () :

    share : object
    text : str

    def __init__ (self, share, text=None) :
        self.share = share
        self.text = text

    def toJSON (self) :
        json = {
            "originalShare: {originalShare}".format(self.share.originalShare),
            "owner: {originalShare}".format(self.share.owner),
            "text: {originalShare}".format(self.share.text)
        }
        return json