import orjson as json
from math import sin, cos
from typing import Any, Optional

class Vector3:
    """
    Class which holds an x, y and z float component.
    Can be used for position, scale, or euler rotation.
    """
    def __init__(self, x : float = 0, y : float = 0, z : float = 0):
        """
        Initialization function.

        Arguments:
        x -- The X component of the vector
        y -- The Y component of the vector
        z -- The Z component of the vector
        """
        self.x = x
        self.y = y
        self.z = z
    
    @classmethod
    def FromDict(cls, data : dict):
        """
        Method to create a vector3 from a dictionary.
        """
        if data == None:
            return cls()
        return cls(data.get("x"), data.get("y"), data.get("z"))

    def __eq__(self, __o: object) -> bool:
        """
        Comparison function for Vector3s. Will check each component for equality.
        """
        if isinstance(__o, Vector3):
            return (__o.x == self.x) & (__o.y == self.y) & (__o.z == self.z)

        return False

class Vector2:
    """
    Class which holds an x and y float component.
    Can be used for position, scale, or euler rotation.
    """
    def __init__(self, x : float = 0, y : float = 0):
        """
        Initialization function.

        Arguments:
        x -- The X component of the vector
        y -- The Y component of the vector
        """
        self.x = x
        self.y = y
    
    @classmethod
    def FromDict(cls, data : dict):
        """
        Method to create a vector2 from a dictionary.
        """
        if data == None:
            return cls()
        return cls(data.get("x"), data.get("y"))

    def __eq__(self, __o: object) -> bool:
        """
        Comparison function for Vector2s. Will check each component for equality.
        """
        if isinstance(__o, Vector2):
            return (__o.x == self.x) & (__o.y == self.y)
        return False

class Quaternion:
    """
    Class which defines an object's rotation.
    """
    def __init__(self, x : float = 0, y : float = 0, z: float = 0, w : float = 1):
        """
        Initialization function.

        Arguments:
        x -- The X component of the quaternion
        y -- The Y component of the quaternion
        z -- The Z component of the quaternion
        w -- The W component of the quaternion
        """
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    @classmethod
    def FromDict(cls, data : dict):
        """
        Method to create a quaternion from a dictionary.
        """
        if data == None:
            return cls()
        return cls(data.get("x"), data.get("y"), data.get("z"), data.get("w"))

def Euler(v3 : Vector3) -> Quaternion:
    """
    Method to create a quaternion rotation based on a Vector3 euler rotation.
    """
    cy = cos(v3.z / 2)
    sy = sin(v3.z / 2)
    cp = cos(v3.y / 2)
    sp = sin(v3.y / 2)
    cr = cos(v3.x / 2)
    sr = sin(v3.x / 2)

    qw = cr * cp * cy + sr * sp * sy
    qx = sr * cp * cy - cr * sp * sy
    qy = cr * sp * cy + sr * cp * sy
    qz = cr * cp * sy - sr * sp * cy

    return Quaternion(qx,qy,qz,qw)

class Pose:
    """
    Class which holds the full information about position, rotation, and scale of an object.
    """
    def __init__(
            self, 
            position : Optional[Vector3] = None, 
            rotation : Optional[Quaternion] = None,
            euler : Optional[Vector3] = None,
            scale : Optional[Vector3] = None,
        ):
        """
        Initialization function.

        Arguments:
        position -- The Position of the object
        rotation -- The Rotation of the object
        scale -- The Scale of the object
        """
        if position != None:
            self.position = position
        if rotation != None:
            self.rotation = rotation
        if euler != None:
            self.eulerRotation = euler
        if scale != None:
            self.scale = scale
    
    @classmethod
    def FromDict(cls, data : dict):
        """
        Method to create a Pose from a dictionary.
        """
        if data == None:
            return cls()
        return cls(
            position = Vector3.FromDict(data.get("position")),
            rotation = Quaternion.FromDict(data.get("rotation")),
            euler = Vector3.FromDict(data.get("eulerRotation")),
            scale = Vector3.FromDict(data.get("scale"))
        )

class Color:
    """
    Class which contains the rgb components defining a color, and the alpha.
    """
    def __init__(
            self,
            r : float = 0,
            g : float = 0,
            b : float = 0,
            a : float = 0
        ):
        """
        Initialization function.

        Arguments:
        r -- The Red component of the color
        g -- The Green component of the color
        b -- The Blue component of the color
        a -- The Alpha component of the color
        """
        self.r = r
        self.g = g
        self.b = b
        self.a = a
    
    @classmethod
    def FromDict(cls, data : dict):
        """
        Method to create a Color from a dictionary.
        """
        if data == None:
            return cls()
        return cls(data.get("r"), data.get("g"), data.get("b"), data.get("a"))
    

def ToJson(obj) -> str:
    """
    Method to turn an object into a json string.
    """
    return json.dumps(obj, default=lambda a : a.__dict__)

def FromJson(obj) -> dict:
    """
    Method to convert a json string to a dictionary.
    """
    return json.loads(obj)