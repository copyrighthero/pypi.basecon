# Author: Hansheng Zhao <copyrighthero@gmail.com> (https://www.zhs.me)


# import directive
__all__ = ('__author__', '__license__', '__version__', 'BaseConvert')
# package metadata
__author__ = 'Hansheng Zhao'
__license__ = 'BSD-2-Clause + MIT'
__version__ = '1.0.1'


class BaseCon(object):
  """ BaseCon class for converting integers to URL safe strings """

  # stop dynamic attribute creation
  __slots__ = ('_base', )
  # Base conversion charsets and indices
  _charset = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-._'
  _reverse = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
    'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25,
    'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35, 'a': 36, 'b': 37, 'c': 38,
    'd': 39, 'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44, 'j': 45, 'k': 46, 'l': 47, 'm': 48, 'n': 49, 'o': 50, 'p': 51,
    'q': 52, 'r': 53, 's': 54, 't': 55, 'u': 56, 'v': 57, 'w': 58, 'x': 59, 'y': 60, 'z': 61, '-': 62, '.': 63, '_': 64
  }

  def __init__(self, base = 62):
    """ BaseConvert class for converting integers """
    if not (isinstance(base, int) and 2 <= base <= 65):
      raise ValueError('Base should be between 2 and 65.')
    # preserve base
    self._base = base

  def __call__(self, data, switch = True):
    """
    Alias for encode/decode methods
    :param data: int, positive integer
    :param switch: bool, whether to encode
    :return: str|int, result
    """
    return self.encode(data) \
      if switch else self.decode(data)

  def encode(self, data):
    """
    Encode integers into base encoded strings.
    :param data: int, the integers to be encoded
    :return: str, base encoded string
    """
    # check if data payload and base are valid
    if not isinstance(data, int) and data > 0:
      raise TypeError('Accepts only non-negative int.')
    # acquire base
    base = self._base
    # check if base have known functions
    if base == 2: return bin(data)[2:]
    elif base == 8: return oct(data)[2:]
    elif base == 10: return str(data)
    elif base == 16: return hex(data)[2:]
    # prepend encoded string to the result
    result = ''
    while data:
      remainder = data % base
      data = (data - remainder) // base
      result  = self._charset[remainder] + result
    return result

  convert = encode

  def decode(self, data):
    """
    Decode base encoded strings back into integers.
    :param data: str, base encoded string
    :return: int, the original number
    """
    # check if data payload and base are valid
    if isinstance(data, (bytes, bytearray)):
      data = data.decode(encoding = 'ASCII')
    elif not isinstance(data, str):
      raise TypeError('Accepts only str, bytes and bytearray.')
    # acquire base
    base = self._base
    # check if base can be used with int function
    if 2 <= base <= 36: return int(data, base)
    # iteratively decode the string
    result = 0
    for item in data:
      result = result * base + self._reverse[item]
    return result

  # aliases for decode
  revert = decode
