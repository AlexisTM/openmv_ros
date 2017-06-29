from microros import Struct
import struct

class Tag(object):
  _md5sum = "978c5dc6bcab3c6d1b43fa94c6e22015"
  _type = "umd_msgs/Tag"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# The tag
# Position of the center of the tag
uint8 cx
uint8 cy
# Size of the tag
uint8 width
uint8 height
float32 rotation

# What tag
uint16 id
uint8 family
uint8 confidence
"""
  __slots__ = ['cx','cy','width','height','rotation','id','family','confidence']
  _slot_types = ['uint8','uint8','uint8','uint8','float32','uint16','uint8','uint8']

  def __init__(self):
    self.cx = 0
    self.cy = 0
    self.width = 0
    self.height = 0
    self.rotation = 0.
    self.id = 0
    self.family = 0
    self.confidence = 0

  def serialize(self):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      return _struct_4BfH2B.pack(_x.cx, _x.cy, _x.width, _x.height, _x.rotation, _x.id, _x.family, _x.confidence)
    except:
      pass


  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.cx, _x.cy, _x.width, _x.height, _x.rotation, _x.id, _x.family, _x.confidence,) = _struct_4BfH2B.unpack(str[start:end])
      return self
    except:
      pass

  def __str__(self):
    """
    Stringify the tag
    """
    return "Tag Family {0}, Tag ID {1}, rotation {2}rad \n x: {3}, y: {4}, confidence: {5}%, \n width: {6}, height: {7}".format(self.family, self.id, self.rotation, self.cx, self.cy, self.confidence, self.width, self.height)
    

_struct_4BfH2B = Struct("<4BfH2B")
