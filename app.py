
from flask import Flask, render_template, redirect, request, flash
import os, yaml
from forms import phoneForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'linuxdegilgnulinux'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/list/', methods = ['GET'])
def list():
    os.system("ls lineage_wiki/_data/devices/ > lineage_wiki/_data/devices/output.txt")
    file_names = []
    f = open("lineage_wiki/_data/devices/output.txt")

    for i in f:
        a = f.readline()
        file_names.append(a)
    f.close()

    for i in range(len(file_names)-1):
        file_path = "/home/ilteriskeskin/Belgeler/LineageOS-Bilgi/lineage_wiki/_data/devices/" + file_names[i].rstrip()
        with open(file_path, "r") as stream:
            try:
                file = yaml.load(stream, Loader=yaml.FullLoader)
                file_names.append(file)
            except:
                print()
    return render_template('list.html', file_names = file_names)

@app.route('/benchmark', methods=['GET', 'POST'])
def benchmark():
    os.system("ls lineage_wiki/_data/devices/ > lineage_wiki/_data/devices/output.txt")
    file_names = []
    f = open("lineage_wiki/_data/devices/output.txt", 'r')

    for i in f:
        a = f.readline()
        file_names.append(a)
    f.close()

    for i in range(len(file_names)-1):
        file_path = "/home/ilteriskeskin/Belgeler/LineageOS-Bilgi/lineage_wiki/_data/devices/" + file_names[i].rstrip()
        with open(file_path, "r") as stream:
            try:
                file = yaml.load(stream, Loader=yaml.FullLoader)
                file_names.append(file)
            except:
                print()

    form = phoneForm(request.form)
    if request.method == 'POST' and form.validate():
        phone1 = request.form['phone1']
        phone2 = request.form['phone2']
        phone1 = int(phone1)
        phone2 = int(phone2)

        phone1_path = "/home/ilteriskeskin/Belgeler/LineageOS-Bilgi/lineage_wiki/_data/devices/" + file_names[phone1 - 1].rstrip()
        phone2_path = "/home/ilteriskeskin/Belgeler/LineageOS-Bilgi/lineage_wiki/_data/devices/" + file_names[phone2 - 1].rstrip()

        with open(phone1_path, "r") as stream1:
            try:
                file1 = yaml.load(stream1, Loader=yaml.FullLoader)
                ram1 = file1["ram"]
            except:
                print()

        with open(phone2_path, "r") as stream2:
            try:
                file2 = yaml.load(stream2, Loader=yaml.FullLoader)
                ram2 = file2["ram"]
            except:
                print()
        
        if int(ram1[0]) > int(ram2[0]):
            flash('Birinci modelin rami, ikinci modelden daha yüksek.','success')
        elif int(ram1[0]) > int(ram2[0]):
            flash('İkinci modelin rami, birinci modelden daha yüksek.','success')
        else:
            flash('Modellerin RAMleri birbirine eşit.', 'success')
        return render_template('benchmark.html', file_names = file_names, form = form)

    return render_template('benchmark.html', file_names = file_names, form = form)

    
if __name__ == '__main__':
    app.run(debug=True)
