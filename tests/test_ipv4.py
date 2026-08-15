import pytest
from src.calculator.ipv4 import calculate_ipv4, subnet_ipv4

def test_calculate_ipv4_24():
    res = calculate_ipv4("192.168.1.10", 24)
    assert res["network_address"] == "192.168.1.0"
    assert res["broadcast_address"] == "192.168.1.255"
    assert res["subnet_mask"] == "255.255.255.0"
    assert res["wildcard_mask"] == "0.0.0.255"
    assert res["first_usable_host"] == "192.168.1.1"
    assert res["last_usable_host"] == "192.168.1.254"
    assert res["number_of_addresses"] == 256
    assert res["number_of_usable_hosts"] == 254
    assert res["classification"]["address_type"] == "Private IPv4"

def test_calculate_ipv4_31():
    res = calculate_ipv4("192.168.1.10", 31)
    assert res["network_address"] == "192.168.1.10"
    assert res["broadcast_address"] == "N/A"
    assert res["first_usable_host"] == "192.168.1.10"
    assert res["last_usable_host"] == "192.168.1.11"
    assert res["number_of_addresses"] == 2
    assert res["number_of_usable_hosts"] == 2

def test_calculate_ipv4_32():
    res = calculate_ipv4("192.168.1.10", 32)
    assert res["network_address"] == "192.168.1.10"
    assert res["broadcast_address"] == "N/A"
    assert res["first_usable_host"] == "192.168.1.10"
    assert res["last_usable_host"] == "192.168.1.10"
    assert res["number_of_addresses"] == 1
    assert res["number_of_usable_hosts"] == 1

def test_subnet_ipv4():
    res = subnet_ipv4("192.168.1.0/24", 26)
    assert res["number_of_subnets"] == 4
    assert res["addresses_per_subnet"] == 64
    assert res["usable_hosts"] == 62
    assert res["subnets"][0]["network"] == "192.168.1.0/26"
    assert res["subnets"][1]["network"] == "192.168.1.64/26"
