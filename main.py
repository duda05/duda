from flask import Flask 

app=Flask(__name__)

@app.route("/")
def index():
	 return "Olá"
@app.route("/pagina")
def index():
	 return render_template("index.html")

@app.route("/test")
def test():
	 return "<input type='submit' value='intervalo'>"

app.run(debug=True,host="0.0.0.0")