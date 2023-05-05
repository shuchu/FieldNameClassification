# FieldNameClassification

Classify the field type of a given field name based on an existing knowledge.


## Example usage:

    from distance_based_fn_classifier import DistanceFieldNameClassifier

    myclassifier = DistanceFieldNameClassifier(0.5)
    myclassifier.load_knowledge_dict(kd)

    fts = myclassifier.predict_field_type(field_name)

The value 0.5 is a tunable threshold. Its value ranges from [0.0, 1.0], where value 1.0 will return the most similary field name of the querying field_name from the pre-defined dictionary.  

The type of "fts" is a list since a single field_name can be mapped to different field types.


## Run demo

    python3 demo.py ./tests/knowledge_dic.json  test_field_names.txt


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

