from flask import Flask,render_template,jsonify

app=Flask(__name__)
Jobs=[{
    'id':1,
    'title':'Data Analyst',
    'location':'Bangalore',
    'salary':'Rs 100000'
       },
       {
    'id':2,
    'title':'QA Engineer',
    'location':'Pune',
    'salary':'Rs 200000'
       },
       {
    'id':1,
    'title':'Full Stack Developer',
    'location':'Trivandrum',
   
       }
       ]

@app.route("/")
def hello():
    return render_template('index.html',job=Jobs,companyname="Gops")

@app.route("/jobs")
def joblist():
    return jsonify(Jobs)
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)