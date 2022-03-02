from flask import render_template, request, Blueprint
from website.models import Post

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template("home.html", title=home)

@main.route('/test')
def test():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("test.html", posts=posts)

@main.route('/history')
def history():
    return render_template("history.html", title=history)