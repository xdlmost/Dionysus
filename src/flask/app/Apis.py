import os
from app import app
from flask import request, jsonify
import uuid
import json

@app.route('/',methods=['POST', 'GET'])
def test_index():
    return app.send_static_file('index.html')
@app.route('/api/test',methods=['POST', 'GET'])
def test_index():
    return app.send_static_file('test.html')
@app.route('/api/display',methods=['POST', 'GET'])
def display():
    user = None
    basepath = os.path.dirname(__file__)
    user_path = os.path.join(basepath, 'storage/users/1.json')
    with open(user_path, 'r') as load_f:
        user = json.load(load_f)
    return  jsonify(user)

@app.route('/api/upload-image',methods=['POST', 'GET'])
def upload_image():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'storage/images')
        if 'image'not in f.mimetype:
            return jsonify({'status':'error','note': 'not support non-images.'})
        if len(f.read()) >15*1024*1024:
            return jsonify({'status':'error','note': 'too big'})
        filename=str(uuid.uuid4());
        while os.path.exists(os.path.join(upload_path,filename)):
            filename = str(uuid.uuid4());
        f.save(os.path.join(upload_path,filename))
        user = None
        basepath = os.path.dirname(__file__)
        user_path = os.path.join(basepath, 'storage/users/1.json')
        with open(user_path, 'r') as load_f:
            user = json.load(load_f)
        with open(user_path, 'w') as over_f:
            user['images'].append('storage/images/'+filename)
            json.dump(user, over_f)
        return jsonify({'status':'ok','note':'storage/images/'+filename})
    else:
        return jsonify({'status':'error','note':'not support get request.'})

@app.route('/api/upload-md',methods=['POST', 'GET'])
def upload_md():
    if request.method == 'POST':
        name = request.form['name'];
        md=request.form['md'];

        basepath = os.path.dirname(__file__)
        user_path = os.path.join(basepath, 'storage/users/1.json')
        upload_path = os.path.join(basepath, 'storage/files')
        filename = str(uuid.uuid4());
        while os.path.exists(os.path.join(upload_path, filename)):
            filename = str(uuid.uuid4());
        with open(os.path.join(upload_path, filename), 'w') as md_f:
            md_f.write(md)
        user = None
        with open(user_path, 'r') as load_f:
            user = json.load(load_f)
        user['files'].append({'name':name,'file':'storage/files/'+filename})
        with open(user_path, 'w') as over_f:
            user['images'].append('storage/images/'+filename)
            json.dump(user, over_f)
        return jsonify({'status': 'ok', 'note': 'storage/files/' + filename})
    else:
        return jsonify({'status':'error','note':'not support get request.'})

@app.route('/api/get-md',methods=['POST', 'GET'])
def get_md():
    if request.method == 'POST':
        basepath = os.path.dirname(__file__)
        md_path = os.path.join(basepath, bytes.decode(request.data))
        if os.path.exists(md_path):
            strr=''
            with open(md_path, 'r') as md_f:
                strr=md_f.read()
            return strr
        else:
            return jsonify({'status': 'error', 'note': 'not file.'})
    else:
        return jsonify({'status':'error','note':'not support get request.'})