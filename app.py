##### -------------- natalia mora l. - vc cohorte gracosoft - bd no sql eval. 2
from flask import Flask, redirect, request, render_template, url_for, flash
from db import collection
from bson.objectid import ObjectId
##
app = Flask(__name__, template_folder="./templates")
app.config['SECRET_KEY'] = "clave_secreta"
## LIST
@app.route("/subjects", methods=["GET"])
def subjects():
    materias = collection.find()
    return render_template("subjectList.html.jinja", materias=materias)

## CREATE
@app.route("/", methods=["GET", "POST"])
def add_subject():
    if request.method == "POST":

        """{{el._id}}  -----> m._id
                {{el.nombre}}  -----> m.nombreProf
                -----> m.apellidoProf
                -----> m.idProf
                -----> m.nombreM
                -----> m.objetM
                -----> m.duracion
                -----> m.notaMin"""

        nombreProf = request.form['teacherFirstName']
        apellidoProf = request.form['teacherLastName']
        idProf = request.form['teacherId']
        nombreM = request.form['subjectName']
        objetM = request.form['subjectPurpose']
        duracion = request.form['durationSubject']
        notaMin = request.form['minimumPassingGrade']

        materia = {
            'nombreProf' : nombreProf,
            'apellidoProf' : apellidoProf,
            'idProf' : idProf,
            'nombreM' : nombreM,
            'objetM' : objetM,
            'duracion' : duracion,
            'notaMin' : notaMin,
        }

        print("Subject: ", materia)

        collection.insert_one(materia)
        materias = collection.find()
        return render_template("subjectList.html.jinja", materias=materias)
    return render_template("createSubject.html.jinja")
## ID
@app.route("/<id>", methods=["GET"])
def getElement(id):
    oid = ObjectId(id)
    matX = collection.find_one({'_id': oid})
    return render_template("detailedSubject.html.jinja", subjectX=matX)
## UPDATE
@app.route("/modificar/<id>", methods=["GET", "POST"])
def updateElement(id):
    oid = ObjectId(id)
    materia = collection.find_one({'_id': oid})
    if request.method == "POST":
        new_materia = request.form
        materia = collection.replace_one({'_id': oid},
                                        {
                                            'nombreProf' : new_materia['teacherFirstName'],
                                            'apellidoProf' : new_materia['teacherLastName'],
                                            'idProf' : new_materia['teacherId'],
                                            'nombreM' : new_materia['subjectName'],
                                            'objetM' : new_materia['subjectPurpose'],
                                            'duracion' : new_materia['durationSubject'],
                                            'notaMin' : new_materia['minimumPassingGrade'],
                                        })
        return redirect(url_for('subjects'))
    return render_template("updateSubject.html.jinja", subjectX=materia)
## DELETE
@app.route("/delete/<id>", methods=["GET"])
def deleteElement(id):
    oid = ObjectId(id)
    collection.delete_one({'_id': oid})
    materias = collection.find()
    return render_template("subjectList.html.jinja", materias=materias)

if __name__ == "__main__":
    app.run(debug=True)


"""
            nombreProf = request.form['teacherFirstName']
            apellidoProf = request.form['teacherLastName']
            idProf = request.form['teacherId']
            nombreM = request.form['subjectName']
            objetM = request.form['subjectPurpose']
            duracion = request.form['durationSubject']
            notaMin = request.form['minimumPassingGrade'] 
        """