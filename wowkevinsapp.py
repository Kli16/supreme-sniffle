from flask import Flask, render_template
from utils import occupation as oc

my_app = Flask(__name__)

data = oc.setup()

@my_app.route('/')
@my_app.route('/occupations')
def occupation():
    return render_template('occupations.html', occtable = data, randelement = oc.getRandWeighted(data))

if __name__ == '__main__':
    my_app.debug = True;
    my_app.run()
