# -*- coding: utf-8 -*-


import pytest
import fasttext
from fasttext_fn_classifier import FTClassifier


def test_predict_field_type():
    myclassifier = FTClassifier()
    myclassifier.train('knowledge_dict_tr.txt')

    res = myclassifier.predict_field_type('source_ip')
    assert res[0] == 'IPv4Address'

    res = myclassifier.predict_field_type('domain')
    assert res[0] == 'Domain'

    res = myclassifier.predict_field_type('image')
    assert res[0] == 'ProcessName'

    res = myclassifier.predict_field_type('abcdef_ip')
    assert res[0] == 'IPv4Address'
    

def test_save_load():
    myclassifier = FTClassifier()
    myclassifier.train('knowledge_dict_tr.txt')

    model_path = 'fasttext_fn.bin'
    myclassifier.save_model(model_path)

    myclassifier_new = FTClassifier()
    myclassifier_new.load_model(model_path)

    res = myclassifier_new.predict_field_type('source_ip')
    assert res[0] == 'IPv4Address'

