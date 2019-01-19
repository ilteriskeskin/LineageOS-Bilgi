
from flask import Flask, render_template, redirect, request
import os, yaml

app = Flask(__name__)
app.config['SECRET_KEY'] = 'linuxdegilgnulinux'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/list')
def list():
    os.system("ls lineage_wiki/_data/devices/ > lineage_wiki/_data/devices/output.txt")
    file_names = []

    f = open("lineage_wiki/_data/devices/output.txt")

    for i in f:
        a = f.readline()
        file_names.append(a)

    for i in range(len(file_names)):

        file_path = "/home/ilteriskeskin/Belgeler/Python/lineage_wiki/_data/devices/" + file_names[i].rstrip()

        with open(file_path, "r") as stream:
            try:
                file = yaml.load(stream)
                #print(i + 1,file["vendor"], file["name"])
                file_names.append(file)
            except:
                print()
    
    return render_template('list.html', file_names = file_names)

@app.route('/benchmark')
def benchmark():
    os.system("ls lineage_wiki/_data/devices/ > lineage_wiki/_data/devices/output.txt")
    file_names = []

    f = open("lineage_wiki/_data/devices/output.txt")

    for i in f:
        a = f.readline()
        file_names.append(a)

    for i in range(len(file_names)):

        file_path = "/home/ilteriskeskin/Belgeler/Python/lineage_wiki/_data/devices/" + file_names[i].rstrip()

        with open(file_path, "r") as stream:
            try:
                file = yaml.load(stream)
                #print(i + 1,file["vendor"], file["name"])
                file_names.append(file)
            except:
                print()
    
    return render_template('benchmark.html', file_names = file_names)
    
if __name__ == '__main__':
    app.run(debug=True)