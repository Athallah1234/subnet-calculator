import pytest
from src.calculator.ipv6 import calculate_ipv6

def test_calculate_ipv6_64():
    res = calculate_ipv6("2001:db8::1", 64)
    assert res["network_address"] == "2001:db8::"
    assert res["prefix_length"] == "/64"
    assert res["first_address"] == "2001:db8::"
    assert res["last_address"] == "2001:db8::ffff:ffff:ffff:ffff"
    assert res["number_of_addresses"] == 18446744073709551616
    assert res["classification"]["address_type"] == "Documentation"

def test_calculate_ipv6_global():
    res = calculate_ipv6("2606:4700:4700::1111", 64)
    assert res["classification"]["address_type"] == "Global Unicast"

