# move active window to big screen
winTitle = window.get_active_title()
window.set_property(winTitle, 'remove', 'sticky')
window.set_property(winTitle, 'remove', 'fullscreen')
window.set_property(winTitle, 'remove', 'maximized_vert')
window.set_property(winTitle, 'remove', 'maximized_horz')
window.resize_move(winTitle, xOrigin=1500, yOrigin=0, width=-1, height=-1, matchClass=False)