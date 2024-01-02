import browsers

def browser_toggle():
    if browsers.get("chrome")!=None:
        return ["chrome"]
    elif browsers.get("msedge")!=None:
        return["msedge"]
    elif browsers.get("firefox")!=None:
        return["firefox"]
    elif browsers.get("msie")!=None:
        return["msie"]
    elif browsers.get("safari")!=None:
        return["safari"]
    else:
        return "Unknown"