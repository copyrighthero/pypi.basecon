###############
BaseCon Project
###############

`README中文文档 <https://github.com/copyrighthero/BaseCon/blob/master/README.zh-CN.md>`_

About the BaseCon Library
=========================

BaseCon is a single class library for converting integers into base 2 - 65 encoded, url-safe, strings. It is simple to use and sometimes very fast for it utilizes built-in functions like `bin`, `oct`, `str` and `hex` when converting integers to base 2, 8, 10, 16 encoded strings; and it uses `int` when converting base 2 - 36 encoded strings into integers.

This library, however, is not compatible with the builtin base64 converter as one of the main purpose of this library is to keep the converted string url-safe. And the library currently does not support converting binary data.

One can use this library, for example, to create short link handles when using with auto increment database insertions, which can keep the generated handles short.

How to Use BaseCon Library
==========================

After installation with `pip install BaseCon`, simply import BaseCon, instantiate and use with `encode` (`convert`) and `decode` (`revert`) methods. The default base is 62 for it only uses 0-9, A-Z and a-z when encoding. One can simply change the base when instantiating.

.. code-block:: python

  from basecon import BaseCon

  basecon = BaseCon() # default base is 62
  # encode integer
  basecon(100) # '1c', __call__ method
  basecon.encode(100) # '1c'
  basecon.convert(100) # '1c'
  # decode string
  basecon('1c', False) # 100
  basecon.decode('1c') # 100
  basecon.revert('1c') # 100

  # change the base
  basecon = BaseCon(16) # change the base to 16
  basecon(128) # '80'
  basecon.encode(128) # '80'
  basecon.convert(128) # '80'
  basecon('80', False)
  basecon.decode('80')
  basecon.revert('80')

BaseCon Class API References
============================

`BaseCon` class is the only class exported for this library.

Signature: `BaseCon(base = 62)`

BaseCon Class
-------------

- `encode(data)` or `convert(data)`: encode an integer to string
- `decode(data)` or `revert(data)`: decode a string to integer
- `__call__(data, switch = True)`: encode/decode a payload, if switch is set to True, then it encodes; if it is set to False then it decodes.

Licenses
========

This project is licensed under two permissive licenses, please chose one or both of the licenses to your like. Although not necessary, bug reports or feature improvements, attributes to the author(s), information on how this program is used are welcome and appreciated :-) Happy coding

[BSD-2-Clause License]

Copyright 2018 Hansheng Zhao

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[MIT License]

Copyright 2018 Hansheng Zhao

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
