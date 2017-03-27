#-*- coding:utf8 -*-


def getMaxSymStrFromCenterOdd(_string, cur_len):
    """Get The Max Symmetry String of @_string from center.
    Return the start, end index of the Symmetry-String."""
    pos_center = cur_len >> 1
    offset = 1
    while offset <= pos_center and _string[pos_center - offset] == _string[pos_center + offset]:
        offset += 1
    return pos_center + 1 - offset, pos_center - 1 + offset

def getMaxSymStrFromCenterEven(_string, cur_len):
    """Get The Max Symmetry String of @_string from center.
    Return the start, end index of the Symmetry-String."""
    pos_right = cur_len >> 1
    pos_left = pos_right - 1
    offset = 0
    while offset <= pos_left and _string[pos_left - offset] == _string[pos_right + offset]:
        offset += 1
    return pos_left + 1 - offset, pos_right - 1 + offset

def getMaxSymStrFromCenter(_string, cur_len):
    """Get The Max Symmetry String of @_string from center.
    Return the start, end index of the Symmetry-String."""
    if cur_len & 0x1:
        _start, _end = getMaxSymStrFromCenterOdd(_string, cur_len)
    else:
        _start, _end = getMaxSymStrFromCenterEven(_string, cur_len)
    return _start, _end

def getMaxSymStrOdd(_string, totalLen):
    """cur_len is odd"""
    cur_len = totalLen
    pos_center = totalLen >> 1
    pos_left = pos_center - 1
    pos_right = pos_center + 1
    _start, _end = getMaxSymStrFromCenterOdd(_string, cur_len)
    max_length = _end - _start + 1
    cur_len -= 1
    last_round = 1
    while cur_len > max_length:
        if cur_len & 0x1:
            # left side
            _start, _end = getMaxSymStrFromCenterOdd(_string[:cur_len], cur_len)
            _len = _end - _start + 1
            pos_left -= 1
            if _len > max_length:
                max_length = _len
            # right side
            _start, _end = getMaxSymStrFromCenterOdd(_string[last_round:], cur_len)
            _len = _end - _start + 1
            pos_right += 1
            if _len > max_length:
                max_length = _len
        else:
            # left side
            _start, _end = getMaxSymStrFromCenterEven(_string[:cur_len], cur_len)
            _len = _end - _start + 1
            if _len > max_length:
                max_length = _len
            # right side
            _start, _end = getMaxSymStrFromCenterEven(_string[last_round:], cur_len)
            _len = _end - _start + 1
            if _len > max_length:
                max_length = _len
        last_round += 1
        cur_len -= 1
    return max_length 

def getMaxSymStrEven(_string, totalLen):
    """cur_len is even"""
    cur_len = totalLen
    pos_right = cur_len >> 1
    pos_left = pos_right - 1
    max_length = 1
    _start, _end = getMaxSymStrFromCenterEven(_string, cur_len)
    max_length = _end - _start + 1
    cur_len -= 1
    last_round = 1
    while cur_len > max_length:
        if cur_len & 0x1:
            # left side
            _start, _end = getMaxSymStrFromCenterOdd(_string[:cur_len], cur_len)
            _len = _end - _start + 1
            pos_left -= 1
            if _len > max_length:
                max_length = _len
            # right side
            _start, _end = getMaxSymStrFromCenterOdd(_string[last_round:], cur_len)
            _len = _end - _start + 1
            pos_right += 1
            if _len > max_length:
                max_length = _len
        else:
            # left side
            _start, _end = getMaxSymStrFromCenterEven(_string[:cur_len], cur_len)
            _len = _end - _start + 1
            if _len > max_length:
                max_length = _len
            # right side
            _start, _end = getMaxSymStrFromCenterEven(_string[last_round:], cur_len)
            _len = _end - _start + 1
            if _len > max_length:
                max_length = _len
        last_round += 1
        cur_len -= 1
    return max_length 


def FindMaxSymString(_string):
    totalLen = len(_string)
    if totalLen & 0x1:
        max_length = getMaxSymStrOdd(_string, totalLen)
    else:
        max_length = getMaxSymStrEven(_string, totalLen)
    return max_length

def test(_string):
    print "test str '%s'"%_string
    print "old", getMaxSymStrOdd(_string, len(_string))
    print "even", getMaxSymStrEven(_string, len(_string))
    print "all", FindMaxSymString(_string)
    print

for s in ["abcdef", "aba", "acbb", "abcdcba", "abcddcba"]:
    test(s)
