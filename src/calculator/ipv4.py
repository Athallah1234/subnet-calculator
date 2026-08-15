import ipaddress
from typing import Dict, Any, List

def calculate_ipv4(ip_str: str, prefix: int) -> Dict[str, Any]:
    """
    Calculates detailed IPv4 info.
    `ip_str` is the IP address without prefix (e.g. 192.168.1.10).
    `prefix` is the CIDR prefix (e.g. 24).
    """
    interface = ipaddress.IPv4Interface(f"{ip_str}/{prefix}")
    network = interface.network
    
    # Calculate wildcard mask
    netmask_int = int(interface.netmask)
    wildcard_int = netmask_int ^ 0xFFFFFFFF
    wildcard_mask = str(ipaddress.IPv4Address(wildcard_int))
    
    # Special calculation for /31 and /32
    if prefix == 32:
        total_addresses = 1
        usable_hosts = 1
        first_host = str(network.network_address)
        last_host = str(network.network_address)
        broadcast = "N/A"
    elif prefix == 31:
        total_addresses = 2
        usable_hosts = 2
        first_host = str(network.network_address)
        last_host = str(network.network_address + 1)
        broadcast = "N/A"
    else:
        total_addresses = network.num_addresses
        usable_hosts = total_addresses - 2
        first_host = str(network.network_address + 1)
        last_host = str(network.broadcast_address - 1)
        broadcast = str(network.broadcast_address)

    # Classifications
    classifications = {
        "address_type": "Private IPv4" if network.is_private else "Public IPv4",
        "scope": "Private Network" if network.is_private else "Global Internet",
        "loopback": "Yes" if network.is_loopback else "No",
        "link_local": "Yes" if network.is_link_local else "No",
        "multicast": "Yes" if network.is_multicast else "No",
        "reserved": "Yes" if network.is_reserved else "No",
        "unspecified": "Yes" if network.is_unspecified else "No",
        "global": "Yes" if network.is_global else "No",
        "documentation": "Yes" if network.is_private and "192.0.2." in ip_str or "198.51.100." in ip_str or "203.0.113." in ip_str else "No"
    }

    # Binary Representation
    ip_octets = ip_str.split('.')
    ip_binary_parts = [f"{int(x):08b}" for x in ip_octets]
    ip_binary = ".".join(ip_binary_parts)
    
    binary_flat = "".join(ip_binary_parts)
    net_part = binary_flat[:prefix]
    host_part = binary_flat[prefix:]
    
    # Add separating dot to visual net/host parts
    net_parts_grouped = []
    host_parts_grouped = []
    
    for i in range(0, 32, 8):
        # determine how many bits of this octet are network bits
        start = i
        end = i + 8
        octet_bin = binary_flat[start:end]
        if prefix >= end:
            net_parts_grouped.append(octet_bin)
        elif prefix <= start:
            host_parts_grouped.append(octet_bin)
        else:
            boundary = prefix - start
            net_parts_grouped.append(octet_bin[:boundary])
            host_parts_grouped.append(octet_bin[boundary:])
            
    network_bits_str = ".".join(net_parts_grouped)
    host_bits_str = ".".join(host_parts_grouped)
    net_host_binary = f"{network_bits_str} | {host_bits_str}"

    return {
        "ip_address": ip_str,
        "cidr_prefix": f"/{prefix}",
        "subnet_mask": str(interface.netmask),
        "wildcard_mask": wildcard_mask,
        "network_address": str(network.network_address),
        "broadcast_address": broadcast,
        "first_usable_host": first_host,
        "last_usable_host": last_host,
        "number_of_addresses": total_addresses,
        "number_of_usable_hosts": usable_hosts,
        "classification": classifications,
        "binary": {
            "ip": f"{ip_octets[0]:>8} .{ip_octets[1]:>8} .{ip_octets[2]:>8} .{ip_octets[3]:>8}",
            "binary": ip_binary,
            "network_host": net_host_binary
        }
    }

def subnet_ipv4(network_str: str, new_prefix: int) -> Dict[str, Any]:
    """Subnets an IPv4 network using a new prefix."""
    network = ipaddress.IPv4Network(network_str, strict=False)
    subnets = list(network.subnets(new_prefix=new_prefix))
    
    addresses_per_subnet = 2**(32 - new_prefix)
    if new_prefix == 32:
        usable_per_subnet = 1
    elif new_prefix == 31:
        usable_per_subnet = 2
    else:
        usable_per_subnet = addresses_per_subnet - 2

    subnet_list = []
    for idx, sub in enumerate(subnets):
        if new_prefix == 32:
            first = str(sub.network_address)
            last = str(sub.network_address)
            bcast = "N/A"
        elif new_prefix == 31:
            first = str(sub.network_address)
            last = str(sub.network_address + 1)
            bcast = "N/A"
        else:
            first = str(sub.network_address + 1)
            last = str(sub.broadcast_address - 1)
            bcast = str(sub.broadcast_address)

        subnet_list.append({
            "index": idx + 1,
            "network": str(sub),
            "first_host": first,
            "last_host": last,
            "broadcast": bcast
        })

    return {
        "original_network": network_str,
        "new_prefix": f"/{new_prefix}",
        "number_of_subnets": len(subnets),
        "addresses_per_subnet": addresses_per_subnet,
        "usable_hosts": usable_per_subnet,
        "subnets": subnet_list
    }
