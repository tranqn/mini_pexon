from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cert.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Cert %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        new_cert = Cert(name = request.form['name'])

        try:
            db.session.add(new_cert)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your certification'

    else:
        certs = Cert.query.all()
        return render_template('index.html', cert_list = certs)


@app.route('/delete/<int:id>')
def delete(id):
    cert_to_delete = Cert.query.get_or_404(id)

    try:
        db.session.delete(cert_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that certification'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    cert = Cert.query.get_or_404(id)

    if request.method == 'POST':
        cert.name = request.form['name']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your certification'

    else:
        return render_template('update.html', cert = cert)


if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)
