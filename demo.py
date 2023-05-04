# -*- coding: utf-8 -*-


import json
import sys
from collections import defaultdict

from distance_based_fn_classifier import DistanceFieldNameClassifier

_usage = """
    demo.py [knowledge_dictionary .json]  [query field_name .txt] 

"""


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(_usage)
        sys.exit(-1)

    knowledge_dict_fname = sys.argv[1]
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

    kd = {}
    try:
        with open(knowledge_dict_fname, "r") as f:
            kd = json.load(f)
    except Exception as e:
        print(
            "Error, failed to load knowledge dictionary file: {} with error: {}".format(
                knowledge_dict_fname, e
            )
        )
        sys.exit(-2)

    myclassifier = DistanceFieldNameClassifier(0.5)
    myclassifier.load_knowledge_dict(kd)

    res = defaultdict(dict)
    for field_name in query_field_names:
        fts = myclassifier.predict_field_type(field_name)
        fns = myclassifier._search_similar_field_names(field_name)
        res[field_name]["field_types"] = fts
        res[field_name]["similar_names"] = fns

    # save results
    ofname = query_field_name_fname + ".fieldtype"
    with open(ofname, "w") as f:
        json.dump(res, f)
