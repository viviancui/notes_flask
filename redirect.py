When make the home page pointing to the specific item in subpage

from flask import Flask, render_template, redirect, url_for

first, you should still have the render_template part
@app.route('/flux/macosall')
def flux_mac_all():
    return render_template('fluxmac.html', title="Flux on MacOS")

after that you can use redirect and use url_for('the function above') & _anchor to item name
@app.route('/flux/macos')
def flux_mac():
    return redirect(url_for('flux_mac_all', _anchor="item-1"))
