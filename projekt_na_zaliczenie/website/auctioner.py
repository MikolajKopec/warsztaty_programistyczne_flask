from os import error, path
from flask import Blueprint, app,render_template,request
from flask.helpers import flash
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import null
from werkzeug.utils import secure_filename   
from flask_login import current_user,login_required
from .models import Auction
from . import create_app,db
auctioner = Blueprint('auctioner',__name__)

IMAGE_STORAGE = './website/static/auction_images/'
ALLOWED_EXTENSIONS = {'jpeg','png','webp','jpg','gif'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


@auctioner.route('/create_auction',methods=['GET','POST'])
def create_auction():
    info = None
    category = 'error'
    if request.method=="GET":
        pass
    else:
        item = request.form['item']
        cw = request.form['cw']
        kt = request.form['kt']
        more = request.form['more']
        if len(item)>30 or len(item)<6:
            info = "Your item name is too long, or too short (shoud be 6-30 characters)."
            print(item)
        elif len(more)>300:
            info = "Please make your additional infiormation shorter (max. 300 characters)."
        elif 'img' not in request.files:
            info = "Please upload image"
        else:
            img = request.files['img']
            if img.filename == '':
                img.filename ="auction.png"
            if img and allowed_file(img.filename):
                img_name = secure_filename(img.filename)
                storage = path.join(IMAGE_STORAGE, img_name)
                img.save(storage)
                info = 'Your auction have been posted.'
                category='success'
            else:
                info = "Wrong format of photo. Check your image."
        if category=='success':
            new_auction = Auction(item_name=item,cw=cw,kt=kt,informations=more,img = img_name, owner_id = current_user.id)
            db.session.add(new_auction)
            db.session.commit()
    if info is not None:
        flash(info,category=category)
    return render_template('create_auction.html', user = current_user)