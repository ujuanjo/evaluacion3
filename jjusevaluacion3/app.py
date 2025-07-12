from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def paginaInicio():
    return render_template('index.html')

@app.route('/formularionotas', methods=['GET', 'POST'])
def estadoEstudiante():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
        promedio = (nota1+nota2+nota3)/3
        if promedio >= 40 and asistencia >= 75:
            estado = 'APROBADO'
        else:
            estado = 'REPROBADO'
        return render_template('formularionotas.html',estado=estado,promedio=promedio,asistencia=asistencia,nota1=nota1,nota2=nota2,nota3=nota3)
    return render_template('formularionotas.html')

@app.route('/formularionombres', methods=['GET', 'POST'])
def nombreMasLargo():
    if request.method == 'POST':
        resultado =''
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])
        largo1 = len(nombre1)
        largo2 = len(nombre2)
        largo3 = len(nombre3)
        if largo1 == largo2 == largo3:
            largo = largo1
            resultado = nombre1+', '+nombre2+', '+nombre3+' poseen la misma cantidad de caracteres en sus nombres.'
        elif largo1 == largo2 and largo1 > largo3:
            largo = largo1
            resultado = 'Los nombres con la mayor cantidad de caracteres son: '+nombre1+' y '+ nombre2+'.'
        elif largo1 == largo3 and largo1 > largo2:
            largo = largo1
            resultado = 'Los nombres con la mayor cantidad de caracteres son: '+nombre1+' y '+ nombre3+'.'
        elif largo2 == largo3 and largo2 > largo1:
            largo = largo2
            resultado = 'Los nombres con la mayor cantidad de caracteres son: ' + nombre2 + ' y ' + nombre2+'.'
        elif largo1 > largo2 and largo1 > largo3:
            largo = largo1
            resultado = 'El nombre con mayor cantidad de caracteres es: '+nombre1+'.'
        elif largo2 > largo1 and largo2 > largo3:
            largo = largo2
            resultado = 'El nombre con mayor cantidad de caracteres es: ' + nombre2 + '.'
        else:
            largo = largo3
            resultado = 'El nombre con mayor cantidad de caracteres es: ' + nombre3 + '.'
        return render_template('formularionombres.html', resultado=resultado, nombre1=nombre1, nombre2=nombre2, largo1=largo1, largo2=largo2, largo3=largo3, largo=largo)
    return render_template('formularionombres.html')


if __name__ =='__main__':
    app.run(debug=True)

