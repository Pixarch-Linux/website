from flask import Flask, render_template, url_for 

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')

def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download')
def download():
    return render_template('downloads.html')

if __name__ == "__main__":
    app.run(debug=True)
