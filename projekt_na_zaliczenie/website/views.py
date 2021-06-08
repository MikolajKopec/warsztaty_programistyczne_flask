from flask import Blueprint,render_template,request
from flask_login import current_user,login_required
from . import db
from .models import Auction
views = Blueprint('views',__name__)

@views.route('/',methods =['GET','POST'])
def home():
    auction = None
    auction = Auction.query.all()
    if request.method == "GET":
        pass
    else:
        bid = request.form['bid']
        id = request.form['auction_id']
        winner = current_user.login
        auction_price = Auction.query.filter_by(id = id).first()
        auction_price.cw=bid
        auction_price.winner=winner
        db.session.commit()
    return render_template('home.html', user = current_user,auction = auction)
