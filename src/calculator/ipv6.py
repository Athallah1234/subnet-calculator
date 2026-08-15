import ipaddress
from typing import Dict, Any

def calculate_ipv6(ip_str: str, prefix: int) -> Dict[str, Any]:
    """
    Calculates detailed IPv6 info.
    `ip_str` is the IPv6 address.
    `prefix` is the CIDR prefix (e.g. 64).
    """
    interface = ipaddress.IPv6Interface(f"{ip_str}/{prefix}")
    network = interface.network

    # Expanded / Exploded address
    expanded = interface.ip.exploded
    compressed = interface.ip.compressed

    total_addresses = network.num_addresses
    
    # Range of addresses
    first_address = str(network.network_address)
    # Get last address using network address + num_addresses - 1
    last_address_int = int(network.network_address) + total_addresses - 1
    last_address = str(ipaddress.IPv6Address(last_address_int))

    # Scope and Classifications
    classifications = {
        "address_type": "Unknown",
        "scope": "Unknown",
        "loopback": "Yes" if interface.ip.is_loopback else "No",
        "link_local": "Yes" if interface.ip.is_link_local else "No",
        "multicast": "Yes" if interface.ip.is_multicast else "No",
        "reserved": "Yes" if interface.ip.is_reserved else "No",
        "unspecified": "Yes" if interface.ip.is_unspecified else "No",
        "global": "Yes" if interface.ip.is_global else "No",
        "documentation": "Yes" if interface.ip.is_private else "No" # ipaddress defines private for doc/etc ranges
    }

    # Better types
    if interface.ip.is_multicast:
        classifications["address_type"] = "Multicast"
        classifications["scope"] = "Multicast Group"
    elif interface.ip.is_link_local:
        classifications["address_type"] = "Link-Local Unicast"
        classifications["scope"] = "Link Local"
    elif interface.ip.is_loopback:
        classifications["address_type"] = "Loopback"
        classifications["scope"] = "Node Local"
    elif interface.ip.is_unspecified:
        classifications["address_type"] = "Unspecified"
        classifications["scope"] = "N/A"
    elif str(interface.ip).lower().startswith("2001:db8"):
        classifications["address_type"] = "Documentation"
        classifications["scope"] = "Documentation"
    elif str(interface.ip).lower().startswith("fc") or str(interface.ip).lower().startswith("fd"):
        classifications["address_type"] = "Unique Local Address"
        classifications["scope"] = "Private Network"
    elif interface.ip.is_global or str(interface.ip).startswith("2") or str(interface.ip).startswith("3"):
        classifications["address_type"] = "Global Unicast"
        classifications["scope"] = "Global Internet"
    else:
        classifications["address_type"] = "Unicast (Other)"
        classifications["scope"] = "Global Unicast"

    return {
        "ipv6_address": compressed,
        "prefix_length": f"/{prefix}",
        "network_address": str(network.network_address),
        "first_address": first_address,
        "last_address": last_address,
        "number_of_addresses": total_addresses,
        "compressed_address": compressed,
        "expanded_address": expanded,
        "classification": classifications,
        "prefix_info": {
            "prefix_length": prefix,
            "network_bits": prefix,
            "interface_bits": 128 - prefix,
            "total_addresses": total_addresses
        }
    }
