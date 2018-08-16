from flask import Flask, request

@app.route('/flux/windows')
def flux_windows():
    return redirect(url_for('flux_windows_all', _anchor="item-1"))

@app.route('/flux/macosall')
def flux_mac_all():
    return render_template('fluxmac.html', title="Flux on MacOS")
    
@app.route('/flux/software')
def flux_software():
    platform = request.user_agent.platform
    if platform == 'macos' or 'iphone':
        return redirect(url_for('flux_mac_all', _anchor="item-2"))
    else:
        return redirect(url_for('flux_windows_all', _anchor="item-2"))

@app.route('/flux/connect')
def flux_connect():
    platform = request.user_agent.platform
    if platform == 'macos' or 'iphone':
        return redirect(url_for('flux_mac_all', _anchor="item-3"))
    else:
        return redirect(url_for('flux_windows_all', _anchor="item-3"))
