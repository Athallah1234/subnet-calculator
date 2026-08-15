from typing import Dict, Any
from src.calculator.ipv4 import calculate_ipv4
from src.calculator.ipv6 import calculate_ipv6
import ipaddress

def calculate_cidr(ip_or_network: str, prefix: int) -> Dict[str, Any]:
    """Calculates CIDR details. Supports both IPv4 and IPv6 based on the address version."""
    try:
        ipaddress.IPv4Address(ip_or_network)
        is_ipv4 = True
    except ipaddress.AddressValueError:
        is_ipv4 = False

    if is_ipv4:
        res = calculate_ipv4(ip_or_network, prefix)
        return {
            "version": 4,
            "cidr": f"{ip_or_network}/{prefix}",
            "network": res["network_address"],
            "broadcast": res["broadcast_address"],
            "subnet_mask": res["subnet_mask"],
            "wildcard_mask": res["wildcard_mask"],
            "first_host": res["first_usable_host"],
            "last_host": res["last_usable_host"],
            "total_addresses": res["number_of_addresses"],
            "usable_hosts": res["number_of_usable_hosts"],
            "raw": res
        }
    else:
        res = calculate_ipv6(ip_or_network, prefix)
        return {
            "version": 6,
            "cidr": f"{ip_or_network}/{prefix}",
            "network": res["network_address"],
            "broadcast": "N/A",
            "subnet_mask": "N/A",
            "wildcard_mask": "N/A",
            "first_host": res["first_address"],
            "last_host": res["last_address"],
            "total_addresses": res["number_of_addresses"],
            "usable_hosts": res["number_of_addresses"],
            "raw": res
        }
