# Aula 08 -redirecionamento e erros
from configparser import ConfigParser
from flask import Flask,request , abort , redirect, url_for #
# (abort =parar abortar(), redirect(url_for)
import json

app =Flask(__name__,static_folder='static')
# app.send_static_file("static")
path_configurer="configs.ini"
config=ConfigParser()
def settings_file_ini(filename):
    ...

# salvando os dados digitados nos imputs do formulario
def save_files(file_name,config):
    print('trying to save user files')
    with open(file_name,'w') as file_conf:
        config.write(file_conf)
        print('file set sucess fully')
    return 'Save ok !'

def read_file_ini(file_name,config,section='user'):
    with open(file_name) as files:
        config.read(files)
        print(config.get(section, 'user_name'))
        _uname=config.get(section,'user_name')
        _upass=config.get(section, 'user_pass')
        dados={'user_name':_uname, 'user_pass':_upass}
        return json.dumps(dados)
    return 'Fail loading file!'



@app.route("/login", methods=['GET','POST'])
def login():

    print(request.method)
    if request.method=='POST':
        _uname = request.form['user_name']
        _upass = request.form['user_password']
        print("\033[36m[User typed these inputs]\033[m " + _uname, _upass)
        import random
        if _uname !="" and _upass !="":
            config['user']={
                'user_name':_uname,
                'user_pass':_upass
            }
            save_files(path_configurer, config)

            #se usuario preecher com os dados avaliados :
            if _uname=="saidino" and _upass=="claudia":
                # ele vai ser redirecionado para arouta "sucess"
                'com estatus code=302 ele redireciona sozinho'
                return redirect(url_for('sucess'), code=302)
            else:
                # "caso os dados nao forem de saidino ele ira simplesmente abortar"
                return redirect(url_for('user_failed'), code=200) #se eu colocar code=200, ele
                #             nao vai redirecionar automaticamente sozinho se nao eu permitir
                # return redirect(url_for('entra_user'))
                # return "HHHH"
    else:
        return abort(403) #erro proibido [forbiden]

@app.route("/sucess")
def sucess():
    return "User saved OK!"

@app.route('/entra_user')
def entra_user():
    return "Herro de servidor<script>a=window.prompt('qual é seu nome ') ;alert(a)</script>"
    # return "Hello"

@app.route("/user_failed")
def user_failed():
    return "<H3> Verifique os seus dados pork sao invalidos </h3>"



if __name__ == '__main__':
    print("[AULA 08 ]")
    app.run(debug=True,host='0.0.0.0',port=8080)