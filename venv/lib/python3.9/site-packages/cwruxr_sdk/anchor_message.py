from typing import Dict, Optional

class ASAAnchor:
    """
    Class defining an Azure Spatial Anchor.
    """
    def __init__(
            self, 
            id : int = None, 
            asaGuid : str = None
        ):
        """
        Initialization function.

        Arguments:
        id -- The integer ID for this anchor. Its index in the list.
        asaGuid -- The guid refrencing the Azure Spatial anchor in storage.
        """
        self.id = id
        self.asaGuid = asaGuid

    @classmethod
    def FromDict(cls, data : dict):
        """
        Method to create an ASAAnchor from a dictionary.
        """
        return cls(id = data["id"], asaGuid= data["asaGuid"])

class AnchorMessage:
    """
    A message type which holds information about an anchor in the room.
    """
    def __init__(
            self, 
            id : Optional[str] = None, 
            asaAnchors : Optional[list[ASAAnchor]] = None
        ):
        if(id != None):
            self.id = id
        if(asaAnchors != None):
            self.asaAnchors = asaAnchors
    
    @classmethod
    def FromDict(cls, data : dict):
        """
        Method to create an Anchor Message from a dictionary.
        """
        val = cls()
        val.id = data["id"]
        val.asaAnchors = []
        for d in data["asaAnchors"]:
            val.asaAnchors.append(ASAAnchor.FromDict(d))
        return val