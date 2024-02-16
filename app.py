from flask import Flask, render_template, url_for, jsonify, flash, redirect
from contactForms import contactForm
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'edf0238db202d541748c1acf347afe48'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 

# create db instance (classes/models/tables)
db = SQLAlchemy(app)

# models
class Projects(db.Model):
    id = db.Column(db.Integer ,  primary_key=True)
    project_name = db.Column(db.String(50) , unique= True, nullable = False)
    project_details = db.Column(db.String(200) , nullable = False)
    project_image = db.Column(db.String(20) , nullable = False)






# routes decorators: additional functionaily to existing functions
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route("/")
@app.route("/home")
def home():
    # return a html page
    return render_template('home.html', title='Home', active_page='home')

@app.route("/about")
def about():
    response = leetcode_api()
    # print(response)
    return render_template('about.html', title='About', active_page='about', response=response)

@app.route("/resume")
def resume():
    return render_template('resume.html', title='Resume',active_page='resume')

@app.route("/projects")
def projects():
    return render_template('projects.html', title='Projects',active_page='projects')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = contactForm()
    if form.validate_on_submit():
        flash(f'Message Sent Successfully!!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', title='Contact', active_page='contact', form=form)



def leetcode_api():
    # Send GET request to Leetcode API with username
    response = requests.get("https://leetcode-stats-api.herokuapp.com/samiksha-lokhande/")
    # Parse the response and extract the total number of problems solved
    data = response.json()
    # print(data)
    response = {}
    response['totalSolved'] =  data["totalSolved"]
    response['easySolved'] =  data["easySolved"]
    response['mediumSolved'] =  data["mediumSolved"]
    response['hardSolved'] =  data["hardSolved"]
    # total_solved = data["totalSolved"]
    print(response)
    # Return the information as a JSON response
    return response

if __name__ == '__main__':
    app.run(debug=True)