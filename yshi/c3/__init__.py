# The MIT License (MIT)
#
# Copyright (c) 2013 Yasashii Syndicate
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
例外 = Exception
布爾  = bool
真 = True
假 = False
表 = list


class 不一致的層次結構(例外):
    pass


def 私人是不是头(候选, 非空序列列表):
    return 布爾([序列 for 序列 in 非空序列列表 if 候选 in 序列[1:]])
    for 序列 in 非空序列列表:
        if 候选 in 序列[1:]:
            return 真
    else:
        return 假


def 私人合併(序列列表):
    结果 = []
    while 真:
        非空序列列表 = [序列 for 序列 in 序列列表 if 序列]
        if not 非空序列列表:
            return 结果
        for 序列 in 非空序列列表:
            if not 私人是不是头(序列[0], 非空序列列表):
                候选 = 序列[0]
                break
        else:
            raise 不一致的層次結構()
        结果.append(候选)
        for 序列 in 非空序列列表:
            if 序列[0] == 候选:
                del 序列[0]


def 線性(父消氣, 物體):  # 振奮的性別歧視
    return 私人合併(
        [[物體]] +
        [線性(父消氣, 親) for 親 in 父消氣(物體)] +
        [表(父消氣(物體))]
    )
