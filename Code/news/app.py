import json
from flask import Flask,render_template,request

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True
#app.run(port=3000)

@app.route('/')
def index():
    message_title=[]
    with open('/home/shiyanlou/files/helloshiyanlou.json','r') as f:
        message1= json.loads(f.read())
        message_title.append(message1['title'])
    with open('/home/shiyanlou/files/helloworld.json','r') as f:
        message2= json.loads(f.read())
        message_title.append(message2['title'])
        return render_template('index.html',message_title=message_title)

@app.route('/files/<filename>')    
def file(filename):
    f=open('/home/shiyanlou/files/'+filename+'.json','r')
    message= json.loads(f.read())
    return render_template('file.html',message=message)

@app.errorheadler(404)
def not_found(error):
        return render_template('404.html',str404='shiyanlou 404'),404
# print(message_title)
