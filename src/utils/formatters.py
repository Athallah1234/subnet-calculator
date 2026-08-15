import json
from typing import Dict, Any

def format_number(val: int) -> str:
    """Formats large integer numbers with thousands separators."""
    return f"{val:,}"

def format_to_txt(data: Dict[str, Any]) -> str:
    """Formats calculation data dictionary to human-readable TXT format."""
    lines = [
        "Simple Subnet Calculator",
        "=========================",
        ""
    ]
    for key, val in data.items():
        if key == "binary":
            lines.append("Binary Representation:")
            lines.append(f"  IP Address: {val.get('ip', '')}")
            lines.append(f"  Binary    : {val.get('binary', '')}")
            if 'network_host' in val:
                lines.append(f"  Net/Host  : {val.get('network_host', '')}")
            lines.append("")
        elif key == "subnets" and val:
            lines.append("Subnet Information:")
            for sub in val:
                lines.append(f"  Subnet {sub.get('index', '')}:")
                lines.append(f"    Network   : {sub.get('network', '')}")
                lines.append(f"    First Host: {sub.get('first_host', '')}")
                lines.append(f"    Last Host : {sub.get('last_host', '')}")
                lines.append(f"    Broadcast : {sub.get('broadcast', '')}")
            lines.append("")
        elif key == "classification":
            lines.append("Classification:")
            for k, v in val.items():
                name = k.replace('_', ' ').title()
                lines.append(f"  {name:<15}: {v}")
            lines.append("")
        else:
            name = key.replace('_', ' ').title()
            lines.append(f"{name:<20}: {val}")

    return "\n".join(lines)

def format_to_json(data: Dict[str, Any]) -> str:
    """Serializes calculation data to formatted JSON string."""
    return json.dumps(data, indent=2)
