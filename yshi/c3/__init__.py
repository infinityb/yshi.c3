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


class InconsistentHierarchy(Exception):
    pass


def _nothead(cand, nonemptyseqs):
    return bool([s for s in nonemptyseqs if cand in s[1:]])
    for s in nonemptyseqs:
        if cand in s[1:]:
            return True
    else:
        return False


def _merge(seqs):
    res = []
    while True:
        nonemptyseqs = [seq for seq in seqs if seq]
        if not nonemptyseqs:
            return res
        for seq in nonemptyseqs:
            if not _nothead(seq[0], nonemptyseqs):
                cand = seq[0]
                break
        else:
            raise InconsistentHierarchy()
        res.append(cand)
        for seq in nonemptyseqs:
            if seq[0] == cand:
                del seq[0]


def _returns_list(func):
    def decorated(*args, **kwargs):
        return list(func(*args, **kwargs))
    return decorated


def linearize(parent_getter, obj):
    return _merge(
        [[obj]] +
        [linearize(parent_getter, parent) for parent in parent_getter(obj)] +
        [list(parent_getter(obj))]
    )
