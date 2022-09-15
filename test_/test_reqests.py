import pytest
import requests
from request import link,path,headers

def test_requests():
    result = str(requests.get(f"{link}?path={path}",headers=headers))
    etalon = '<Response [200]>'
    assert result == etalon

def test_package_created_requests():
    result = str(requests.put(f"{link}?path={path}",headers=headers))
    etalon = '<Response [409]>'
    assert result == etalon