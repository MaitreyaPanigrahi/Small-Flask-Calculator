### Flask App  Routing


from flask import Flask,render_template,request,redirect,url_for,jsonify


## Create a simple flask application

app = Flask(__name__)

@app.route("/",methods =["GET"])
def welcome():
    return "<h1>Welcome to the first Flask App</h1>"



@app.route("/index",methods =["GET"])
def index():
    return "<h2>Welcome to the index page</h2>"

## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    return f"The person has passed the exam and the score is {score}"


@app.route('/fail/<int:score>')
def fail(score):
    return f"The person has failed the exam and the score is {score}"

@app.route('/form' , methods =['GET' , 'POST'])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        math = float(request.form['math'])
        science= float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (math + science + history) /3

        res = ""
        if average_marks >=50:
            res = "success"
        else:
            res = "fail"

        return redirect(url_for(res,score = average_marks))

        # return render_template('form.html' , score = average_marks)
    
@app.route('/api' , methods= ['POST'])    

def calculate_sum():
    data = request.get_json("test2.json")
    a_val = float(dict(data)["a"])
    b_val = float(dict(data)["b"])

    return jsonify(a_val - b_val)




if __name__ == "__main__":
    app.run(debug = True)
