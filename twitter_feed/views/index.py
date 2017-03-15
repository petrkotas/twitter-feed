from flask import Blueprint, render_template


index_view = Blueprint('index_view', __name__, template_folder='templates', url_prefix='/')


@index_view.route('/', methods=['GET'])
def index():
    return render_template('index.html')