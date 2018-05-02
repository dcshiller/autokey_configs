winClass = window.get_active_class()
winTitle = window.get_active_title()

if 'Chromium' in winClass:
    window.move_to_desktop(winClass,3,matchClass=True)
elif 'Google-chrome' in winClass:
    window.move_to_desktop(winClass,2,matchClass=True)
elif 'Firefox' in winClass:
    window.move_to_desktop(winClass,2,matchClass=True)
elif 'Slack' in winClass:
    window.move_to_desktop(winClass,1,matchClass=True)
elif 'VIM' in winTitle:
    window.move_to_desktop(winTitle,0)
elif 'Gnome-terminal' in winClass:
    window.move_to_desktop(winClass,0,matchClass=True)
elif 'Autokey' in winClass:
    window.move_to_desktop(winClass,4,matchClass=True)
elif 'Thunderbird' in winClass:
    window.move_to_desktop(winClass,1,matchClass=True)