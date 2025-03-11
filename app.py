from flask import Flask, render_template, send_from_directory


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/corvette")
def corvette():
    return render_template("corvette.html")


@app.route("/klettern-im-elbsandsteingebirge")
def climbing():
    return render_template("Klettern_im_Elbsandsteingebirge.html")


@app.route("/daf")
def daf():
    return render_template("daf.html")


@app.route("/iceland")
def iceland():
    return render_template("iceland.html")


@app.route("/ccl-label")
def cll():
    return render_template("cll.html")


@app.route("/falten-des-kranichs")
def falten_des_kranichs():
    return render_template("kranichs.html")


@app.route("/impressum")
def impressum():
    return render_template("impressum.html")


@app.route("/datenschutz")
def datenschutz():
    return render_template("datenschutz.html")


@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory("static", "sitemap.xml")


# Run app
if __name__ == '__main__':
    app.run()