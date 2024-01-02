__all__ = ['temp']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['getBrowser'])
@Js
def PyJsHoisted_getBrowser_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['userAgent', 'browser'])
    var.put('userAgent', var.get('navigator').get('userAgent'))
    var.put('browser', Js('Unknown'))
    if (JsRegExp('/Chrome/').callprop('test', var.get('userAgent')) and JsRegExp('/Chromium/').callprop('test', var.get('userAgent')).neg()):
        var.put('browser', Js('Google Chrome'))
    else:
        if JsRegExp('/Edg/').callprop('test', var.get('userAgent')):
            var.put('browser', Js('Microsoft Edge'))
        else:
            if JsRegExp('/Firefox/').callprop('test', var.get('userAgent')):
                var.put('browser', Js('Mozilla Firefox'))
            else:
                if JsRegExp('/Safari/').callprop('test', var.get('userAgent')):
                    var.put('browser', Js('Apple Safari'))
                else:
                    if JsRegExp('/Trident/').callprop('test', var.get('userAgent')):
                        var.put('browser', Js('Internet Explorer'))
    return var.get('browser')
PyJsHoisted_getBrowser_.func_name = 'getBrowser'
var.put('getBrowser', PyJsHoisted_getBrowser_)
pass
pass


# Add lib to the module scope
temp = var.to_python()