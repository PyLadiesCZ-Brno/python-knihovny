# task_32_decode_string.py

def decode_string(s: str) -> str:
    """
    Dekóduje zakódovaný řetězec ve formátu k[encoded_string],
    např. "3[a]2[bc]" → "aaabcbc".
    """
    while '[' in s:
        pos_left_bracket = s.index('[')
        pos_right_bracket = s.index(']')
        # check for nested brackets
        if '[' in s[pos_left_bracket + 1:]:
            pos_left_bracket2 = s.index('[', pos_left_bracket + 1)
        else:
            pos_left_bracket2 = len(s) + 1
        # no nested brackets
        if pos_right_bracket < pos_left_bracket2:
            pos_num = pos_left_bracket - 1
            num = ''
            while s[pos_num].isdigit():
                num = s[pos_num] + num
                pos_num += -1
            s = s[:pos_left_bracket - len(num)] + int(
                num) * s[pos_left_bracket + 1:pos_right_bracket] + s[pos_right_bracket + 1:]
        # nested brackets
        else:
            s = s[:pos_left_bracket + 1] + \
                decode_string(s[pos_left_bracket + 1:])
    return s
