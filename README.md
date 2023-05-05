# FieldNameClassification

Classify the field type of a given field name based on an existing knowledge.


## Example usage of distance based classifier:

    from distance_based_fn_classifier import DistanceFieldNameClassifier

    myclassifier = DistanceFieldNameClassifier(0.5)
    myclassifier.load_knowledge_dict(kd)

    fts = myclassifier.predict_field_type(field_name)

The value 0.5 is a tunable threshold. Its value ranges from [0.0, 1.0], where value 1.0 will return the most similar field name from the pre-defined dictionary and doesn't care about the results are make sense or not. And value 0.0 will only return the exact matched ones.  

The type of "fts" is a list since a single field_name can be mapped to different field types.


## Run demo

    python3 demo.py ./tests/knowledge_dict.json  test_field_names.txt


The example output is:
```json
{
    "source_ip": {
        "field_types": [
            "SourceIPv4Address",
            "IPv4Address"
        ],
        "similar_names": [
            "source_ip"
        ],
        "normalized_distance": 0.0
    },
    "sourec_ip": {
        "field_types": [
            "SourceIPv4Address",
            "IPv4Address"
        ],
        "similar_names": [
            "source_ip"
        ],
        "normalized_distance": 0.1111111111111111
    },
    "abcdef_ip": {
        "field_types": [],
        "similar_names": [],
        "normalized_distance": 0.5
    },
    "domain_name": {
        "field_types": [
            "Domain"
        ],
        "similar_names": [
            "domain"
        ],
        "normalized_distance": 0.45454545454545453
    },
    "WindowsDomain": {
        "field_types": [],
        "similar_names": [],
        "normalized_distance": 0.5
    },
    "dst_port": {
        "field_types": [],
        "similar_names": [],
        "normalized_distance": 0.5
    },
    "ip": {
        "field_types": [
            "SourceIPv4Address",
            "DestinationIPv4Address",
            "IPv4Address"
        ],
        "similar_names": [
            "s_ip",
            "d_ip"
        ],
        "normalized_distance": 0.5
    }
}
```

## Example usage of fasttext based classifier:
    from fasttext_fn_classifier import FTClassifier

    myclassifier = FTClassifier(0.5)
    myclassifier.train(knowledge_dict_tr_fname)

    ft = myclassifier.predict_field_type(field_name)

The value 0.5 means the minimum probability. It's the confidence about fasttext's prediction.  

The value ft is a list of field type. And only one field type will be returned even the return type is a Python list.


## run demo 
    python3 demo.py ./tests/knowledge_dict_tr.txt  test_field_names.txt

(Possible) output is:
```json
{
    "source_ip": {
        "field_types": [
            "IPv4Address"
        ]
    },
    "sourec_ip": {
        "field_types": [
            "IPv4Address"
        ]
    },
    "abcdef_ip": {
        "field_types": [
            "IPv4Address"
        ]
    },
    "domain_name": {
        "field_types": [
            "ProcessName"
        ]
    },
    "WindowsDomain": {
        "field_types": [
            "Domain"
        ]
    },
    "dst_port": {
        "field_types": [
            "Domain"
        ]
    },
    "ip": {
        "field_types": [
            "IPv4Address"
        ]
    },
    "endpoint": {
        "field_types": [
            "Domain"
        ]
    }
}
```
