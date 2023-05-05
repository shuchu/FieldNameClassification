# -*- coding: utf-8 -*-


import json
from collections import defaultdict

from tokenizer import Tokenizer

# Transfer the dictionary into labeled data for fasttext

kd = {}

with open('tests/knowledge_dict.json', 'r') as f:
    kd = json.load(f)

# build the reverse map
inverse_map = defaultdict(set)

for ft in kd:
    for fn in kd[ft]:
        inverse_map[fn].add(ft)


# build traning  data
tr_data = []  # list of list

mytokenizer = Tokenizer()

for fn in inverse_map:
    r = []
    # Add field type
    for ft in inverse_map[fn]:
        r.append('__label__{}'.format(ft))

    fn_tokens = mytokenizer.extract_tokens(fn)
    r.extend(fn_tokens)

    print(r)

    tr_data.append(r)

# write to txt file
print(tr_data)

with open('knowledge_dict_tr.txt', 'w') as f:
    for r in tr_data:
        f.write("{}\n".format(" ".join(r)))
