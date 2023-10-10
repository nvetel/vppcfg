def get_vhost_users(yaml):
    """Return a list of all vhost_users names"""
    ret = []
    if "vhost_users" not in yaml:
        return ret
    for ifname, vhu in yaml["vhost_users"].items():
        ret.append(ifname)
    return ret


def get_by_name(yaml, ifname):
    """Return the vhost user by name, if it exists. Return None otherwise."""
    try:
        if ifname in yaml["vhost_users"]:
            return ifname, yaml["vhost_users"][ifname]
    except KeyError:
        pass
    return None, None


def is_vhost_user(yaml, ifname):
    """Returns True if the interface name is an existing vhost user Tunnel."""
    ifname, iface = get_by_name(yaml, ifname)
    return iface is not None
