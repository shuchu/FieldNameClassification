# -*- coding: utf-8 -*-


import pytest

from tokenizer import Tokenizer


def test_init():
    tker = Tokenizer()

    res = tker.extract_tokens('ABC')
    assert res[0] == 'abc'

    res = tker.extract_tokens('abc')
    assert res[0] == 'abc'

    res = tker.extract_tokens('Abc')
    assert res[0] == 'abc'

    res = tker.extract_tokens('Abc-------')
    assert res[0] == 'abc'

    res = tker.extract_tokens('-----------@@@@@ Abc')
    assert res[0] == 'abc'

    res = tker.extract_tokens('Abc.edf.hij_kl')
    assert res[0] == 'abc'
    assert res[1] == 'edf'
    assert res[2] == 'hij'
    assert res[3] == 'kl'
 
    res = tker.extract_tokens('ABC-abc')
    assert res[0] == 'abc'
    assert res[1] == 'abc'

    res = tker.extract_tokens('8.8.8.8')
    assert res[0] == '8'
    assert res[1] == '8'
    assert res[2] == '8'
    assert res[3] == '8'