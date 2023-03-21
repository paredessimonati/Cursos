import ipaddress


def int32_to_ip(int32):
    return str(ipaddress.ip_address(int32))


