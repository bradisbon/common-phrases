import json

from fastapi.testclient import TestClient

from common_phrases.main import api


client = TestClient(api)


def test_find_common():
    data = {'text': 'a b c a b c a b c d e f d e f'}
    r = client.post('/find_common', data=json.dumps(data))

    assert r.status_code == 200
    assert r.json().get('most_common') == ['a b c', 'b c a', 'c a b', 'd e f', 'b c d', 'c d e', 'e f d', 'f d e']


def test_find_common_ignore_punc():
    data = {'text': 'a b c a b c!'}
    r = client.post('/find_common', data=json.dumps(data))

    assert r.status_code == 200
    assert r.json().get('most_common') == ['a b c', 'b c a', 'c a b']


def test_find_common_ignore_case():
    data = {'text': 'a b c A B C'}
    r = client.post('/find_common', data=json.dumps(data))

    assert r.status_code == 200
    assert r.json().get('most_common') == ['a b c', 'b c a', 'c a b']


def test_find_common_convert_newlines():
    data = {'text': 'a b c a\nb c'}
    r = client.post('/find_common', data=json.dumps(data))

    assert r.status_code == 200
    assert r.json().get('most_common') == ['a b c', 'b c a', 'c a b']
