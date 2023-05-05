# -*- coding: utf-8 -*-


from typing import List


class Tokenizer:
    @classmethod
    def extract_tokens(cls, field_name: str) -> List[str]:
        """Tokenize a field_name to a list of words. Only keep English characters and numbers.
        ord('a') = 97, ord('z') = 122
        ord('A') = 65, ord('Z') = 90
        ord('0') = 48, ord('9') = 57
        """
        fn_char_list = list(field_name)

        for i, v in enumerate(fn_char_list):
            if ord(v) > 64 and ord(v) < 91:
                fn_char_list[i] = chr(ord(v) + 32)
            elif ord(v) > 47 and ord(v) < 58:
                continue
            elif ord(v) > 96 and ord(v) < 123:
                continue
            else:
                fn_char_list[i] = ""

        # nm_fn = "".join(fn_char_list)
        # res = [t.strip() for t in nm_fn.strip().split()]
        res = []
        i, j = 0, 0
        while i < len(fn_char_list):
            if fn_char_list[i]:
                j = i
                while j < len(fn_char_list):
                    if not fn_char_list[j]:
                        res.append("".join(fn_char_list[i:j]))
                        i = j
                        break
                    elif j == len(fn_char_list) - 1:
                        res.append("".join(fn_char_list[i : j + 1]))
                        i = j
                        break
                    else:
                        j += 1
            i += 1

        return res
