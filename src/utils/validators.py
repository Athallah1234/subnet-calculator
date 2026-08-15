import re
import ipaddress
from typing import Tuple, Optional

def validate_cidr_input(ip_str: str) -> Tuple[bool, str, Optional[int]]:
    """
    Validates the input IP address/CIDR.
    Returns: (is_valid, clean_ip_or_network, prefix_if_any)
    """
    ip_str = ip_str.strip()
    if not ip_str:
        return False, "Input cannot be empty.", None

    # Check for prefix slash
    parts = ip_str.split('/')
    if len(parts) > 2:
        return False, "Invalid format. Multiple slashes found.", None

    ip_part = parts[0]
    prefix_part = parts[1] if len(parts) == 2 else None

    # Check IP version by trying to parse IP
    is_ipv4 = False
    is_ipv6 = False

    try:
        ipaddress.IPv4Address(ip_part)
        is_ipv4 = True
    except ipaddress.AddressValueError:
        pass

    if not is_ipv4:
        try:
            ipaddress.IPv6Address(ip_part)
            is_ipv6 = True
        except ipaddress.AddressValueError:
            pass

    if not is_ipv4 and not is_ipv6:
        return False, f"Invalid IP address format: {ip_part}", None

    if prefix_part is not None:
        try:
            prefix = int(prefix_part)
        except ValueError:
            return False, f"Invalid prefix format: {prefix_part}. Prefix must be an integer.", None

        if is_ipv4 and (prefix < 0 or prefix > 32):
            return False, f"Invalid IPv4 prefix: /{prefix}. Must be between 0 and 32.", None
        elif is_ipv6 and (prefix < 0 or prefix > 128):
            return False, f"Invalid IPv6 prefix: /{prefix}. Must be between 0 and 128.", None

        return True, ip_str, prefix
    else:
        return True, ip_part, None
