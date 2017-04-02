#!/usr/bin/env python
import os

from flask import Flask, send_from_directory, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'doc'
ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/<path:filename>')
def index(filename="index.html"):
    return send_from_directory('.', filename)

@app.route('/work_doc')
def work_doc():
    docs = os.walk('doc/work_doc')
    elements = []
    for el in docs:
        elements.append(el)

    docs = {}
    # scheme = []
    # for doc in elements[0][2]:
    #     scheme.append((elements[0][0] + '/' + doc, doc[:-4]))
    # docs['schemes'] = scheme

    cab_con = []
    for doc in elements[1][2]:
        cab_con.append((elements[1][0] + '/' + doc, doc[:-4]))
    docs['cab_cons'] = cab_con

    equip = []
    for doc in elements[7][2]:
        equip.append((elements[7][0] + '/' + doc, doc[:-4]))
    docs['equips'] = equip

    rooms = []
    for doc in elements[2][2]:
        rooms.append((elements[2][0] + '/' + doc, doc[:-4]))
    docs['rooms'] = rooms

    datas = []
    for doc in elements[3][2]:
        datas.append((elements[3][0] + '/' + doc, doc[:-4]))
    docs['datas'] = datas

    specs = []
    for doc in elements[5][2]:
        specs.append((elements[5][0] + '/' + doc, doc[:-4]))
    docs['specs'] = specs

    tasks = []
    for doc in elements[6][2]:
        tasks.append((elements[6][0] + '/' + doc, doc[:-4]))
    docs['tasks'] = tasks

    tracts = []
    for doc in elements[4][2]:
        tracts.append((elements[4][0] + '/' + doc, doc[:-4]))
    docs['tracts'] = tracts

    return render_template('work_doc.html', docs=docs)

@app.route('/net_doc')
def net_doc():
    docs = os.walk('doc/net_doc')
    elements = []
    for el in docs:
        elements.append(el)

    docs = []
    for doc in elements[0][2]:
        docs.append((elements[0][0] + '/' + doc, doc[:-4]))
    return render_template('net_doc.html', docs=docs)

@app.route('/prog_doc')
def prog_doc():
    docs = os.walk('doc/prog_doc')
    elements = []
    for el in docs:
        elements.append(el)

    docs = []
    for doc in elements[0][2]:
        docs.append((elements[0][0] + '/' + doc, doc[:-4]))
    return render_template('prog_doc.html', docs=docs)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/add_net_doc', methods=['GET', 'POST'])
def net_doc_upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/net_doc", filename))

            return redirect(url_for('net_doc'))
    return '''
    <!doctype html>
    <title>Загрузить сетевую документ</title>
    <h1>Загрузить новую сетевую документацию</h1>
    <form method=post enctype=multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Загрузить>
    </form>
    '''

@app.route('/add_prog_doc', methods=['GET', 'POST'])
def prog_doc_upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/prog_doc", filename))

            return redirect(url_for('prog_doc'))
    return '''
    <!doctype html>
    <title>Загрузить программную документ</title>
    <h1>Загрузить новую программную документацию</h1>
    <form method=post enctype=multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Загрузить>
    </form>
    '''

@app.route('/add_cab_con', methods=['GET', 'POST'])
def cab_con_upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/work_doc/cab_con", filename))

            return redirect(url_for('work_doc'))
    return '''
    <!doctype html>
    <title>Загрузить схему кабельных соединений</title>
    <h1>Загрузить новую схему кабельных соединений</h1>
    <form method=post enctype=multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Загрузить>
    </form>
    '''

@app.route('/add_equip', methods=['GET', 'POST'])
def equip_upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/work_doc/equip", filename))

            return redirect(url_for('work_doc'))
    return '''
    <!doctype html>
    <title>Загрузить схему расположения оборудования в шкафах</title>
    <h1>Загрузить новую схему расположения оборудования в шкафах</h1>
    <form method=post enctype=multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Загрузить>
    </form>
    '''

@app.route('/add_rooms', methods=['GET', 'POST'])
def rooms_upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/work_doc/rooms", filename))

            return redirect(url_for('work_doc'))
    return '''
    <!doctype html>
    <title>Загрузить план расположения оборудования и кабельных трасс</title>
    <h1>Загрузить новый план расположения оборудования и кабельных трасс</h1>
    <form method=post enctype=multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Загрузить>
    </form>
    '''

@app.route('/add_tracts', methods=['GET', 'POST'])
def tracts_upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/work_doc/tracts", filename))

            return redirect(url_for('work_doc'))
    return '''
    <!doctype html>
    <title>Загрузить схему прохождения трактов</title>
    <h1>Загрузить новую схему прохождения трактов</h1>
    <form method=post enctype=multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Загрузить>
    </form>
    '''

@app.route('/del', methods=['POST'])
def del_doc():
    if request.method == 'POST':
        os.remove(request.form['upfile'])
        print(request.form['upfile'])
    return redirect("type_doc.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
