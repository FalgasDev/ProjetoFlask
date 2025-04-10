from flask import Flask

app = Flask(__name__)
app.config['HOST'] = 'localhost'
app.config['PORT'] = 5000
app.config['DEBUG'] = True