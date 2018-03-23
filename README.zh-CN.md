# BaseCon类 #

[README中文文档](README.zh-CN.md)

## 关于BaseCon库 ##

BaseCon是一个单类的库，被用于将数字编码成url安全的字符串，或将字符串解码为数字。 这个库简单易用，并且在特定基数的情况下速度很快。如果基数为2，8，10，16的请胯下，本库将使用Python内置的`bin`, `oct`, `str`和`hex`函数来编码；并且使用`int`函数来解码。本库支持2-65的基数。

本库和Python内置的`base64`库并不兼容，因为本库着重于URL兼容性。需要注意的是当前的库并不支持二进制数据的转换。

一个例子是：用户可以使用本库来根据数据库的lastrowid来创建短链接的接口，这样短链接可以变得比直接使用数字的连接更短。

## 如何使用BaseCon库 ##

使用`pip install BaseCon`安装之后，只需要import BaseCon，创建实例并且`encode` (`convert`) 和 `decode` (`revert`) 方法。默认的基数是62，因为所有的编码只需要0-9, A-Z 还有 a-z。用户在实例化的时候可以指定所需要的基数。

```python
from basecon import BaseCon

basecon = BaseCon() # 默认基数为62
# 编码整数
basecon(100) # '1c', __call__ 方法
basecon.encode(100) # '1c'
basecon.convert(100) # '1c'
# 解码字符串
basecon('1c', False) # 100
basecon.decode('1c') # 100
basecon.revert('1c') # 100

# 改变基数
basecon = BaseCon(16) # 把基数变为16
basecon(128) # '80'
basecon.encode(128) # '80'
basecon.convert(128) # '80'
basecon('80', False)
basecon.decode('80')
basecon.revert('80')
```

## BaseCon Class API References ##

`BaseCon`类是此库暴露的唯一类。

头: `BaseCon(base = 62)`

### BaseCon Class ###

- `encode(data)` or `convert(data)`: 将整数编码成字符串。
- `decode(data)` or `revert(data)`: 将字符串解码成整数。
- `__call__(data, switch = True)`: 编码整数/解码字符串, 如果switch设定为True，将被用来编码整数；如果设定为False将解码字符串.

## Licenses ##

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
