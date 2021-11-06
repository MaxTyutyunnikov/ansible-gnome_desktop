"""Role testing files using testinfra."""


def test_dconf_settings(host):
    """
    Tests some dconf settings
    """
    settings = [
        "/org/gnome/desktop/interface/enable-animations",
        "/org/gnome/desktop/interface/enable-hot-corners",
        "/org/gnome/desktop/privacy/report-technical-problems",
        "/org/gnome/desktop/privacy/send-software-usage-stats"
    ]
    for setting in settings:
        result = host.run("dconf read %s" % setting).stdout.strip()
        assert 'false' in result
