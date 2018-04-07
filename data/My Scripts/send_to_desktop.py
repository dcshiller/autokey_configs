winTitle = window.get_active_class()
if 'Chromium' in winTitle:
    window.move_to_desktop(winTitle,2,matchClass=True)
elif 'chrome' in winTitle:
    window.move_to_desktop(winTitle,2,matchClass=True)
elif 'Firefox' in winTitle:
    window.move_to_desktop(winTitle,2,matchClass=True)
elif 'Slack' in winTitle:
    window.move_to_desktop(winTitle,1,matchClass=True)
elif 'Gnome-terminal' in winTitle:
    window.move_to_desktop(winTitle,0,matchClass=True)
elif 'Autokey' in winTitle:
    window.move_to_desktop(winTitle,4,matchClass=True)
elif 'Thunderbird' in winTitle:
    window.move_to_desktop(winTitle,1,matchClass=True)