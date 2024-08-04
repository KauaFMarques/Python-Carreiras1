from flask import Flask, render_template,jsonify

app = Flask(__name__)

VAGAS = [{
    'id': 1,
    'titulo': 'analista de dados',
    'localidade': 'Rio de Janeiro',
    'salario': 'R$ 5.000,00'
}, {
    'id': 2,
    'titulo': 'desenvolvedor frontend',
    'localidade': 'Parana',
    'salario': 'R$ 3.500,00'
}, {
    'id': 3,
    'titulo': 'analista de dados',
    'localidade': 'sao paulo',
    'salario': 'R$ 5.000,00'
}, {
    'id': 4,
    'titulo': 'analista de dados',
    'localidade': 'Rio de Janeiro',
    'salario': 'R$ 3.500,00'
}, {
    'id': 5,
    'titulo': 'UI/UIX desing',
    'localidade': 'Malta',
    'salario': 'R$ 2.500,00'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", vagas=VAGAS)

@app.route("/vagas")
def listar_vagas():
  return jsonify(VAGAS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
