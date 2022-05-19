import os, sys
real_path = os.path.dirname(os.path.realpath(__file__))
sub_path = os.path.split(real_path)[0]
os.chdir(sub_path)

from flask import Flask, escape, request,  Response, g, make_response
from flask.templating import render_template
from werkzeug.utils import secure_filename
from . import neural_style_transfer

app = Flask(__name__)
app.debug = True

def root_path():
	'''root 경로 유지'''
	real_path = os.path.dirname(os.path.realpath(__file__))
	sub_path = "\\".join(real_path.split("\\")[:-1])
	return os.chdir(sub_path)

''' Main page '''
@app.route('/')
def index():
	return render_template('index.html')

''' ConvNet info page '''
@app.route('/convnet_info')
def convnet_info():
	return render_template('convnet_info.html')

''' Scalp info page '''
@app.route('/scalp_info')
def scalp_info():
	return render_template('scalp_info.html')

''' Neural Style Transfer '''
@app.route('/nst_get')
def nst_get():
	return render_template('nst_get.html')

@app.route('/nst_post', methods=['GET','POST'])
def nst_post():
	if request.method == 'POST':
		root_path()

		# User Image (target image)
		user_img = request.files['user_img']
		user_img.save('./flask_deep/static/images/' + str(user_img.filename))
		user_img_path = '../static/images/' + str(user_img.filename)

		result2 = neural_style_transfer.main(user_img.filename)
	return render_template('nst_post.html', user_img=user_img_path, result = result2)