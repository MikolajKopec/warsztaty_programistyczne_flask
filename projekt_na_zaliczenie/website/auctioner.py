from os import error, path
from flask import Blueprint, app,render_template,request
from flask.helpers import flash
from werkzeug.utils import secure_filename   
from flask_login import current_user,login_required
from . import create_app
auctioner = Blueprint('auctioner',__name__)

IMAGE_STORAGE = './website/auction_images/'
ALLOWED_EXTENSIONS = {'jpeg','png','webp','jpg','gif'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


@auctioner.route('/create_auction',methods=['GET','POST'])
def create_auction():
    if request.method=="GET":
        pass
    else:
        if 'img' not in request.files:
            flash('Please upload image',category='error')
        else:
            img = request.files['img']
            if img.filename == '':
                flash('Please upload image x2',category='error')
            elif img and allowed_file(img.filename):
                img_name = secure_filename(img.filename)
                img.save(path.join(IMAGE_STORAGE, img_name))
                flash('Your auction have been posted.',category='success')
            else:
                flash("Wrong format of photo. Check your image.",category='error')
    return render_template('create_auction.html', user = current_user)