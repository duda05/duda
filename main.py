from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
	 return "Olá"
@app.route("/pagina")
def pagina():
	 return render_template("index.html")

@app.route("/test")
def test():
	 return "<input type='submit' value='intervalo'>"

@app.route("/nmap")
def nmap():
	import subprocess
	proc = subprocess.Popen(['nmap','-sP','10.120.71.*'],
		stdout=subprocess.PIPE)
	ret=proc.stdout.read()
	return ret

app.run(debug=True,host="0.0.0.0")