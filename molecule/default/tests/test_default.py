"""Role testing files using testinfra."""


def test_dconf_settings(host):
    """
    Tests some dconf settings
    """
    settings = [
        "/org/gnome/desktop/interface/enable-animations",
        "/org/gnome/desktop/interface/enable-hot-corners"
    ]
    for setting in settings:
        result = host.run("dconf read %s" % setting).stdout.strip()
        assert 'true' in result
