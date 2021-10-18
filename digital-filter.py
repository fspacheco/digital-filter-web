"""

Flask Application for Digital Filter Design and Analysis
Fernando S. Pacheco

"""
from flask import Flask, render_template
from scipy import signal

app = Flask(__name__)

@app.route("/")
def homepage():
    """View function for Home Page."""
    return "<h1>Digital Filter Design and Analysis</h1>\
<p>Hello, filter designer!</p>\
<p>This is a work in progress. Try a <a href=/design_notch/48000/4500/30>notch filter with fs=48kHz, fc=4.5kHz, and Q=30</a></p>"


@app.route("/design_notch/<int:fs>/<int:fc>/<int:qfactor>")
def design_notch(fs, fc, qfactor):
    """Design 2nd order notch filter."""
    b, a = signal.iirnotch(fc, qfactor, fs)
    return "Filter with fs:"+str(fs)+", fc:"+str(fc)+" and Q:"+str(qfactor)+" has b:"+str(b)+" and a:"+str(a)

if __name__ == "__main__":
    app.run(debug=True)
