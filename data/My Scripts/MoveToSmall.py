# move active window small screen
winTitle = window.get_active_title()
window.set_property(winTitle, 'remove', 'sticky')
window.set_property(winTitle, 'remove', 'fullscreen')
window.set_property(winTitle, 'remove', 'maximized_vert')
window.set_property(winTitle, 'remove', 'maximized_horz')
window.resize_move(winTitle, xOrigin=0, yOrigin=0, width=-1, height=200)