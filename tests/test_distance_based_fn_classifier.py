# -*- coding: utf-8 -*-


import json

import pytest

from distance_based_fn_classifier import DistanceFieldNameClassifier


@pytest.fixture
def knowledge_dict():
    kd = {}
    with open('./tests/knowledge_dict.json', 'r') as f:
        kd = json.load(f)
    return kd

def test_predict_field_type(knowledge_dict):
    dist_classifier = DistanceFieldNameClassifier()
    dist_classifier.load_knowledge_dict(knowledge_dict)

    # Example test
    query_fn = 'source_ip'
    res = dist_classifier.predict_field_type(query_fn)

    assert len(res) == 2
    assert 'SourceIPv4Address' in res
    assert 'IPv4Address' in res
    
    query_fn = 'image'
    res = dist_classifier.predict_field_type(query_fn)

    assert len(res) == 1
    assert 'ProcessName' == res[0]


def test_load_knowledge_dict():
    
    kd = {'a': [1]}

    dist_classifier = DistanceFieldNameClassifier()
    dist_classifier.load_knowledge_dict(kd)

    assert 'a' in dist_classifier._kd
    assert dist_classifier._kd['a'] == [1]
    assert 1 in dist_classifier._lookup_tbl
    assert dist_classifier._lookup_tbl[1] == {'a'}

        
    kd = {'a': 1}

    dist_classifier = DistanceFieldNameClassifier()
    dist_classifier.load_knowledge_dict(kd)

    assert 'a' in dist_classifier._kd
    assert dist_classifier._kd['a'] == 1
    assert not dist_classifier._lookup_tbl


