import pytest
from src.calculator.cidr import calculate_cidr

def test_cidr_ipv4():
    res = calculate_cidr("192.168.10.25", 27)
    assert res["version"] == 4
    assert res["cidr"] == "192.168.10.25/27"
    assert res["network"] == "192.168.10.0"
    assert res["broadcast"] == "192.168.10.31"
    assert res["subnet_mask"] == "255.255.255.224"
    assert res["wildcard_mask"] == "0.0.0.31"
    assert res["first_host"] == "192.168.10.1"
    assert res["last_host"] == "192.168.10.30"
    assert res["total_addresses"] == 32
    assert res["usable_hosts"] == 30

def test_cidr_ipv6():
    res = calculate_cidr("2001:db8::1", 64)
    assert res["version"] == 6
    assert res["cidr"] == "2001:db8::1/64"
    assert res["network"] == "2001:db8::"
    assert res["first_host"] == "2001:db8::"
    assert res["last_host"] == "2001:db8::ffff:ffff:ffff:ffff"
    assert res["total_addresses"] == 18446744073709551616
