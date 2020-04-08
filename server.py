from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/<username>/<int:post_id>')
def greet_world(username=None, post_id=None):
    #print(url_for('static', filename='favicon.ico'))
    return render_template('index.html', name=username, id=post_id)

@app.route('/blog')
def blog_world():
    return 'Crofts way!'

#@app.route('/blog/2020/dogs')
#def blog_2020():
    #return 'perceptron created!'

@app.route('/')
def my_home():
    return render_template('index.html')

#@app.route('/index.html')
#def my_home_link():
    #return render_template('index.html')

#@app.route('/works.html')
#def my_works():
    #return render_template('works.html')

#@app.route('/about.html')
#def my_about():
    #return render_template('about.html')

#@app.route('/contact.html')
#def my_contact():
    #return render_template('contact.html')

#@app.route('/components.html')
#def my_components():
    #return render_template('components.html')

@app.route('/<string:page_name>')
def my_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def form():
    if request.method=='POST':
        try:
            data = request.form.to_dict()
            log_CSVdata(data)
            #return render_template('login.html', error=error)
            return redirect('/thankyou.html')
        except:
            return 'did not saved to database'
    else:
        return 'something went wrong. Pls try again'

def log_data(data):
    with open('database.txt', mode='a',) as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email},{subject},{message}')

def log_CSVdata(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email,subject,message])