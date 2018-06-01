import os
from app import app
from flask import request, jsonify,make_response
import uuid
import json
import time
from app.models import *

def wrap(arg):
    response = make_response(arg)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response

def loadUser():
    basepath = os.path.dirname(__file__)
    userfile=os.path.join(basepath, 'storage/users/users.json')
    if os.path.exists(userfile):
        with open(userfile, 'rb') as load_f:
            user = json.load(load_f)
            users=[]
            for u in user:
                users.append(Author.Author(u))
            return  users
    return None


@app.route('/',methods=['POST', 'GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/api/v1/user/<int:id>',methods=['POST', 'GET'])
def user(id):
    def interfun():
        token=request.args['token']
        users=loadUser()
        if users is not None:
            for u in users:
                if id==u.id and token==u.token:
                    return jsonify({'state':'ok',"userinfo":u.__dict__})
        return jsonify({'state':'error'})
    return wrap(interfun())

@app.route('/api/v1/ArticleList/<int:id>', methods=['POST', 'GET'])
def articlelist(id):
    def interfun():
        users=loadUser()
        if users is not None:
            for u in users:
                if id==u.id :
                    basepath = os.path.dirname(__file__)
                    filesfile = os.path.join(basepath, 'storage/files/'+str(id)+'/index.json')
                    with open(filesfile, 'rb') as load_f:
                        files_f = json.load(load_f)
                        return jsonify({'state':'ok',"filesList":files_f})
        return jsonify({'state':'error'})
    return wrap(interfun())

@app.route('/api/v1/Article/<int:id>', methods=['POST', 'GET'])
def article(id):
    def interfun():
        aid=None
        if "aid" in request.args:
            aid=request.args["aid"]
        users = loadUser()
        if request.method=="GET":
            if users is not None:
                for u in users:
                    if id == u.id:
                        basepath = os.path.dirname(__file__)
                        filesfile = os.path.join(basepath, 'storage/files/' + str(id) + '/index.json')
                        with open(filesfile, 'rb') as load_f:
                            files_f = json.load(load_f)
                            files=[]
                            for file in files_f:
                                files.append(Article.Article(file))
                            for file in files:
                                if file.aid== aid:
                                    articlefile=os.path.join(basepath, 'storage/files/' + str(id) + '/'+aid)
                                    if os.path.exists(articlefile):
                                        with open(articlefile, 'rb') as load_f_article:
                                            content=load_f_article.read()
                                            return jsonify({'state': 'ok', "article": {"header": file.__dict__,
                                                                                       "content": str(content)}})
                                    return jsonify({'state': 'error'})
                            return jsonify({'state': 'error'})
            return jsonify({'state': 'error'})
        if request.method == "POST":
            try:
                postdata= json.loads(request.data)
            except:
                return jsonify({'state': 'error'})
            token =None
            if "token" in postdata:
                token =postdata["token"]
            title=None
            if "title" in postdata:
                title =postdata["title"]
            content=None
            if "content" in postdata:
                content =postdata["content"]
            if token is not None:
                if users is not None:
                    for u in users:
                        if id == u.id and token==u.token:
                            if aid is not None:
                                if title is not None:
                                    basepath = os.path.dirname(__file__)
                                    filesfile = os.path.join(basepath, 'storage/files/' + str(id) + '/index.json')
                                    files = []
                                    with open(filesfile, 'rb') as load_f:
                                        files_f = json.load(load_f)
                                        for f in files_f:
                                            if f['aid']==aid:
                                                tmp=f;
                                                tmp["title"]=title
                                                files.append(tmp)
                                            else:
                                                files.append(f)
                                    with open(filesfile, 'w') as write_f:
                                        json.dump(files,write_f )
                                        return  jsonify({'state': 'ok'})
                                if content is not None:
                                    basepath = os.path.dirname(__file__)
                                    articlefile = os.path.join(basepath, 'storage/files/' + str(id) + '/' + aid)
                                    if os.path.exists(articlefile):
                                        with open(articlefile, 'w') as write_f:
                                            write_f.write(content)
                                            return jsonify({'state': 'ok'})
                                return jsonify({'state': 'error'})
                            else:
                                if content is not None and title is not None:
                                    basepath = os.path.dirname(__file__)
                                    filesfile = os.path.join(basepath, 'storage/files/' + str(id) + '/index.json')
                                    files_f=None
                                    with open(filesfile, 'rb') as load_f:
                                        files_f = json.load(load_f)
                                        articlefile = os.path.join(basepath, 'storage/files/' + str(id) + '/')
                                        filename = str(uuid.uuid4());
                                        while os.path.exists(os.path.join(articlefile, filename)):
                                            filename = str(uuid.uuid4());
                                        now = int(round(time.time() * 1000))
                                        files_f.append({"aid":filename,"title":title,"date":now})
                                        with open(os.path.join(articlefile, filename), 'w') as write_f:
                                            write_f.write(content)
                                    with open(filesfile, 'w') as write_f:
                                        json.dump(files_f,write_f)
                                    return jsonify({'state': 'ok'})
        return jsonify({'state': 'error'})
    return wrap(interfun())