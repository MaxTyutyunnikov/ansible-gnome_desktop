[![Build Status](https://travis-ci.org/stdevel/ansible-gnome_desktop.svg?branch=master)](https://travis-ci.org/stdevel/ansible-gnome_desktop)

# gnome_desktop

Configures the GNOME 3+ desktop.

## Requirements

This role will not install the GNOME desktop itself - it should be pre-installed.
`dconf` and other requirements will be installed automagically.

## Role Variables

### Top bar settings

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `gnome_topbar_time_24h` | `true` | Show 24h time in top bar |
| `gnome_topbar_time_seconds` | `false` | Show seconds in top bar |
| `gnome_topbar_show_weekday` | `true` | Show weekday in top bar |
| `gnome_battery_percentage` | `false` | Show battery percentage |

### Shell settings

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `gnome_shell_animations` | `true` | Enable GNOME Shell animations |
| `gnome_shell_hotcorners` | `true` | Enable GNOME Shell hot corners |

### Window manager settings

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `gnome_wm_buttons` | `"'appmenu:minimize,maximize,close'"` | Set custom button layout |

### Hardware settings

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `gnome_ambient_light` | `true` | Enable ambient light sensor |

### Mouse/Keyboard settings

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `gnome_mouse_natural_scrolling` | `true` | Enable natural scrolling |
| `gnome_desktop_shortcut` | `true` | Create/restore shortcut for showing desktop (SUPER+D) |

### Other settings

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `gnome_additional_settings` | `true` | Additional setting/value pairs (*as list*) |

## Dependencies

No dependencies.

## Example Playbook

Refer to the following example:

```yaml
---
- hosts: servers
  roles:
      - stdevel.gnome_desktop
```

Set variables if required, e.g.:

```yaml
---
- hosts: uyuni.giertz.loc
  roles:
    - role: stdevel.gnome_desktop
      gnome_additional_settings:
        - setting: "/org/gnome/desktop/privacy/report-technical-problems"
          value: "false"
        - setting: "/org/gnome/desktop/privacy/send-software-usage-stats"
          value: "false"
        - setting: "/org/gnome/desktop/wm/keybindings/minimize"
          value: ['']
        - setting: "/dummy/setting"
          state: absent
```

## License

Apache 2.0

## Author Information

Christian Stankowic (info@cstan.io)
