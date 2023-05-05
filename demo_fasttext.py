# -*- coding: utf-8 -*-


import json
import sys
from collections import defaultdict

from fasttext_fn_classifier import FTClassifier

_usage = """
    demo_fasttext.py [knowledge_dictionary_tr.txt]  [query field_name .txt] 

"""


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(_usage)
        sys.exit(-1)

    knowledge_dict_tr_fname = sys.argv[1]
    query_field_name_fname = sys.argv[2]

    query_field_names = []
    try:
        with open(query_field_name_fname, "r") as f:
            for line in f:
                fn = line.strip()
                if fn:
                    query_field_names.append(fn)
    except Exception as e:
        print("Error, failed to load testing field names: {}".format(e))
        sys.exit(-2)

    print("#loaded test field names: {}".format(len(query_field_names)))

    myclassifier = FTClassifier(0.5)
    myclassifier.train(knowledge_dict_tr_fname)

    res = defaultdict(dict)
    for field_name in query_field_names:
        ft = myclassifier.predict_field_type(field_name)
        res[field_name]["field_types"] = ft

    # save results
    ofname = query_field_name_fname + "_ft.json"
    with open(ofname, "w") as f:
        json.dump(res, f)
